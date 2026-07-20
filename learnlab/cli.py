import argparse
import sys

from .checker import ensure_all_workspaces, reset_lesson, run_lesson_tests
from .lessons import LESSONS_BY_ID
from .server import serve


def _lesson_id(value: str) -> str:
    if value not in LESSONS_BY_ID:
        choices = ", ".join(LESSONS_BY_ID)
        raise argparse.ArgumentTypeError(f"unknown lesson {value!r}. Choose one of: {choices}")
    return value


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="python3 -m learnlab",
        description="Run the offline LearnLab server or check an assignment.",
    )
    commands = parser.add_subparsers(dest="command")

    serve_parser = commands.add_parser("serve", help="start the local learning app")
    serve_parser.add_argument("--host", default="127.0.0.1")
    serve_parser.add_argument("--port", type=int, default=8000)

    check_parser = commands.add_parser("check", help="run one lesson's tests")
    check_parser.add_argument("lesson_id", type=_lesson_id)

    reset_parser = commands.add_parser("reset", help="restore a lesson to its starter state")
    reset_parser.add_argument("lesson_id", type=_lesson_id)

    commands.add_parser("setup", help="create any missing assignment workspaces")
    commands.add_parser("list", help="list lesson IDs")
    return parser


def main(argv=None) -> int:
    parser = build_parser()
    args = parser.parse_args(argv)
    if args.command in {None, "serve"}:
        serve(
            getattr(args, "host", "127.0.0.1"),
            getattr(args, "port", 8000),
        )
        return 0
    if args.command == "check":
        result = run_lesson_tests(args.lesson_id)
        print(result.output)
        print("\nPASS: lesson complete" if result.passed else "\nFAIL: keep working")
        return 0 if result.passed else 1
    if args.command == "reset":
        reset_lesson(args.lesson_id)
        print(f"Reset {args.lesson_id} to its starter state.")
        return 0
    if args.command == "setup":
        ensure_all_workspaces()
        print("Assignment workspaces are ready.")
        return 0
    if args.command == "list":
        for lesson_id in LESSONS_BY_ID:
            print(lesson_id)
        return 0
    parser.print_help()
    return 2


if __name__ == "__main__":
    sys.exit(main())
