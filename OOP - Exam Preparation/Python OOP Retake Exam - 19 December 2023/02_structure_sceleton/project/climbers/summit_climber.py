from project.climbers.base_climber import BaseClimber


class SummitClimber(BaseClimber):
    INITIAL_STRENGTH = 150
    NEEDED_STRENGTH = 75
    STRENGTH_REDUCE = 30
    MULTIPLIERS = {"Advanced": 1.3, "Extreme": 2.5}

    def __init__(self, name):
        super().__init__(name, self.INITIAL_STRENGTH)

    def take_rest(self):
        return self.rest()
