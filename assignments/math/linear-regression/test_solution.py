import unittest
from solution import fit_line

class FitLineTests(unittest.TestCase):
    def test_exact_line(self):
        self.assertEqual(fit_line([(1, 3), (2, 5), (3, 7)]), (2.0, 1.0))

    def test_best_fit_line(self):
        self.assertEqual(fit_line([(1, 2), (2, 3), (3, 5), (4, 4)]), (0.8, 1.5))

    def test_invalid_points(self):
        with self.assertRaises(ValueError):
            fit_line([(1, 2)])
        with self.assertRaises(ValueError):
            fit_line([(2, 1), (2, 4)])

if __name__ == "__main__":
    unittest.main()
