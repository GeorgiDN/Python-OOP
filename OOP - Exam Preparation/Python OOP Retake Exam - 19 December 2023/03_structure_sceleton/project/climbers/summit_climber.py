from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class SummitClimber(BaseClimber):
    def __init__(self, name: str):
        super().__init__(name, 150)

    def can_climb(self):
        return self.strength >= 75

    def climb(self, peak: BasePeak):
        if peak.difficulty_level == "Extreme":
            self.strength -= (30 * 2.5)
        elif peak.difficulty_level == "Advanced":
            self.strength -= (30 * 1.3)
        self.conquered_peaks.append(peak.name)


# b = SummitPeak("Peak", 2501)
# print(b.difficulty_level)
# print(b.get_recommended_gear())
#
# s = SummitClimber("Summit")
# print(s.can_climb())
# s.climb(b)
# print(s.strength)
# print(s.__str__())
