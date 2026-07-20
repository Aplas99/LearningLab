import unittest
from solution import shared_interests

class SharedInterestTests(unittest.TestCase):
    def test_intersection_is_sorted_tuple(self):
        result = shared_interests(["music", "chess", "music"], ["hiking", "chess", "music"])
        self.assertEqual(result, ("chess", "music"))

    def test_no_overlap(self):
        self.assertEqual(shared_interests(["a"], ["b"]), ())

    def test_accepts_sets(self):
        self.assertEqual(shared_interests({"z", "a"}, {"a"}), ("a",))

if __name__ == "__main__":
    unittest.main()
