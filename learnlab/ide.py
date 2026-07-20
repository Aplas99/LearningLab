import shlex
import shutil
import subprocess
import sys
from pathlib import Path

from .lessons import get_lesson, lesson_directory
from .settings import IDE_OPTIONS_BY_ID, load_settings


IDE_LAUNCHERS = {
    "vscode": {"executables": ("code",), "mac_app": "Visual Studio Code"},
    "cursor": {"executables": ("cursor",), "mac_app": "Cursor"},
    "pycharm": {"executables": ("pycharm", "charm"), "mac_app": "PyCharm"},
    "pycharm-community": {
        "executables": ("pycharm", "charm"),
        "mac_app": "PyCharm CE",
    },
    "zed": {"executables": ("zed",), "mac_app": "Zed"},
    "sublime": {"executables": ("subl",), "mac_app": "Sublime Text"},
}


class IDELaunchError(RuntimeError):
    """Raised when the configured IDE cannot be launched."""


def build_launch_command(
    workspace: Path,
    settings: dict,
    *,
    which=shutil.which,
    platform: str = sys.platform,
) -> list[str]:
    ide = settings.get("ide", {})
    ide_id = ide.get("id")
    if ide_id not in IDE_OPTIONS_BY_ID:
        raise IDELaunchError("Choose an IDE before opening the assignment.")

    if ide_id == "custom":
        try:
            parts = shlex.split(ide.get("custom_command", ""))
        except ValueError as error:
            raise IDELaunchError(f"The custom IDE command is invalid: {error}") from error
        if not parts:
            raise IDELaunchError("Enter a custom IDE command.")
        executable = _resolve_executable(parts[0], which)
        if not executable:
            raise IDELaunchError(f"Could not find the IDE executable: {parts[0]}")
        return [executable, *parts[1:], str(workspace)]

    launcher = IDE_LAUNCHERS[ide_id]
    for executable_name in launcher["executables"]:
        executable = which(executable_name)
        if executable:
            return [executable, str(workspace)]

    if platform == "darwin":
        open_executable = which("open") or "/usr/bin/open"
        return [open_executable, "-a", launcher["mac_app"], str(workspace)]

    label = IDE_OPTIONS_BY_ID[ide_id]["label"]
    raise IDELaunchError(
        f"Could not find {label}. Install its command-line launcher or choose another IDE."
    )


def _resolve_executable(value: str, which=shutil.which) -> str | None:
    candidate = Path(value).expanduser()
    if candidate.is_absolute():
        return str(candidate) if candidate.is_file() else None
    return which(value)


def open_lesson_in_ide(lesson_id: str) -> str:
    lesson = get_lesson(lesson_id)
    workspace = lesson_directory(lesson)
    settings = load_settings()
    command = build_launch_command(workspace, settings)

    if len(command) >= 3 and command[1] == "-a":
        check = subprocess.run(
            [command[0], "-Ra", command[2]],
            capture_output=True,
            text=True,
            timeout=4,
            check=False,
        )
        if check.returncode != 0:
            raise IDELaunchError(
                f"Could not find {command[2]}. Choose another IDE or custom command."
            )

    try:
        subprocess.Popen(
            command,
            stdout=subprocess.DEVNULL,
            stderr=subprocess.DEVNULL,
            start_new_session=True,
        )
    except OSError as error:
        raise IDELaunchError(f"Could not launch the IDE: {error}") from error

    ide_id = settings["ide"]["id"]
    return IDE_OPTIONS_BY_ID[ide_id]["label"]
