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
        sorted_ships = sorted(self.ships, key=lambda ship: (-ship.hit_strength, ship.name))
        return sorted_ships

    @abstractmethod
    def zone_info(self):
        pass
