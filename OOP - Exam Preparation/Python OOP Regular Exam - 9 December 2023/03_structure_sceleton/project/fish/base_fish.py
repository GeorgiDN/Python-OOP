from abc import ABC, abstractmethod


class BaseFish(ABC):
    TYPE = "BaseFish"

    def __init__(self, name: str, points: float, time_to_catch: int):
        self.name = name
        self.points = points
        self.time_to_catch = time_to_catch

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Fish name should be determined!")
        self.__name = value

    @property
    def points(self):
        return self.__points

    @points.setter
    def points(self, value):
        if not 1 <= value <= 10:
            raise ValueError("Points should be a value ranging from 1 to 10!")
        self.__points = value

    def fish_details(self):
        return f"{self.TYPE}: {self.name} [Points: {self.points}, Time to Catch: {self.time_to_catch} seconds]"
        # return f"{type(self).__name__}: {self.name} [Points: {self.points}, Time to Catch: {self.time_to_catch} seconds]"

    @abstractmethod
    def show_fish_details(self):
        pass


# f = BaseFish("Fish Name", 10, 10)
# print(f.show_fish_details())
