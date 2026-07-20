import unittest
from solution import invoice_total

class InvoiceTotalTests(unittest.TestCase):
    def test_multiple_prices(self):
        self.assertEqual(invoice_total(20, 30, tax_rate=0.1, discount=0.2), 44.0)

    def test_defaults(self):
        self.assertEqual(invoice_total(4.25, 5.75), 10.0)

if __name__ == "__main__":
    unittest.main()
