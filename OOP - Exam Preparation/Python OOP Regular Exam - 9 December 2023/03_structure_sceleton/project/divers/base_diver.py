from abc import ABC, abstractmethod

from project.fish.base_fish import BaseFish
# from project.fish.deep_sea_fish import DeepSeaFish


class BaseDiver(ABC):
    INITIAL_OXYGEN_LEVEL = 120  # for test
    TYPE = "BaseDiver"
    PERCENT_REDUCE = 0.6

    def __init__(self, name: str, oxygen_level: float):
        self.name = name
        self.oxygen_level = oxygen_level
        self.catch: list = []
        self.competition_points: float = 0.0 # TODO round first digit
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
        if value < 0:
            raise ValueError("Cannot create diver with negative oxygen level!")
        self.__oxygen_level = value

    def miss(self, time_to_catch: int):
        if self.oxygen_level - (time_to_catch * self.PERCENT_REDUCE) >= 0:
            self.oxygen_level -= (time_to_catch * self.PERCENT_REDUCE)
            self.oxygen_level = int(self.oxygen_level)
        else:
            self.oxygen_level = 0.0

    @abstractmethod
    def renew_oxy(self):
        pass

    def hit(self, fish: BaseFish):
        if self.oxygen_level - fish.time_to_catch >= 0:
            self.oxygen_level -= fish.time_to_catch
            self.catch.append(fish)
            self.competition_points = round(self.competition_points + fish.points, 1)
        else:
            self.oxygen_level = 0.0

    def update_health_status(self):
        self.has_health_issue = not self.has_health_issue

    def __str__(self):
        return (f"{self.TYPE}: [Name: {self.name}, Oxygen level left: {self.oxygen_level}, "
                f"Fish caught: {len(self.catch)}, Points earned: {self.competition_points}]")


# f = DeepSeaFish("Fish Name", 9)  # 180time to catch
# d = BaseDiver("Diver", 190)
# print(d.miss(100))
# print(d.miss(10000))
# print(d.renew_oxy())
 # print(d.hit(f))
# print(d.oxygen_level)
# print(d.competition_points)
# print(d.update_health_status())
# print(d.has_health_issue)
# print(d)
