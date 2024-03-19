class PizzaDelivery:
    def __init__(self, name: str, price: float, ingredients: dict):
        self.name = name
        self.price = price
        self.ingredients = ingredients
        self.ordered = False

    def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
        if not self.ordered:
            if ingredient not in self.ingredients:
                self.ingredients[ingredient] = 0
            self.ingredients[ingredient] += quantity
            self.price += price_per_quantity * quantity
        return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):
        if not self.ordered:
            if ingredient not in self.ingredients:
                return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
            if quantity > self.ingredients[ingredient]:
                return f"Please check again the desired quantity of {ingredient}!"
            self.ingredients[ingredient] -= quantity
            self.price -= price_per_quantity * quantity
        return f"Pizza {self.name} already prepared, and we can't make any changes!"

    def make_order(self):
        if not self.ordered:
            self.ordered = True
            ingredients = []
            for ingredient_name, qty in self.ingredients.items():
                ingredients.append(f"{ingredient_name}: {qty}")

            return f"You've ordered pizza {self.name} prepared with {', '.join(map(str, ingredients))} and the price will be {self.price}lv."


margarita = PizzaDelivery('Margarita', 11, {'cheese': 2, 'tomatoes': 1})
margarita.add_extra('mozzarella', 1, 0.5)
margarita.add_extra('cheese', 1, 1)
margarita.remove_ingredient('cheese', 1, 1)
print(margarita.remove_ingredient('bacon', 1, 2.5))
print(margarita.remove_ingredient('tomatoes', 2, 0.5))
margarita.remove_ingredient('cheese', 2, 1)
print(margarita.make_order())
print(margarita.add_extra('cheese', 1, 1))





# class PizzaDelivery:
#     def __init__(self, name: str, price: float, ingredients: dict):
#         self.name = name
#         self.price = price
#         self.ingredients = ingredients
#         self.ordered = False
# 
#     def add_extra(self, ingredient: str, quantity: int, price_per_quantity: float):
#         if self.ordered:
#             return f"Pizza {self.name} already prepared, and we can't make any changes!"
# 
#         if ingredient not in self.ingredients:
#             self.ingredients[ingredient] = 0
#         self.ingredients[ingredient] += quantity
#         total_cost = price_per_quantity * quantity
#         self.price += total_cost
# 
#     def remove_ingredient(self, ingredient: str, quantity: int, price_per_quantity: float):
#         if self.ordered:
#             return f"Pizza {self.name} already prepared, and we can't make any changes!"
#         if ingredient not in self.ingredients:
#             return f"Wrong ingredient selected! We do not use {ingredient} in {self.name}!"
#         elif ingredient in self.ingredients:
#             if quantity > self.ingredients[ingredient]:
#                 return f"Please check again the desired quantity of {ingredient}!"
#             self.ingredients[ingredient] -= quantity
#             total_cost = price_per_quantity * quantity
#             self.price -= total_cost
# 
#     def make_order(self):
#         self.ordered = True
#         ingredients = []
#         for ingr, quant in self.ingredients.items():
#             ingredients.append(f"{ingr}: {quant}")
# 
#         return f"You've ordered pizza {self.name} prepared with {', '.join(ingredients)} " \
#                f"and the price will be {self.price}lv."
