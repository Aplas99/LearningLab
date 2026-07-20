import unittest
from solution import split_bill

class SplitBillTests(unittest.TestCase):
    def test_distributes_leftover_cents(self):
        self.assertEqual(split_bill("10.00", 3), [3.34, 3.33, 3.33])

    def test_even_split(self):
        self.assertEqual(split_bill(12, 4), [3.0, 3.0, 3.0, 3.0])

    def test_invalid_inputs(self):
        with self.assertRaises(ValueError):
            split_bill(10, 0)
        with self.assertRaises(ValueError):
            split_bill(-1, 2)

if __name__ == "__main__":
    unittest.main()
