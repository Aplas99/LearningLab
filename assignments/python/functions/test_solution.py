import unittest
from solution import rectangle_perimeter

class RectanglePerimeterTests(unittest.TestCase):
    def test_typical_rectangle(self):
        self.assertEqual(rectangle_perimeter(8, 3), 22)

    def test_square(self):
        self.assertEqual(rectangle_perimeter(5, 5), 20)

    def test_uses_supplied_arguments(self):
        self.assertEqual(rectangle_perimeter(2.5, 4), 13)

if __name__ == "__main__":
    unittest.main()
