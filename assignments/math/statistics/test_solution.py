import unittest
from solution import summarize

class SummaryTests(unittest.TestCase):
    def test_odd_count(self):
        self.assertEqual(summarize([9, 2, 4]), {"mean": 5.0, "median": 4})

    def test_even_count(self):
        self.assertEqual(summarize([1, 4, 2, 9]), {"mean": 4.0, "median": 3.0})

    def test_does_not_mutate_input(self):
        values = [3, 1, 2]
        summarize(values)
        self.assertEqual(values, [3, 1, 2])

    def test_empty_input(self):
        with self.assertRaises(ValueError):
            summarize([])

if __name__ == "__main__":
    unittest.main()
