from project.equipment.base_equipment import BaseEquipment


class ElbowPad(BaseEquipment):
    TYPE = "ElbowPad"
    def __init__(self):
        super().__init__(protection=90, price=25.0)

    def increase_price(self):
        self.price *= 1.1


# k = ElbowPad()
# k.increase_price()
# print(k.price)
