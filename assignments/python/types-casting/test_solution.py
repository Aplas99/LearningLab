import unittest
from solution import celsius_to_fahrenheit

class TemperatureCastingTests(unittest.TestCase):
    def test_freezing_point(self):
        self.assertEqual(celsius_to_fahrenheit("0"), 32.0)

    def test_decimal_text(self):
        self.assertEqual(celsius_to_fahrenheit("37.5"), 99.5)

    def test_negative_text(self):
        self.assertEqual(celsius_to_fahrenheit("-40"), -40.0)

if __name__ == "__main__":
    unittest.main()
