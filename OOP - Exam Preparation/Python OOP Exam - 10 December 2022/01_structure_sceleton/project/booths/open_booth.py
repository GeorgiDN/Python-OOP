from project.booths.booth import Booth


class OpenBooth(Booth):
    PRICE_PER_PERSON = 2.50
    TYPE = "OpenBooth"

    def __init__(self, booth_number: int,  capacity: int):
        super().__init__(booth_number, capacity)

    def reserve(self, number_of_people: int):
        self.price_for_reservation = self.PRICE_PER_PERSON * number_of_people
        self.is_reserved = True


# o = OpenBooth(5, 5)
# o.reserve(3)
# print(o.price_for_reservation)
# print(o.is_reserved)
