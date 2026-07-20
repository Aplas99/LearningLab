import unittest
from solution import passing_names

class PassingNamesTests(unittest.TestCase):
    def test_filters_normalizes_and_sorts(self):
        records = [("Zoe", 70), ("BEN", 69), ("Ana", 94)]
        self.assertEqual(passing_names(records), ["ana", "zoe"])

    def test_empty_records(self):
        self.assertEqual(passing_names([]), [])

if __name__ == "__main__":
    unittest.main()
