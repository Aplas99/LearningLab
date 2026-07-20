import unittest
from solution import average_from_text

class AverageTextTests(unittest.TestCase):
    def test_numeric_values(self):
        self.assertEqual(average_from_text(["2", "3.5", 6]), 3.83)

    def test_bad_value_message(self):
        with self.assertRaisesRegex(ValueError, "values must be numeric"):
            average_from_text(["2", "nope"])

    def test_empty_message(self):
        with self.assertRaisesRegex(ValueError, "values cannot be empty"):
            average_from_text([])

if __name__ == "__main__":
    unittest.main()
