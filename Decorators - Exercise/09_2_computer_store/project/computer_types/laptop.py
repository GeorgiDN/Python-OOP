from project.computer_types.computer import Computer


class Laptop(Computer):
    PROCESSORS = {
        "AMD Ryzen 9 5950X": 900,
        "Intel Core i9-11900H": 1050,
        "Apple M1 Pro": 1200,
    }
    RAMS = [2, 4, 8, 16, 32, 64]
    RAM_PRICES = {
        2: 100,
        4: 200,
        8: 300,
        16: 400,
        32: 500,
        64: 600,
    }
    TYPE = 'laptop'

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor: str, ram: int):
        return self.computer_config(processor, ram)
