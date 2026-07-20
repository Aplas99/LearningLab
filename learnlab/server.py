import json
import mimetypes
import shlex
from http import HTTPStatus
from http.server import BaseHTTPRequestHandler, ThreadingHTTPServer
from pathlib import Path
from urllib.parse import unquote, urlparse

from .checker import ensure_all_workspaces, reset_lesson, run_lesson_tests
from .ide import IDELaunchError, open_lesson_in_ide
from .lessons import CATEGORIES, LESSONS, get_lesson, lesson_directory
from .paths import PROJECT_ROOT, STATIC_DIR
from .progress import load_progress
from .settings import public_ide_settings, save_ide_settings


def _public_lesson(item: dict, progress: dict) -> dict:
    learner_state = progress.get("lessons", {}).get(item["id"], {})
    workspace = lesson_directory(item)
    return {
        key: value
        for key, value in item.items()
        if key not in {"starter", "tests"}
    } | {
        "assignment_path": str(workspace),
        "solution_path": str(workspace / "solution.py"),
        "cd_command": f"cd {shlex.quote(str(workspace))}",
        "check_command": f"python3 -m learnlab check {shlex.quote(item['id'])}",
        "progress": {
            "completed": bool(learner_state.get("completed")),
            "attempts": int(learner_state.get("attempts", 0)),
            "last_result": learner_state.get("last_result"),
            "last_checked_at": learner_state.get("last_checked_at"),
        },
    }


def application_state() -> dict:
    progress = load_progress()
    lessons = [_public_lesson(item, progress) for item in LESSONS]
    completed = sum(item["progress"]["completed"] for item in lessons)
    return {
        "app": {"name": "LearnLab", "version": "0.1.0"},
        "categories": CATEGORIES,
        "lessons": lessons,
        "summary": {"completed": completed, "total": len(lessons)},
        "ide": public_ide_settings(),
        "project_root": str(PROJECT_ROOT),
    }


class LearnLabHandler(BaseHTTPRequestHandler):
    server_version = "LearnLab/0.1"

    def do_GET(self):
        parsed = urlparse(self.path)
        if parsed.path == "/api/state":
            self._send_json(application_state())
            return
        if parsed.path == "/health":
            self._send_json({"status": "ok"})
            return
        self._serve_static(parsed.path)

    def do_POST(self):
        parsed = urlparse(self.path)
        if parsed.path == "/api/settings/ide":
            try:
                payload = self._read_json()
                save_ide_settings(
                    payload.get("ide_id"), payload.get("custom_command", "")
                )
            except (ValueError, json.JSONDecodeError) as error:
                self._send_json({"error": str(error)}, HTTPStatus.BAD_REQUEST)
                return
            self._send_json({"saved": True, "state": application_state()})
            return

        parts = [unquote(part) for part in parsed.path.strip("/").split("/")]
        if len(parts) != 4 or parts[0] != "api" or parts[1] != "lessons":
            self._send_json({"error": "Not found"}, HTTPStatus.NOT_FOUND)
            return

        lesson_id = f"{parts[2]}/{parts[3].rsplit(':', 1)[0]}"
        action = parts[3].rsplit(":", 1)[-1] if ":" in parts[3] else ""
        try:
            get_lesson(lesson_id)
            if action == "check":
                result = run_lesson_tests(lesson_id)
                self._send_json(
                    {
                        "passed": result.passed,
                        "output": result.output,
                        "return_code": result.return_code,
                        "state": application_state(),
                    }
                )
                return
            if action == "reset":
                reset_lesson(lesson_id)
                self._send_json({"reset": True, "state": application_state()})
                return
            if action == "open":
                ide_label = open_lesson_in_ide(lesson_id)
                self._send_json({"opened": True, "ide_label": ide_label})
                return
        except KeyError:
            self._send_json({"error": "Unknown lesson"}, HTTPStatus.NOT_FOUND)
            return
        except IDELaunchError as error:
            self._send_json({"error": str(error)}, HTTPStatus.CONFLICT)
            return
        except OSError as error:
            self._send_json(
                {"error": f"Local file operation failed: {error}"},
                HTTPStatus.INTERNAL_SERVER_ERROR,
            )
            return

        self._send_json({"error": "Not found"}, HTTPStatus.NOT_FOUND)

    def _read_json(self) -> dict:
        content_length = int(self.headers.get("Content-Length", "0"))
        if content_length <= 0 or content_length > 16_384:
            raise ValueError("A small JSON request body is required.")
        payload = json.loads(self.rfile.read(content_length).decode("utf-8"))
        if not isinstance(payload, dict):
            raise ValueError("The JSON request body must be an object.")
        return payload

    def _serve_static(self, requested_path: str):
        relative = "index.html" if requested_path in {"", "/"} else requested_path.lstrip("/")
        candidate = (STATIC_DIR / relative).resolve()
        try:
            candidate.relative_to(STATIC_DIR.resolve())
        except ValueError:
            self.send_error(HTTPStatus.FORBIDDEN)
            return
        if not candidate.is_file():
            self.send_error(HTTPStatus.NOT_FOUND)
            return
        content_type, _ = mimetypes.guess_type(candidate.name)
        body = candidate.read_bytes()
        self.send_response(HTTPStatus.OK)
        self.send_header("Content-Type", f"{content_type or 'application/octet-stream'}; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def _send_json(self, payload, status=HTTPStatus.OK):
        body = json.dumps(payload).encode("utf-8")
        self.send_response(status)
        self.send_header("Content-Type", "application/json; charset=utf-8")
        self.send_header("Content-Length", str(len(body)))
        self.send_header("Cache-Control", "no-store")
        self.end_headers()
        self.wfile.write(body)

    def log_message(self, format_string, *args):
        print(f"[learnlab] {self.address_string()} - {format_string % args}")


def serve(host="127.0.0.1", port=8000):
    ensure_all_workspaces()
    server = ThreadingHTTPServer((host, port), LearnLabHandler)
    print(f"LearnLab is running at http://{host}:{port}")
    print("Press Ctrl+C to stop.")
    try:
        server.serve_forever()
    except KeyboardInterrupt:
        print("\nStopping LearnLab.")
    finally:
        server.server_close()
