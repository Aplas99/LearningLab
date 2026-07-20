class Employee:
    def __init__(self, name):
        self.name = name

    def weekly_pay(self):
        raise NotImplementedError


class HourlyEmployee(Employee):
    pass


class SalariedEmployee(Employee):
    pass
