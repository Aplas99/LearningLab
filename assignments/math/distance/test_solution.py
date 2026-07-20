import unittest
from solution import distance_between

class DistanceTests(unittest.TestCase):
    def test_three_four_five_triangle(self):
        self.assertEqual(distance_between((0, 0), (3, 4)), 5.0)

    def test_negative_coordinates(self):
        self.assertEqual(distance_between((-2, 1), (2, -2)), 5.0)

    def test_decimal_result(self):
        self.assertEqual(distance_between((1, 1), (2, 2)), 1.41)

if __name__ == "__main__":
    unittest.main()
