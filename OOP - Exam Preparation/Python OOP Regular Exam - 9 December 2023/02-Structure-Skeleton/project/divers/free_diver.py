from project.divers.base_diver import BaseDiver


class FreeDiver(BaseDiver):
    INITIAL_OXYGEN_LEVEL = 120
    OXYGEN_DECREASE = 0.6

    def __init__(self, name):
        super().__init__(name, oxygen_level=FreeDiver.INITIAL_OXYGEN_LEVEL)

    def renew_oxy(self):
        self.oxygen_level = FreeDiver.INITIAL_OXYGEN_LEVEL
