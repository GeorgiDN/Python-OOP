from abc import ABC, abstractmethod


class BaseService(ABC):
    TYPE_SERVICE = "Base"

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.robots: list = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Service name cannot be empty!")
        self.__name = value
    
    @property
    def capacity(self):
        return self.__capacity
    
    @capacity.setter
    def capacity(self, value):
        if value <= 0:
            raise ValueError("Service capacity cannot be less than or equal to 0!")
        self.__capacity = value

    @abstractmethod
    def take_details(self):
        pass

    def details(self):
        result = f"{self.name} {self.TYPE_SERVICE} Service:\n"
        robots = " ".join(r.name for r in self.robots) if self.robots else "none"
        result += f"Robots: {robots}"
        return result


