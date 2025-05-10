from project.devices.base_device import BaseDevice


class Smartwatch(BaseDevice):
    def __init__(self, serial_number: str, durability: int, is_functional: bool):
        super().__init__(serial_number, durability, is_functional, "Smartwatch")

    def repair(self):
        if not self.is_functional:
            self.durability = min(100, self.durability * 2)
            self.is_functional = True
