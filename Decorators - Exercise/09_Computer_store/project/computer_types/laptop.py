from project.computer_types.computer import Computer


class Laptop(Computer):
    VALID_COMPUTERS = ["Laptop", "Desktop Computer"]
    VALID_PROCESSORS_FOR_LAPTOPS = {
        "AMD Ryzen 9 5950X": 900,
        "Intel Core i9-11900H": 1050,
        "Apple M1 Pro": 1200
    }
    VALID_RAMS = [2, 4, 8, 16, 32, 64]
    PRICE_PER_RAM = {2: 100, 4: 200, 8: 300, 16: 400, 32: 500, 64: 600}

    def __init__(self, manufacturer: str, model: str):
        super().__init__(manufacturer, model)

    def configure_computer(self, processor: str, ram: int):
        if processor not in Laptop.VALID_PROCESSORS_FOR_LAPTOPS:
            raise ValueError(f"{processor} is not compatible with laptop {self.manufacturer} {self.model}!")
        if ram not in Laptop.VALID_RAMS:
            raise ValueError(f"{ram}GB RAM is not compatible with laptop {self.manufacturer} {self.model}!")

        self.processor = processor
        self.ram = ram
        current_ram_price = Laptop.VALID_PROCESSORS_FOR_LAPTOPS[processor] + Laptop.PRICE_PER_RAM[ram]
        self.price += current_ram_price

        return f"Created {self.manufacturer} {self.model} with {processor} and {ram}GB RAM for {current_ram_price}$."