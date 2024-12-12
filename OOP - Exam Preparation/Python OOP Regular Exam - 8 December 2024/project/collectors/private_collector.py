from project.collectors.base_collector import BaseCollector


class PrivateCollector(BaseCollector):
    AVAILABLE_MONEY = 25000.0
    AVAILABLE_SPACE = 3000
    INCREASE_AMOUNT = 5000.0

    def __init__(self, name):
        super().__init__(name, self.AVAILABLE_MONEY, self.AVAILABLE_SPACE)

    def increase_money(self):
        self.available_money += self.INCREASE_AMOUNT
