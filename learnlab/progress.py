import json
import os
import tempfile
from datetime import datetime, timezone
from pathlib import Path
from threading import Lock

from .paths import PROGRESS_FILE


_LOCK = Lock()


def _empty_progress() -> dict:
    return {"version": 1, "lessons": {}}


def load_progress(path: Path = PROGRESS_FILE) -> dict:
    with _LOCK:
        if not path.exists():
            return _empty_progress()
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return _empty_progress()
        if not isinstance(data, dict) or not isinstance(data.get("lessons"), dict):
            return _empty_progress()
        return data


def _save_progress(data: dict, path: Path = PROGRESS_FILE) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w", encoding="utf-8", dir=path.parent, delete=False
    ) as handle:
        json.dump(data, handle, indent=2, sort_keys=True)
        handle.write("\n")
        temporary_path = Path(handle.name)
    os.replace(temporary_path, path)


def record_check(lesson_id: str, passed: bool, path: Path = PROGRESS_FILE) -> dict:
    with _LOCK:
        if path.exists():
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                data = _empty_progress()
        else:
            data = _empty_progress()

        previous = data["lessons"].get(lesson_id, {})
        attempts = int(previous.get("attempts", 0)) + 1
        data["lessons"][lesson_id] = {
            "completed": bool(previous.get("completed")) or passed,
            "attempts": attempts,
            "last_checked_at": datetime.now(timezone.utc).isoformat(),
            "last_result": "passed" if passed else "failed",
        }
        _save_progress(data, path)
        return data["lessons"][lesson_id]


def reset_lesson_progress(lesson_id: str, path: Path = PROGRESS_FILE) -> None:
    with _LOCK:
        if path.exists():
            try:
                data = json.loads(path.read_text(encoding="utf-8"))
            except (OSError, json.JSONDecodeError):
                data = _empty_progress()
        else:
            data = _empty_progress()
        data["lessons"].pop(lesson_id, None)
        _save_progress(data, path)
