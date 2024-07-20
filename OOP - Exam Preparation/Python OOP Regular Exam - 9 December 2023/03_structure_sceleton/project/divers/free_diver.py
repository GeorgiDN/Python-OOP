from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    INITIAL_OXYGEN_LEVEL = 120
    TYPE = "FreeDiver"
    PERCENT_REDUCE = 0.6

    def __init__(self, name):
        super().__init__(name, oxygen_level=self.INITIAL_OXYGEN_LEVEL)

    def renew_oxy(self):
        self.oxygen_level = self.INITIAL_OXYGEN_LEVEL
