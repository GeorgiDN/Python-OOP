from abc import ABC, abstractmethod
from project.peaks.base_peak import BasePeak
# from project.peaks.arctic_peak import ArcticPeak


class BaseClimber(ABC):
    NEEDED_STRENGTH = ''
    STRENGTH_REDUCE = ''
    MULTIPLIERS = {"Advanced": 1, "Extreme": 1}

    def __init__(self, name: str, strength: float):
        self.name = name
        self.strength = strength
        self.conquered_peaks: list = []
        self.is_prepared: bool = True

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Climber name cannot be null or empty!")
        self.__name = value

    @property
    def strength(self):
        return self.__strength

    @strength.setter
    def strength(self, value):
        if value <= 0:
            raise ValueError("A climber cannot have negative strength or strength equal to 0!")
        self.__strength = value

    @abstractmethod
    def take_rest(self):
        pass

    def can_climb(self):
        return self.__strength >= self.NEEDED_STRENGTH

    def climb(self, peak: BasePeak):
        self.__strength -= (self.STRENGTH_REDUCE * self.MULTIPLIERS[peak.difficulty_level])
        self.conquered_peaks.append(peak.name)

    def rest(self):
        self.__strength += 15

    def __str__(self):
        sorted_conquered_peaks = sorted(self.conquered_peaks)
        conquered_peaks = ', '.join(sorted_conquered_peaks)
        return f"{type(self).__name__}: /// Climber name: {self.name} * Left strength: {round(self.__strength, 1)} * Conquered peaks: {conquered_peaks} ///"
