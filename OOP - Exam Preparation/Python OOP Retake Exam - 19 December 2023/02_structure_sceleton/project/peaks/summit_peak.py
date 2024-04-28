from project.peaks.base_peak import BasePeak


class SummitPeak(BasePeak):
    EXTREME_ELEVATION = 2500
    ADVANCED_ELEVATION = range(1500, 2501)
    GEAR = ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]

    def __init__(self, name: str, elevation: int):
        super().__init__(name, elevation)

    def get_gear(self):
        return self.get_recommended_gear()
