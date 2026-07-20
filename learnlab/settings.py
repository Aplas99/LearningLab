import json
import os
import tempfile
from pathlib import Path
from threading import Lock

from .paths import SETTINGS_FILE


IDE_OPTIONS = [
    {"id": "vscode", "label": "Visual Studio Code"},
    {"id": "cursor", "label": "Cursor"},
    {"id": "pycharm", "label": "PyCharm"},
    {"id": "pycharm-community", "label": "PyCharm Community"},
    {"id": "zed", "label": "Zed"},
    {"id": "sublime", "label": "Sublime Text"},
    {"id": "custom", "label": "Custom command", "custom": True},
]
IDE_OPTIONS_BY_ID = {option["id"]: option for option in IDE_OPTIONS}

_LOCK = Lock()


def _empty_settings() -> dict:
    return {"version": 1, "ide": {"id": None, "custom_command": ""}}


def load_settings(path: Path = SETTINGS_FILE) -> dict:
    with _LOCK:
        if not path.exists():
            return _empty_settings()
        try:
            data = json.loads(path.read_text(encoding="utf-8"))
        except (OSError, json.JSONDecodeError):
            return _empty_settings()

        ide = data.get("ide", {}) if isinstance(data, dict) else {}
        ide_id = ide.get("id")
        custom_command = ide.get("custom_command", "")
        if ide_id not in IDE_OPTIONS_BY_ID or not isinstance(custom_command, str):
            return _empty_settings()
        return {
            "version": 1,
            "ide": {"id": ide_id, "custom_command": custom_command},
        }


def save_ide_settings(
    ide_id: str, custom_command: str = "", path: Path = SETTINGS_FILE
) -> dict:
    if ide_id not in IDE_OPTIONS_BY_ID:
        raise ValueError("Choose a supported IDE.")
    custom_command = custom_command.strip()
    if ide_id == "custom" and not custom_command:
        raise ValueError("Enter a custom IDE command.")
    if len(custom_command) > 500:
        raise ValueError("The custom IDE command is too long.")

    data = {
        "version": 1,
        "ide": {
            "id": ide_id,
            "custom_command": custom_command if ide_id == "custom" else "",
        },
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    with _LOCK:
        with tempfile.NamedTemporaryFile(
            "w", encoding="utf-8", dir=path.parent, delete=False
        ) as handle:
            json.dump(data, handle, indent=2, sort_keys=True)
            handle.write("\n")
            temporary_path = Path(handle.name)
        os.replace(temporary_path, path)
    return data


def public_ide_settings(path: Path = SETTINGS_FILE) -> dict:
    settings = load_settings(path)
    selected_id = settings["ide"]["id"]
    selected = IDE_OPTIONS_BY_ID.get(selected_id)
    return {
        "selected_id": selected_id,
        "selected_label": selected["label"] if selected else None,
        "custom_command": settings["ide"]["custom_command"],
        "options": IDE_OPTIONS,
    }
