import unittest
from solution import Product

class ProductTests(unittest.TestCase):
    def test_reads_and_updates_price(self):
        product = Product("Notebook", 4.5)
        self.assertEqual(product.name, "Notebook")
        self.assertEqual(product.price, 4.5)
        product.price = 6
        self.assertEqual(product.price, 6)

    def test_rejects_negative_initial_price(self):
        with self.assertRaises(ValueError):
            Product("Notebook", -1)

    def test_rejects_negative_update(self):
        product = Product("Notebook", 2)
        with self.assertRaises(ValueError):
            product.price = -0.01

if __name__ == "__main__":
    unittest.main()
