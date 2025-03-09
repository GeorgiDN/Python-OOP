from project.waiters.base_waiter import BaseWaiter


class FullTimeWaiter(BaseWaiter):
    SHIFT_TYPE = 'full-time'
    WAGE = 15.0

    def __init__(self, name: str, hours_worked: int):
        super().__init__(name, hours_worked)

    def calculate_earnings(self):
        return self.hours_worked * self.WAGE
