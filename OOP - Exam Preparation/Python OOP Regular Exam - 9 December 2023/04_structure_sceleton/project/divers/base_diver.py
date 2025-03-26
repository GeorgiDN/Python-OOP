from abc import ABC, abstractmethod

from project.fish.base_fish import BaseFish


class BaseDiver(ABC):
    DECREASE_PERCENT = 0

    def __init__(self, name: str, oxygen_level: float):
        self.name = name
        self.oxygen_level = oxygen_level
        self.catch: list = []
        self.competition_points: float = 0.0
        self.has_health_issue: bool = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Diver name cannot be null or empty!")
        self.__name = value

    @property
    def oxygen_level(self):
        return self.__oxygen_level

    @oxygen_level.setter
    def oxygen_level(self, value):
        if value < 0.0:
            raise ValueError("Cannot create diver with negative oxygen level!")
        self.__oxygen_level = value

    def miss(self, time_to_catch: int):
        decrease_amount = time_to_catch * self.DECREASE_PERCENT
        if self.oxygen_level - decrease_amount >= 0:
            self.oxygen_level = round(self.oxygen_level - decrease_amount, 1)
        else:
            self.oxygen_level = 0

        if self.oxygen_level == 0:
            self.update_health_status()

    @abstractmethod
    def renew_oxy(self):
        pass

    def hit(self, fish: BaseFish):
        if self.oxygen_level >= fish.time_to_catch:
            self.oxygen_level -= fish.time_to_catch
            self.catch.append(fish)
            self.competition_points = round(self.competition_points + fish.points, 1)
        else:
            self.oxygen_level = 0.0

        if self.oxygen_level == 0:
            self.update_health_status()

    def update_health_status(self, ):
        self.has_health_issue = not self.has_health_issue

    def __str__(self, ):
        return (f"{self.__class__.__name__}: [Name: {self.name}, "
                f"Oxygen level left: {self.oxygen_level}, "
                f"Fish caught: {len(self.catch)}, Points earned: {self.competition_points}]")
