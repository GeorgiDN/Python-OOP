from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    DECREASE_PERCENT = 0.3
    OXYGEN_VALUE = 540

    def __init__(self, name):
        super().__init__(name, self.OXYGEN_VALUE)

    def renew_oxy(self):
        self.oxygen_level = self.OXYGEN_VALUE
