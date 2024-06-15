from project.divers.base_diver import BaseDiver


class ScubaDiver(BaseDiver):
    INITIAL_OXYGEN_LEVEL = 540
    OXYGEN_DECREASE = 0.3

    def __init__(self, name):
        super().__init__(name, oxygen_level=ScubaDiver.INITIAL_OXYGEN_LEVEL)

    def renew_oxy(self):
        self.oxygen_level = ScubaDiver.INITIAL_OXYGEN_LEVEL

