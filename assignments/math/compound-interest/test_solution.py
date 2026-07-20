import unittest
from solution import future_value

class FutureValueTests(unittest.TestCase):
    def test_monthly_compounding(self):
        self.assertEqual(future_value(1000, 0.06, 5), 1348.85)

    def test_annual_compounding(self):
        self.assertEqual(future_value(500, 0.1, 2, 1), 605.0)

    def test_zero_years(self):
        self.assertEqual(future_value(750, 0.08, 0), 750.0)

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            future_value(-1, 0.1, 2)
        with self.assertRaises(ValueError):
            future_value(100, 0.1, 2, 0)

if __name__ == "__main__":
    unittest.main()
