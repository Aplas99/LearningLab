import unittest
from solution import population_spread

class PopulationSpreadTests(unittest.TestCase):
    def test_known_population(self):
        self.assertEqual(population_spread([2, 4, 6]), {"variance": 2.67, "standard_deviation": 1.63})

    def test_no_spread(self):
        self.assertEqual(population_spread([5, 5, 5]), {"variance": 0.0, "standard_deviation": 0.0})

    def test_empty_population(self):
        with self.assertRaises(ValueError):
            population_spread([])

if __name__ == "__main__":
    unittest.main()
