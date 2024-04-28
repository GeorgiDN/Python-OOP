from project.climbers.base_climber import BaseClimber


class ArcticClimber(BaseClimber):
    INITIAL_STRENGTH = 200
    NEEDED_STRENGTH = 100
    STRENGTH_REDUCE = 20
    MULTIPLIERS = {"Advanced": 1.5, "Extreme": 2.0}

    def __init__(self, name):
        super().__init__(name, self.INITIAL_STRENGTH)

    def take_rest(self):
        return self.rest()
