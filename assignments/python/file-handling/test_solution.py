import tempfile
import unittest
from pathlib import Path
from solution import summarize_log

class LogSummaryTests(unittest.TestCase):
    def test_counts_nonblank_lines_and_errors(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "app.log"
            path.write_text("Started\n\nERROR: disk\nerror: network\nDone\n", encoding="utf-8")
            self.assertEqual(summarize_log(path), {"lines": 4, "errors": 2})

    def test_empty_file(self):
        with tempfile.TemporaryDirectory() as directory:
            path = Path(directory) / "empty.log"
            path.write_text("", encoding="utf-8")
            self.assertEqual(summarize_log(path), {"lines": 0, "errors": 0})

if __name__ == "__main__":
    unittest.main()
