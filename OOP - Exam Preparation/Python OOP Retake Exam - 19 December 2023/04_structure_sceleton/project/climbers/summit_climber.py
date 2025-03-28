from project.climbers.base_climber import BaseClimber


class SummitClimber(BaseClimber):
    STRENGTH = 150
    REQUIRED_STRENGTH = 75

    def __init__(self, name: str):
        super().__init__(name, self.STRENGTH)

    def climb(self, peak):
        if peak.difficulty_level == "Extreme":
            self.strength -= (30 * 2.5)
        elif peak.difficulty_level == "Advanced":
            self.strength -= (30 * 1.3)
        self.conquered_peaks.append(peak.name)
