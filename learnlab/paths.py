from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parent.parent
STATIC_DIR = PROJECT_ROOT / "static"
ASSIGNMENTS_DIR = PROJECT_ROOT / "assignments"
DATA_DIR = PROJECT_ROOT / "data"
PROGRESS_FILE = DATA_DIR / "progress.json"
SETTINGS_FILE = DATA_DIR / "settings.json"
