import os
import shutil
import subprocess
import sys
from dataclasses import dataclass

from .lessons import get_lesson, lesson_directory
from .paths import PROJECT_ROOT
from .progress import record_check, reset_lesson_progress


@dataclass(frozen=True)
class CheckResult:
    passed: bool
    output: str
    return_code: int


def run_lesson_tests(lesson_id: str, *, record: bool = True) -> CheckResult:
    lesson = get_lesson(lesson_id)
    workspace = lesson_directory(lesson)
    ensure_workspace(lesson)
    environment = os.environ.copy()
    environment["PYTHONPATH"] = str(workspace)
    command = [
        sys.executable,
        "-m",
        "unittest",
        "discover",
        "-s",
        str(workspace),
        "-p",
        "test_solution.py",
        "-v",
    ]
    try:
        completed = subprocess.run(
            command,
            cwd=PROJECT_ROOT,
            env=environment,
            capture_output=True,
            text=True,
            timeout=12,
            check=False,
        )
        output = (completed.stdout + completed.stderr).strip()
        passed = completed.returncode == 0
        result = CheckResult(passed, output, completed.returncode)
    except subprocess.TimeoutExpired as error:
        partial = "".join(
            value for value in (error.stdout, error.stderr) if isinstance(value, str)
        ).strip()
        output = "The check timed out after 12 seconds. Look for an infinite loop."
        if partial:
            output = f"{partial}\n\n{output}"
        result = CheckResult(False, output, 124)

    if record:
        record_check(lesson_id, result.passed)
    return result


def ensure_workspace(lesson: dict) -> None:
    workspace = lesson_directory(lesson)
    workspace.mkdir(parents=True, exist_ok=True)
    module_link = workspace / "learnlab"
    solution_path = workspace / "solution.py"
    test_path = workspace / "test_solution.py"
    readme_path = workspace / "README.md"
    if not module_link.exists() and not module_link.is_symlink():
        module_link.symlink_to(PROJECT_ROOT / "learnlab", target_is_directory=True)
    if not solution_path.exists():
        solution_path.write_text(lesson["starter"].rstrip() + "\n", encoding="utf-8")
    test_path.write_text(lesson["tests"].rstrip() + "\n", encoding="utf-8")
    readme_path.write_text(
        f"# {lesson['title']}\n\n{lesson['assignment']}\n\n"
        f"Run from this assignment folder or the project root:\n\n"
        f"```bash\npython3 -m learnlab check {lesson['id']}\n```\n",
        encoding="utf-8",
    )


def ensure_all_workspaces() -> None:
    from .lessons import LESSONS

    for lesson in LESSONS:
        ensure_workspace(lesson)


def reset_lesson(lesson_id: str) -> None:
    lesson = get_lesson(lesson_id)
    workspace = lesson_directory(lesson)
    workspace.mkdir(parents=True, exist_ok=True)
    (workspace / "solution.py").write_text(
        lesson["starter"].rstrip() + "\n", encoding="utf-8"
    )
    cache = workspace / "__pycache__"
    if cache.exists():
        shutil.rmtree(cache)
    ensure_workspace(lesson)
    reset_lesson_progress(lesson_id)
