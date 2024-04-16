from project.computer_types.computer import Computer

class DesktopComputer(Computer):
    VALID_COMPUTERS = ["Laptop", "Desktop Computer"]
    VALID_PROCESSORS_FOR_DESKTOP_COMPUTERS = {
        "AMD Ryzen 7 5700G": 500,
        "Intel Core i5-12600K": 600,
        "Apple M1 Max": 1800
    }
    VALID_RAMS = [2, 4, 8, 16, 32, 64, 128]
    PRICE_PER_RAM = {2: 100, 4: 200, 8: 300, 16: 400, 32: 500, 64: 600, 128: 700}

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor: str, ram: int):
        if processor not in self.VALID_PROCESSORS_FOR_DESKTOP_COMPUTERS:
            raise ValueError(f"{processor} is not compatible with desktop computer {self.manufacturer} {self.model}!")

        if ram not in self.VALID_RAMS:
            raise ValueError(f"{ram}GB RAM is not compatible with desktop computer {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        current_ram_price = self.PRICE_PER_RAM[ram] + self.VALID_PROCESSORS_FOR_DESKTOP_COMPUTERS[processor]
        self.price += current_ram_price

        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {current_ram_price}$."


