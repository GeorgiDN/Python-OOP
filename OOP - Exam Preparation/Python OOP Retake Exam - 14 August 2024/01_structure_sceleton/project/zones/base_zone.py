from abc import ABC, abstractmethod


class BaseZone(ABC):
    def __init__(self, code: str, volume: int):
        self.code = code
        self.volume = volume
        self.ships: list = []

    @property
    def code(self):
        return self.__code

    @code.setter
    def code(self, value):
        if not value.isdigit():
            raise ValueError("Zone code must contain digits only!")
        self.__code = value

    def get_ships(self):
        ordered_ships = sorted(self.ships, key=lambda s: (-s.hit_strength, s.name))
        return ordered_ships

    @abstractmethod
    def zone_info(self):
        pass
