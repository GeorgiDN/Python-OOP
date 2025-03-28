from abc import ABC, abstractmethod


class BaseClimber(ABC):
    REQUIRED_STRENGTH = 0

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

    def can_climb(self):
        return self.strength >= self.REQUIRED_STRENGTH

    @abstractmethod
    def climb(self, peak):
        pass

    def rest(self):
        self.strength += 15

    def __str__(self):
        sorted_peaks = sorted(self.conquered_peaks)
        all_conquered_peaks = ", ".join(sorted_peaks)
        return f"{self.__class__.__name__}: /// Climber name: {self.name} * Left strength: {self.strength:.1f} * Conquered peaks: {all_conquered_peaks} ///"

