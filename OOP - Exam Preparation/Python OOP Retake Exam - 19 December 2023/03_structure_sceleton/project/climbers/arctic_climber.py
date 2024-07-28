from project.climbers.base_climber import BaseClimber
from project.peaks.base_peak import BasePeak


class ArcticClimber(BaseClimber):
    def __init__(self, name: str):
        super().__init__(name, 200)

    def can_climb(self):
        return self.strength >= 100

    def climb(self, peak: BasePeak):
        if peak.difficulty_level == "Extreme":
            self.strength -= (20 * 2)
        elif peak.difficulty_level == "Advanced":
            self.strength -= (20 * 1.5)
        self.conquered_peaks.append(peak.name)


# b = ArcticPeak("Peak", 3001)
# print(b.difficulty_level)
# print(b.get_recommended_gear())
#
# s = ArcticClimber("Articc")
# print(s.can_climb())
# s.climb(b)
# print(s.strength)
# print(s.__str__())

