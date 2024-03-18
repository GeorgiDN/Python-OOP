class Cup:
    def __init__(self, size: int, quantity: int):
        self.size = size
        self.quantity = quantity

    def fill(self, quantity):
        if self.quantity + quantity <= self.size:
            self.quantity += quantity

    def status(self):
        return self.size - self.quantity


cup = Cup(100, 50)
print(cup.status())
cup.fill(40)
cup.fill(20)
print(cup.status())




# class Cup:
#     def __init__(self, size, quantity):
#         self.size = size
#         self.quantity = quantity

#     def get_free_size(self):
#         return self.size - self.quantity

#     def fill(self, milliliters):
#         if self.get_free_size() < milliliters:
#             return

#         self.quantity += milliliters

#     def status(self):
#         return self.get_free_size()

