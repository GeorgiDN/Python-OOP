from project.computer_types.desktop_computer import Computer
from project.computer_types.laptop import Laptop
from project.computer_types.desktop_computer import DesktopComputer


class ComputerStoreApp:
    VALID_COMPUTERS = {"Laptop": Laptop, "Desktop Computer": DesktopComputer}

    def __init__(self):
        self.warehouse = []
        self.profits = 0

    def build_computer(self, type_computer: str, manufacturer: str, model: str, processor: str, ram: int):
        if type_computer not in self.VALID_COMPUTERS:
            raise ValueError(f"{type_computer} is not a valid type computer!")

        current_computer = self.VALID_COMPUTERS[type_computer](manufacturer, model)
        message = current_computer.configure_computer(processor, ram)
        self.warehouse.append(current_computer)
        return message

    def sell_computer(self, client_budget: int, wanted_processor: str, wanted_ram: int):
        found_computer = next((c for c in self.warehouse if c.processor == wanted_processor
                               and c.price <= client_budget and c.ram >= wanted_ram), None)

        if found_computer:
            self.warehouse.remove(found_computer)
            self.profits += client_budget - found_computer.price
            return f"{found_computer} sold for {client_budget}$."

        raise Exception("Sorry, we don't have a computer for you.")

