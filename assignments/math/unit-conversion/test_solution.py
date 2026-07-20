import unittest
from solution import ml_to_cups

class ConversionTests(unittest.TestCase):
    def test_one_cup(self):
        self.assertEqual(ml_to_cups(236.588), 1.0)

    def test_partial_cup(self):
        self.assertEqual(ml_to_cups(500), 2.113)

    def test_rejects_negative_input(self):
        with self.assertRaises(ValueError):
            ml_to_cups(-1)

if __name__ == "__main__":
    unittest.main()
