from abc import ABC, abstractmethod


class Computer(ABC):
    PROCESSORS = {}
    RAMS = []
    RAM_PRICES = {}
    TYPE = "computer"

    def __init__(self, manufacturer: str, model: str):
        self.manufacturer = manufacturer
        self.model = model
        self.processor = None
        self.ram = None
        self.price: int = 0

    @property
    def manufacturer(self):
        return self.__manufacturer

    @manufacturer.setter
    def manufacturer(self, value):
        if not value.strip():
            raise ValueError("Manufacturer name cannot be empty.")
        self.__manufacturer = value

    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, value):
        if not value.strip():
            raise ValueError("Model name cannot be empty.")
        self.__model = value

    @abstractmethod
    def configure_computer(self, processor: str, ram: int):
        pass

    def computer_config(self, processor: str, ram: int):
        if processor not in self.PROCESSORS:
            raise ValueError(
                f"{processor} is not compatible with {self.TYPE} {self.manufacturer} {self.model}!")

        if ram not in self.RAMS:
            raise ValueError(
                f"{ram}GB RAM is not compatible with {self.TYPE} {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        price = self.RAM_PRICES[ram] + self.PROCESSORS[processor]
        self.price = price

        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {price}$."
