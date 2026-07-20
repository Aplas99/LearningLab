import unittest
from solution import TimeSpan

class TimeSpanTests(unittest.TestCase):
    def test_regular_constructor(self):
        self.assertEqual(TimeSpan(45).seconds, 45)

    def test_alternate_constructor(self):
        self.assertEqual(TimeSpan.from_minutes(2.5).seconds, 150)

    def test_validation(self):
        self.assertTrue(TimeSpan.is_valid(0))
        self.assertFalse(TimeSpan.is_valid(-1))
        self.assertFalse(TimeSpan.is_valid("5"))
        with self.assertRaises(ValueError):
            TimeSpan(-2)

if __name__ == "__main__":
    unittest.main()
