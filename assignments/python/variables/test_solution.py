import unittest
import solution

class OrderTotalTests(unittest.TestCase):
    def test_order_total(self):
        self.assertAlmostEqual(solution.order_total, 24.25)

    def test_total_is_numeric(self):
        self.assertIsInstance(solution.order_total, (int, float))

if __name__ == "__main__":
    unittest.main()
