import unittest
from solution import BankAccount

class BankAccountTests(unittest.TestCase):
    def test_initial_state(self):
        account = BankAccount("Ada", 25)
        self.assertEqual(account.owner, "Ada")
        self.assertEqual(account.balance, 25)

    def test_deposit(self):
        account = BankAccount("Lin")
        self.assertEqual(account.deposit(10), 10)
        self.assertEqual(account.deposit(2.5), 12.5)

    def test_rejects_invalid_deposit(self):
        with self.assertRaises(ValueError):
            BankAccount("Sam").deposit(0)

if __name__ == "__main__":
    unittest.main()
