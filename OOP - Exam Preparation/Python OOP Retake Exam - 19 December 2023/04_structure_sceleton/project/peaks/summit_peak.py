from project.peaks.base_peak import BasePeak


class SummitPeak(BasePeak):
    EXTREME_LEVEL = 2500
    ADVANCED_LEVEL = 1500
    RECOMMENDED_GEAR = ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]

    def __init__(self, name, elevation):
        super().__init__(name, elevation)
