import unittest
from solution import build_profile

class BuildProfileTests(unittest.TestCase):
    def test_profile_fields(self):
        self.assertEqual(
            build_profile("Ada", ["math", "python"]),
            {"name": "Ada", "first_skill": "math", "skill_count": 2},
        )

    def test_uses_supplied_values(self):
        self.assertEqual(
            build_profile("Lin", ["design"]),
            {"name": "Lin", "first_skill": "design", "skill_count": 1},
        )

if __name__ == "__main__":
    unittest.main()
