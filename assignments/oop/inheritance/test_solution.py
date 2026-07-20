import unittest
from solution import Employee, HourlyEmployee, SalariedEmployee

class EmployeeTests(unittest.TestCase):
    def test_hourly_employee(self):
        employee = HourlyEmployee("Mina", 30, 20)
        self.assertIsInstance(employee, Employee)
        self.assertEqual(employee.name, "Mina")
        self.assertEqual(employee.weekly_pay(), 600)

    def test_salaried_employee(self):
        employee = SalariedEmployee("Noah", 52000)
        self.assertIsInstance(employee, Employee)
        self.assertEqual(employee.weekly_pay(), 1000)

if __name__ == "__main__":
    unittest.main()
