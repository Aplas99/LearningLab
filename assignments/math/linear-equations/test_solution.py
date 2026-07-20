import unittest
from solution import taxi_fare

class TaxiFareTests(unittest.TestCase):
    def test_zero_miles_is_base_fare(self):
        self.assertEqual(taxi_fare(0), 3.5)

    def test_typical_trip(self):
        self.assertEqual(taxi_fare(7.25), 19.45)

    def test_rejects_negative_distance(self):
        with self.assertRaises(ValueError):
            taxi_fare(-0.1)

if __name__ == "__main__":
    unittest.main()
