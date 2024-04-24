from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    STRENGTH = 200
    MINIMUM_STRENGTH_TO_CLIMB = 100

    def __init__(self, name: str):
        super().__init__(name, strength=self.STRENGTH)

    def can_climb(self):
        return self.strength >= self.MINIMUM_STRENGTH_TO_CLIMB

    def climb(self, peak: BasePeak):
        if peak.difficulty_level == "Extreme":
            self.strength -= (20.0 * 2.0)
        else:
            self.strength -= (20.0 * 1.5)
        self.conquered_peaks.append(peak.name)
