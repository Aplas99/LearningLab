import unittest
from solution import long_trip_total

class LongTripTests(unittest.TestCase):
    def test_filters_and_sums(self):
        self.assertEqual(long_trip_total([3, 12, 8, 20], 10), 32)

    def test_boundary_counts(self):
        self.assertEqual(long_trip_total([5, 5, 4], 5), 10)

    def test_empty_input(self):
        self.assertEqual(long_trip_total([], 10), 0)

if __name__ == "__main__":
    unittest.main()
