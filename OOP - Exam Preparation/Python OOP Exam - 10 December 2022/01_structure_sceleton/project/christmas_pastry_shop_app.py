from project.booths.open_booth import OpenBooth
from project.booths.private_booth import PrivateBooth
from project.delicacies.gingerbread import Gingerbread
from project.delicacies.stolen import Stolen


class ChristmasPastryShopApp:
    VALID_DELICACIES = {"Gingerbread": Gingerbread, "Stolen": Stolen}
    VALID_BOOTHS = {"Open Booth": OpenBooth, "Private Booth": PrivateBooth}

    def __init__(self):
        self.booths: list = []
        self.delicacies: list = []
        self.income: float = 0.0

    def add_delicacy(self, type_delicacy: str, name: str, price: float):
        delicacy = self._get_delicacy_by_name(self.delicacies, name)
        if delicacy:
            raise Exception(f"{name} already exists!")

        if type_delicacy not in self.VALID_DELICACIES:
            raise Exception(f"{type_delicacy} is not on our delicacy menu!")

        new_delicacy = self.VALID_DELICACIES[type_delicacy](name, price)
        self.delicacies.append(new_delicacy)
        return f"Added delicacy {name} - {type_delicacy} to the pastry shop."

    def add_booth(self, type_booth: str, booth_number: int, capacity: int):
        booth = self._get_booth_by_number(self.booths, booth_number)
        if booth:
            raise Exception(f"Booth number {booth_number} already exists!")

        if type_booth not in self.VALID_BOOTHS:
            raise Exception(f"{type_booth} is not a valid booth!")

        new_booth = self.VALID_BOOTHS[type_booth](booth_number, capacity)
        self.booths.append(new_booth)
        return f"Added booth number {booth_number} in the pastry shop."

    def reserve_booth(self, number_of_people: int):
        for booth in self.booths:
            if not booth.is_reserved and booth.capacity >= number_of_people:
                booth.reserve(number_of_people)
                return f"Booth {booth.booth_number} has been reserved for {number_of_people} people."
        raise Exception(f"No available booth for {number_of_people} people!")

    def order_delicacy(self, booth_number: int, delicacy_name: str):
        booth = self._get_booth_by_number(self.booths, booth_number)
        if not booth:
            raise Exception(f"Could not find booth {booth_number}!")

        delicacy = self._get_delicacy_by_name(self.delicacies, delicacy_name)
        if not delicacy:
            raise Exception(f"No {delicacy_name} in the pastry shop!")

        booth.delicacy_orders.append(delicacy)
        return f"Booth {booth_number} ordered {delicacy_name}."

    def leave_booth(self, booth_number: int):
        booth = self._get_booth_by_number(self.booths, booth_number)
        sum_of_all_orders = sum(d.price for d in booth.delicacy_orders)
        total_price = booth.price_for_reservation + sum_of_all_orders
        self.income += total_price
        booth.delicacy_orders = []
        booth.is_reserved = False
        booth.price_for_reservation = 0.0
        return (f"Booth {booth_number}:\n"
                f"Bill: {total_price:.2f}lv.")

    def get_income(self):
        return f"Income: {self.income:.2f}lv."

    ###
    @staticmethod
    def _get_delicacy_by_name(delicacies_list, name):
        found_delicacy = next((d for d in delicacies_list if d.name == name), None)
        return found_delicacy

    @staticmethod
    def _get_booth_by_number(booths_list, booth_number):
        found_booth = next((b for b in booths_list if b.booth_number == booth_number), None)
        return found_booth





