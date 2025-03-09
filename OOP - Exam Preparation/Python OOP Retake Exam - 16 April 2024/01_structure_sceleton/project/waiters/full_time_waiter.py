from project.waiters.base_waiter import BaseWaiter


class FullTimeWaiter(BaseWaiter):
    HOURLY_WAGE = 15.0
    WAITER_TYPE = 'full-time'

    def __init__(self,name: str, hours_worked: int):
        super().__init__(name, hours_worked)

    def get_report(self):
        return self.report_shift()
