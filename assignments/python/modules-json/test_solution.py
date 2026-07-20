import json
import unittest
from solution import total_from_json

class JsonTotalTests(unittest.TestCase):
    def test_totals_items(self):
        payload = json.dumps({"items": [{"price": 2.5, "quantity": 3}, {"price": 4, "quantity": 1}]})
        self.assertEqual(total_from_json(payload), 11.5)

    def test_empty_items(self):
        self.assertEqual(total_from_json('{"items": []}'), 0)

    def test_invalid_json(self):
        with self.assertRaises(json.JSONDecodeError):
            total_from_json("not json")

if __name__ == "__main__":
    unittest.main()
