from project.peaks.base_peak import BasePeak


class ArcticPeak(BasePeak):
    EXTREME_LEVEL = 3000
    ADVANCED_LEVEL = 2000
    RECOMMENDED_GEAR = ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]

    def __init__(self, name, elevation):
        super().__init__(name, elevation)
