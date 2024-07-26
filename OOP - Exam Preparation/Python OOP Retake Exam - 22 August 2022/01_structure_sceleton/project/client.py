import re


class Client:
    def __init__(self, phone_number: str):
        self.phone_number = phone_number
        self.shopping_cart: list = []
        self.bill: float = 0.0
        self.ordered_meals = {}

    @property
    def phone_number(self):
        return self.__phone_number

    @phone_number.setter
    def phone_number(self, value):
        pattern = r"^0\d{9}$"
        if not re.match(pattern, value):
            raise ValueError("Invalid phone number!")
        self.__phone_number = value

