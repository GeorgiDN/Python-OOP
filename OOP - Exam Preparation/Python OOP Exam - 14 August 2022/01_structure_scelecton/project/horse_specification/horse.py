from abc import ABC, abstractmethod


class Horse(ABC):
    HORSE_MAX_SPEED: int = 10
    SPEED_INCREMENT: int = 3
    TYPE = "Horse"

    def __init__(self, name: str, speed: int):
        self.name = name
        self.speed = speed
        self.is_taken: bool = False

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if len(value) < 4:
            raise ValueError(f"Horse name {value} is less than 4 symbols!")
        self.__name = value

    @property
    def speed(self):
        return self.__speed

    @speed.setter
    def speed(self, value):
        if self.HORSE_MAX_SPEED < value:
            raise ValueError("Horse speed is too high!")
        self.__speed = value

    @abstractmethod
    def train(self):
        pass

    def train_horse(self):
        if self.speed + self.SPEED_INCREMENT > self.HORSE_MAX_SPEED:
            self.speed = self.HORSE_MAX_SPEED
        else:
            self.speed += self.SPEED_INCREMENT
