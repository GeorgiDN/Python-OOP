from project.peaks.base_peak import BasePeak


class ArcticPeak(BasePeak):
    EXTREME_ELEVATION = 3000
    ADVANCED_ELEVATION = range(2000, 3001)
    GEAR = ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]

    def __init__(self, name: str, elevation: int):
        super().__init__(name, elevation)

    def get_gear(self):
        return self.get_recommended_gear()
