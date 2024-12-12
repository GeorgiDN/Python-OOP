from project.collectors.base_collector import BaseCollector


class Museum(BaseCollector):
    AVAILABLE_MONEY = 15000.0
    AVAILABLE_SPACE = 2000
    INCREASE_AMOUNT = 1000.0

    def __init__(self, name):
        super().__init__(name, self.AVAILABLE_MONEY, self.AVAILABLE_SPACE)

    def increase_money(self):
        self.available_money += self.INCREASE_AMOUNT
