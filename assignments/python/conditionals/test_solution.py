import unittest
from solution import ticket_price

class TicketPriceTests(unittest.TestCase):
    def test_boundary_ages(self):
        self.assertEqual(ticket_price(12), 8)
        self.assertEqual(ticket_price(13), 12)
        self.assertEqual(ticket_price(64), 12)
        self.assertEqual(ticket_price(65), 9)

if __name__ == "__main__":
    unittest.main()
