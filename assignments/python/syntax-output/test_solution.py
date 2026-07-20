import subprocess
import sys
import unittest
from pathlib import Path

SOLUTION = Path(__file__).with_name("solution.py")

class StatusMessageTests(unittest.TestCase):
    def test_script_prints_expected_message(self):
        result = subprocess.run(
            [sys.executable, str(SOLUTION)],
            capture_output=True,
            text=True,
            check=False,
        )
        self.assertEqual(result.returncode, 0)
        self.assertEqual(result.stdout.strip(), "Maya: 3/5 lessons complete")

if __name__ == "__main__":
    unittest.main()
