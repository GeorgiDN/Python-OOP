from project.clients.regular_client import RegularClient
from project.clients.vip_client import VIPClient
from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter


class SphereRestaurantApp:
    VALID_WAITERS = {'FullTimeWaiter': FullTimeWaiter, 'HalfTimeWaiter': HalfTimeWaiter}
    VALID_CLIENTS = {'RegularClient': RegularClient, 'VIPClient': VIPClient}

    def __init__(self):
        self.waiters: list = []
        self.clients: list = []

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int):
        if waiter_type not in self.VALID_WAITERS:
            return f"{waiter_type} is not a recognized waiter type."

        waiter = self.get_object_by_name(self.waiters, waiter_name)
        if waiter:
            return f"{waiter_name} is already on the staff."

        new_waiter = self.VALID_WAITERS[waiter_type](waiter_name, hours_worked)
        self.waiters.append(new_waiter)
        return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client(self, client_type: str, client_name: str):
        if client_type not in self.VALID_CLIENTS:
            return f"{client_type} is not a recognized client type."

        client = self.get_object_by_name(self.clients, client_name)
        if client:
            return f"{client_name} is already a client."

        new_client = self.VALID_CLIENTS[client_type](client_name)
        self.clients.append(new_client)
        return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str):
        waiter = self.get_object_by_name(self.waiters, waiter_name)
        if not waiter:
            return f"No waiter found with the name {waiter_name}."

        return waiter.report_shift()

    def process_client_order(self, client_name: str, order_amount: float):
        client = self.get_object_by_name(self.clients, client_name)
        if not client:
            return f"{client_name} is not a registered client."

        points_earned = client.earning_points(order_amount)
        return f"{client_name} earned {points_earned} points from the order."

    def apply_discount_to_client(self, client_name: str):
        client = self.get_object_by_name(self.clients, client_name)

        if not client:
            return f"{client_name} cannot get a discount because this client is not admitted!"

        discount_percentage, remaining_points = client.apply_discount()
        return f"{client_name} received a {discount_percentage}% discount. Remaining points {remaining_points}"

    def generate_report(self):
        result = ["$$ Monthly Report $$"]

        total_earnings = sum(waiter.calculate_earnings() for waiter in self.waiters)
        result.append(f"Total Earnings: ${total_earnings:.2f}")

        total_client_points = sum(client.points for client in self.clients)
        result.append(f"Total Clients Unused Points: {total_client_points}")

        clients_count = len(self.clients)
        result.append(f"Total Clients Count: {clients_count}")

        result.append("** Waiter Details **")

        waiters_earnings = {}
        for waiter in self.waiters:
            if waiter.name not in waiters_earnings:
                waiters_earnings[waiter.name] = waiter.calculate_earnings()

        sorted_waiters = dict(sorted(waiters_earnings.items(), key=lambda w: -w[1]))

        for waiter, earning in sorted_waiters.items():
            result.append(f"Name: {waiter}, Total earnings: ${earning:.2f}")

        return '\n'.join(result)

    @staticmethod
    def get_object_by_name(object_list, name):
        found_object = next((obj for obj in object_list if obj.name == name), None)
        return found_object


# # TEST CODE
# # Create an instance of SphereRestaurantApp
# sphere_restaurant_app = SphereRestaurantApp()
#
# # Hire some waiters
# print(sphere_restaurant_app.hire_waiter("FullTimeWaiter", "John", 40))
# print(sphere_restaurant_app.hire_waiter("HalfTimeWaiter", "Alice", 20))
# print(sphere_restaurant_app.hire_waiter("InvalidWaiter", "JohnDoe", 10))
# print(sphere_restaurant_app.hire_waiter("HalfTimeWaiter", "Charlie", 30))
# print(sphere_restaurant_app.hire_waiter("FullTimeWaiter", "Frank", 50))
# print(sphere_restaurant_app.hire_waiter("HalfTimeWaiter", "Alice", 60))
#
# # Admit some clients
# print(sphere_restaurant_app.admit_client("InvalidClient", "JohnDoe"))
# print(sphere_restaurant_app.admit_client("VIPClient", "Eve"))
# print(sphere_restaurant_app.admit_client("VIPClient", "Lila"))
# print(sphere_restaurant_app.admit_client("RegularClient", "Bob"))
# print(sphere_restaurant_app.admit_client("VIPClient", "Eve"))
# print(sphere_restaurant_app.admit_client("RegularClient", "Oscar"))
#
# # Process shifts
# print(sphere_restaurant_app.process_shifts("John"))
# print(sphere_restaurant_app.process_shifts("Alice"))
# print(sphere_restaurant_app.process_shifts("Emily"))
# print(sphere_restaurant_app.process_shifts("Frank"))
#
# # Process client orders
# print(sphere_restaurant_app.process_client_order("Bob", 100.0))
# print(sphere_restaurant_app.process_client_order("Eve", 500.0))
# print(sphere_restaurant_app.process_client_order("JohnDoe", 250.0))
# print(sphere_restaurant_app.process_client_order("Bob", 750.0))
# print(sphere_restaurant_app.process_client_order("Lila", 550.0))
# print(sphere_restaurant_app.process_client_order("Oscar", 84.0))
#
# # Apply discounts to clients
# print(sphere_restaurant_app.apply_discount_to_client("Lila"))
# print(sphere_restaurant_app.apply_discount_to_client("Eve"))
# print(sphere_restaurant_app.apply_discount_to_client("JohnDoe"))
# print(sphere_restaurant_app.apply_discount_to_client("Oscar"))
# print(sphere_restaurant_app.apply_discount_to_client("Bob"))
#
# # Generate report
# print(sphere_restaurant_app.generate_report())


"""
John is successfully hired as a FullTimeWaiter.
Alice is successfully hired as a HalfTimeWaiter.
InvalidWaiter is not a recognized waiter type.
Charlie is successfully hired as a HalfTimeWaiter.
Frank is successfully hired as a FullTimeWaiter.
Alice is already on the staff.
InvalidClient is not a recognized client type.
Eve is successfully admitted as a VIPClient.
Lila is successfully admitted as a VIPClient.
Bob is successfully admitted as a RegularClient.
Eve is already a client.
Oscar is successfully admitted as a RegularClient.
John worked a full-time shift of 40 hours.
Alice worked a half-time shift of 20 hours.
No waiter found with the name Emily.
Frank worked a full-time shift of 50 hours.
Bob earned 10 points from the order.
Eve earned 100 points from the order.
JohnDoe is not a registered client.
Bob earned 75 points from the order.
Lila earned 110 points from the order.
Oscar earned 8 points from the order.
Lila received a 10% discount. Remaining points 10
Eve received a 10% discount. Remaining points 0
JohnDoe cannot get a discount because this client is not admitted!
Oscar received a 0% discount. Remaining points 8
Bob received a 5% discount. Remaining points 35
$$ Monthly Report $$
Total Earnings: $1950.00
Total Clients Unused Points: 53
Total Clients Count: 4
** Waiter Details **
Name: Frank, Total earnings: $750.00
Name: John, Total earnings: $600.00
Name: Charlie, Total earnings: $360.00
Name: Alice, Total earnings: $240.00
"""
