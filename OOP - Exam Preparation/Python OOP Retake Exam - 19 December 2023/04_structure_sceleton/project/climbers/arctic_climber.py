from project.climbers.base_climber import BaseClimber


class ArcticClimber(BaseClimber):
    STRENGTH = 200
    REQUIRED_STRENGTH = 100

    def __init__(self, name: str):
        super().__init__(name, self.STRENGTH)

    def climb(self, peak):
        if peak.difficulty_level == "Extreme":
            self.strength -= (20 * 2)
        elif peak.difficulty_level == "Advanced":
            self.strength -= (20 * 1.5)
        self.conquered_peaks.append(peak.name)
