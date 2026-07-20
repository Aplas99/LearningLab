import unittest
from solution import Money

class MoneyTests(unittest.TestCase):
    def test_string_format(self):
        self.assertEqual(str(Money(12.5, "USD")), "USD 12.50")

    def test_equality(self):
        self.assertEqual(Money(5, "USD"), Money(5, "USD"))
        self.assertNotEqual(Money(5, "USD"), Money(5, "EUR"))

    def test_addition(self):
        self.assertEqual(Money(2.5, "USD") + Money(4, "USD"), Money(6.5, "USD"))

    def test_currency_mismatch(self):
        with self.assertRaises(ValueError):
            Money(2, "USD") + Money(2, "EUR")

if __name__ == "__main__":
    unittest.main()
