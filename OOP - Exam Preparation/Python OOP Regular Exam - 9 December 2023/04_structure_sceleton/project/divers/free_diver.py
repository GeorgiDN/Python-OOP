from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    DECREASE_PERCENT = 0.6
    OXYGEN_VALUE = 120

    def __init__(self, name):
        super().__init__(name, self.OXYGEN_VALUE)

    def renew_oxy(self):
        self.oxygen_level = self.OXYGEN_VALUE
