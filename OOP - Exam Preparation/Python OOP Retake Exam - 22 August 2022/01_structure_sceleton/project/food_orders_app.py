from project.client import Client
from project.meals.main_dish import MainDish
from project.meals.meal import Meal
from project.meals.starter import Starter
from project.meals.dessert import Dessert


class FoodOrdersApp:
    ALLOWED_MEALS = ["Starter", "MainDish", "Dessert"]
    RECEIPT_ID = 1

    def __init__(self):
        self.menu: list = []
        self.clients_list: list = []

    def register_client(self, client_phone_number: str):
        client = self._get_client_by_phone_number(self.clients_list, client_phone_number)
        if client:
            raise Exception(f"The client has already been registered!")

        new_client = Client(client_phone_number)
        self.clients_list.append(new_client)
        return f"Client {client_phone_number} registered successfully."

    def add_meals_to_menu(self, *meals: Meal):
        for meal in meals:
            if meal.__class__.__name__ in self.ALLOWED_MEALS:
                self.menu.append(meal)

    def show_menu(self):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        return "\n".join(meal.details() for meal in self.menu)

    def add_meals_to_shopping_cart(self, client_phone_number: str, **meal_names_and_quantities):
        if len(self.menu) < 5:
            raise Exception("The menu is not ready!")

        client = self._get_client_by_phone_number(self.clients_list, client_phone_number)
        if not client:
            client = Client(client_phone_number)
            self.clients_list.append(client)

        menu_names = [m.name for m in self.menu]

        # validation
        for meal_name, qty in meal_names_and_quantities.items():
            if meal_name not in menu_names:
                raise Exception(f"{meal_name} is not on the menu!")

            meal = self._get_meal_by_name(self.menu, meal_name)
            if meal.quantity < qty:
                raise Exception(f"Not enough quantity of {meal.__class__.__name__}: {meal_name}!")

        for meal_name, qty in meal_names_and_quantities.items():
            meal = self._get_meal_by_name(self.menu, meal_name)
            if meal_name not in client.ordered_meals:
                client.ordered_meals[meal_name] = 0
            client.ordered_meals[meal_name] += qty
            client.shopping_cart.append(meal)
            client.bill += meal.price * qty
            meal.quantity -= qty

        meal_names = ", ".join(m.name for m in client.shopping_cart)

        return f"Client {client_phone_number} successfully ordered {meal_names} for {client.bill:.2f}lv."

    def cancel_order(self, client_phone_number: str):
        client = self._get_client_by_phone_number(self.clients_list, client_phone_number)

        if not client.shopping_cart:
            raise Exception(f"There are no ordered meals!")

        for ordered_meal, quantity in client.ordered_meals.items():
            for menu_meal in self.menu:
                if ordered_meal == menu_meal.name:
                    menu_meal.quantity += quantity

        client.ordered_meals = {}
        client.shopping_cart = []
        client.bill = 0.0

        return f"Client {client.phone_number} successfully canceled his order."

    def finish_order(self, client_phone_number: str):
        client = self._get_client_by_phone_number(self.clients_list, client_phone_number)
        if not client.shopping_cart:
            raise Exception(f"There are no ordered meals!")

        message = f"Receipt #{self.RECEIPT_ID} with total amount of {client.bill:.2f} was successfully paid for {client_phone_number}."
        client.ordered_meals = {}
        client.shopping_cart = []
        client.bill = 0
        self.RECEIPT_ID += 1
        return message

    def __str__(self):
        return f"Food Orders App has {len(self.menu)} meals on the menu and {len(self.clients_list)} clients."

    ###
    @staticmethod
    def _get_client_by_phone_number(clients_list, phone_num):
        found_client = next((c for c in clients_list if c.phone_number == phone_num), None)
        return found_client

    @staticmethod
    def _get_meal_by_name(menu_list, meal_name):
        found_meal = next((m for m in menu_list if m.name == meal_name), None)
        return found_meal



# food_orders_app = FoodOrdersApp()
# print(food_orders_app.register_client("0899999999"))
# french_toast = Starter("French toast", 6.50, 5)
# hummus_and_avocado_sandwich = Starter("Hummus and Avocado Sandwich", 7.90)
# tortilla_with_beef_and_pork = MainDish("Tortilla with Beef and Pork", 12.50, 12)
# risotto_with_wild_mushrooms = MainDish("Risotto with Wild Mushrooms", 15)
# chocolate_cake_with_mascarpone = Dessert("Chocolate Cake with Mascarpone", 4.60, 17)
# chocolate_and_violets = Dessert("Chocolate and Violets", 5.20)
# print(food_orders_app.add_meals_to_menu(
#     french_toast, hummus_and_avocado_sandwich,
#     tortilla_with_beef_and_pork,
#     risotto_with_wild_mushrooms,
#     chocolate_cake_with_mascarpone,
#     chocolate_and_violets))
# print(food_orders_app.show_menu())
# food = {"Hummus and Avocado Sandwich": 5,
#         "Risotto with Wild Mushrooms": 1,
#         "Chocolate and Violets": 4}
# print(food_orders_app.add_meals_to_shopping_cart('0899999999', **food))
# additional_food = {"Risotto with Wild Mushrooms": 2,
#                    "Tortilla with Beef and Pork": 2}
# print(food_orders_app.add_meals_to_shopping_cart('0899999999', **additional_food))
# # print(food_orders_app.cancel_order('0899999999'))
#
# print(food_orders_app.finish_order("0899999999"))
# print(food_orders_app)





"""
Client 0899999999 registered successfully.
None
Starter French toast: 6.50lv/piece
Starter Hummus and Avocado Sandwich: 7.90lv/piece
Main Dish Tortilla with Beef and Pork: 12.50lv/piece
Main Dish Risotto with Wild Mushrooms: 15.00lv/piece
Dessert Chocolate Cake with Mascarpone: 4.60lv/piece
Dessert Chocolate and Violets: 5.20lv/piece
Client 0899999999 successfully ordered Hummus and Avocado Sandwich, Risotto with Wild Mushrooms, Chocolate and Violets for 75.30lv.
Client 0899999999 successfully ordered Hummus and Avocado Sandwich, Risotto with Wild Mushrooms, Chocolate and Violets, Risotto with Wild Mushrooms, Tortilla with Beef and Pork for 130.30lv.
Receipt #1 with total amount of 130.30 was successfully paid for 0899999999.
Food Orders App has 6 meals on the menu and 1 clients.
"""
