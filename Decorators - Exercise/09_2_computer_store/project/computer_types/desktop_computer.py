from project.computer_types.computer import Computer


class DesktopComputer(Computer):
    PROCESSORS = {
        "AMD Ryzen 7 5700G": 500,
        "Intel Core i5-12600K": 600,
        "Apple M1 Max": 1800,
    }
    RAMS = [2, 4, 8, 16, 32, 64, 128]
    RAM_PRICES = {
        2: 100,
        4: 200,
        8: 300,
        16: 400,
        32: 500,
        64: 600,
        128: 700
    }
    TYPE = "desktop computer"

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor: str, ram: int):
        return self.computer_config(processor, ram)
