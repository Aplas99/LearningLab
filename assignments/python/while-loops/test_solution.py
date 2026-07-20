import unittest
from solution import months_to_goal

class MonthsToGoalTests(unittest.TestCase):
    def test_counts_months(self):
        self.assertEqual(months_to_goal(100, 30, 205), 4)

    def test_already_at_goal(self):
        self.assertEqual(months_to_goal(250, 20, 200), 0)

if __name__ == "__main__":
    unittest.main()
