import unittest
from solution import make_slug

class MakeSlugTests(unittest.TestCase):
    def test_regular_title(self):
        self.assertEqual(make_slug("Learn Python Today"), "learn-python-today")

    def test_mixed_case_and_space(self):
        self.assertEqual(make_slug("  Clean   DATA  "), "clean-data")

    def test_empty_text(self):
        self.assertEqual(make_slug("   "), "")

if __name__ == "__main__":
    unittest.main()
