from project.products.base_product import BaseProduct


class HobbyHorse(BaseProduct):
    MATERIAL = "Wood/Plastic"
    SUB_TYPE = "Toys"
    DISCOUNT = 0.8

    def __init__(self, model: str, price: float):
        super().__init__(model, price, material=self.MATERIAL, sub_type=self.SUB_TYPE)

    def discount(self):
        self.price *= self.DISCOUNT


# h = HobbyHorse("Chair1", 10)
# h.discount()
# print(h.price)
# print(h.material)
# print(h.sub_type)
