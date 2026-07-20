import json
import shlex
import tempfile
import unittest
from pathlib import Path

from learnlab.checker import ensure_all_workspaces
from learnlab.ide import IDELaunchError, build_launch_command
from learnlab.lessons import CATEGORIES, LESSONS, LESSONS_BY_ID, lesson_directory
from learnlab.progress import load_progress, record_check, reset_lesson_progress
from learnlab.server import application_state
from learnlab.settings import load_settings, public_ide_settings, save_ide_settings


class CurriculumTests(unittest.TestCase):
    def test_lesson_ids_are_unique_and_categories_exist(self):
        self.assertEqual(len(LESSONS), len(LESSONS_BY_ID))
        self.assertEqual(len(LESSONS), 29)
        category_ids = {category["id"] for category in CATEGORIES}
        self.assertEqual(category_ids, {"python", "oop", "math"})
        self.assertTrue(all(lesson["category"] in category_ids for lesson in LESSONS))

    def test_lesson_order_is_contiguous_in_each_category(self):
        for category in CATEGORIES:
            orders = [
                lesson["order"]
                for lesson in LESSONS
                if lesson["category"] == category["id"]
            ]
            with self.subTest(category=category["id"]):
                self.assertEqual(orders, list(range(1, len(orders) + 1)))

    def test_lessons_have_required_learning_material(self):
        required = {
            "id",
            "title",
            "summary",
            "explanation",
            "example",
            "assignment",
            "starter",
            "tests",
            "assignment_steps",
            "hint",
        }
        for lesson in LESSONS:
            with self.subTest(lesson=lesson["id"]):
                self.assertTrue(required.issubset(lesson))
                self.assertIn("unittest", lesson["tests"])
                self.assertGreaterEqual(len(lesson["assignment_steps"]), 3)
                self.assertTrue(lesson["hint"].strip())
                compile(lesson["starter"], f"{lesson['id']}/solution.py", "exec")
                compile(lesson["tests"], f"{lesson['id']}/test_solution.py", "exec")

    def test_beginner_sequence_does_not_require_untaught_features(self):
        syntax = LESSONS_BY_ID["python/syntax-output"]
        variables = LESSONS_BY_ID["python/variables"]
        functions = LESSONS_BY_ID["python/functions"]
        self.assertNotIn("def ", syntax["starter"])
        self.assertNotIn("def ", variables["starter"])
        self.assertEqual(functions["order"], 3)

        before_exceptions = [
            lesson
            for lesson in LESSONS
            if lesson["category"] == "python" and lesson["order"] < 14
        ]
        for lesson in before_exceptions:
            with self.subTest(lesson=lesson["id"]):
                self.assertNotIn("Raise `ValueError", lesson["assignment"])

    def test_complex_lessons_include_plain_language_explanations(self):
        complex_ids = {
            "python/collections",
            "python/tuples-sets",
            "python/arguments-scope",
            "python/comprehensions",
            "python/modules-json",
            "python/exceptions",
            "python/file-handling",
            "oop/classes",
            "oop/encapsulation",
            "oop/class-methods",
            "oop/inheritance",
            "oop/composition",
            "oop/special-methods",
            "math/numeric-precision",
            "math/linear-equations",
            "math/distance",
            "math/statistics",
            "math/spread",
            "math/linear-regression",
            "math/compound-interest",
        }
        self.assertTrue(all(LESSONS_BY_ID[item]["eli10"] for item in complex_ids))

    def test_public_state_does_not_expose_answers_or_tests(self):
        state = application_state()
        self.assertEqual(state["summary"]["total"], len(LESSONS))
        for lesson in state["lessons"]:
            self.assertNotIn("starter", lesson)
            self.assertNotIn("tests", lesson)
            self.assertTrue(Path(lesson["assignment_path"]).is_absolute())
            command = shlex.split(lesson["cd_command"])
            self.assertEqual(command[0], "cd")
            self.assertEqual(Path(command[1]), Path(lesson["assignment_path"]))
            self.assertEqual(
                lesson["check_command"],
                f"python3 -m learnlab check {lesson['id']}",
            )

    def test_assignment_folders_can_resolve_learnlab_module(self):
        ensure_all_workspaces()
        package_directory = Path(__file__).resolve().parent.parent / "learnlab"
        for lesson in LESSONS:
            with self.subTest(lesson=lesson["id"]):
                module_link = lesson_directory(lesson) / "learnlab"
                self.assertTrue(module_link.is_symlink())
                self.assertEqual(module_link.resolve(), package_directory.resolve())


class ProgressTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.path = Path(self.temp_dir.name) / "progress.json"

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_success_is_persistent_and_attempts_accumulate(self):
        first = record_check("python/variables", False, self.path)
        second = record_check("python/variables", True, self.path)
        third = record_check("python/variables", False, self.path)
        self.assertFalse(first["completed"])
        self.assertTrue(second["completed"])
        self.assertTrue(third["completed"])
        self.assertEqual(third["attempts"], 3)
        self.assertEqual(load_progress(self.path)["lessons"]["python/variables"]["last_result"], "failed")

    def test_reset_removes_only_selected_lesson(self):
        record_check("python/variables", True, self.path)
        record_check("python/loops", True, self.path)
        reset_lesson_progress("python/variables", self.path)
        data = json.loads(self.path.read_text(encoding="utf-8"))
        self.assertNotIn("python/variables", data["lessons"])
        self.assertIn("python/loops", data["lessons"])


class SettingsTests(unittest.TestCase):
    def setUp(self):
        self.temp_dir = tempfile.TemporaryDirectory()
        self.path = Path(self.temp_dir.name) / "settings.json"

    def tearDown(self):
        self.temp_dir.cleanup()

    def test_ide_choice_persists(self):
        save_ide_settings("cursor", path=self.path)
        self.assertEqual(load_settings(self.path)["ide"]["id"], "cursor")
        self.assertEqual(public_ide_settings(self.path)["selected_label"], "Cursor")

    def test_custom_command_persists(self):
        save_ide_settings("custom", "code-insiders --reuse-window", self.path)
        ide = load_settings(self.path)["ide"]
        self.assertEqual(ide["id"], "custom")
        self.assertEqual(ide["custom_command"], "code-insiders --reuse-window")

    def test_invalid_choice_is_rejected(self):
        with self.assertRaises(ValueError):
            save_ide_settings("unknown", path=self.path)
        with self.assertRaises(ValueError):
            save_ide_settings("custom", "", self.path)


class IDECommandTests(unittest.TestCase):
    def setUp(self):
        self.workspace = Path("/tmp/lesson folder")

    def test_uses_installed_cli_launcher(self):
        settings = {"ide": {"id": "vscode", "custom_command": ""}}
        command = build_launch_command(
            self.workspace,
            settings,
            which=lambda name: "/usr/local/bin/code" if name == "code" else None,
            platform="darwin",
        )
        self.assertEqual(command, ["/usr/local/bin/code", str(self.workspace)])

    def test_uses_macos_application_fallback(self):
        settings = {"ide": {"id": "zed", "custom_command": ""}}
        command = build_launch_command(
            self.workspace,
            settings,
            which=lambda name: "/usr/bin/open" if name == "open" else None,
            platform="darwin",
        )
        self.assertEqual(command, ["/usr/bin/open", "-a", "Zed", str(self.workspace)])

    def test_custom_command_is_parsed_without_a_shell(self):
        settings = {
            "ide": {"id": "custom", "custom_command": "my-editor --new-window"}
        }
        command = build_launch_command(
            self.workspace,
            settings,
            which=lambda name: "/opt/bin/my-editor" if name == "my-editor" else None,
        )
        self.assertEqual(
            command,
            ["/opt/bin/my-editor", "--new-window", str(self.workspace)],
        )

    def test_missing_choice_is_actionable(self):
        with self.assertRaisesRegex(IDELaunchError, "Choose an IDE"):
            build_launch_command(self.workspace, {"ide": {}})


if __name__ == "__main__":
    unittest.main()
