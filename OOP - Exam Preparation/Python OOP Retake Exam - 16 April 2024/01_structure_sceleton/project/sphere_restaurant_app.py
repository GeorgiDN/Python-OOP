from project.waiters.full_time_waiter import FullTimeWaiter
from project.waiters.half_time_waiter import HalfTimeWaiter
from project.clients.vip_client import VIPClient
from project.clients.regular_client import RegularClient


class SphereRestaurantApp:
    WAITER_TYPES = {"FullTimeWaiter": FullTimeWaiter, "HalfTimeWaiter": HalfTimeWaiter}
    CLIENT_TYPES = {"RegularClient": RegularClient, "VIPClient": VIPClient}

    def __init__(self):
        self.waiters: list = []
        self.clients: list = []

    def hire_waiter(self, waiter_type: str, waiter_name: str, hours_worked: int):
        if waiter_type not in self.WAITER_TYPES:
            return f"{waiter_type} is not a recognized waiter type."

        waiter = self._get_waiter(self.waiters, waiter_name)
        if waiter:
            return f"{waiter_name} is already on the staff."

        new_waiter = self.WAITER_TYPES[waiter_type](waiter_name, hours_worked)
        self.waiters.append(new_waiter)
        return f"{waiter_name} is successfully hired as a {waiter_type}."

    def admit_client(self, client_type: str, client_name: str):
        if client_type not in self.CLIENT_TYPES:
            return f"{client_type} is not a recognized client type."

        client = self._get_client(self.clients, client_name)
        if client:
            return f"{client_name} is already a client."

        new_client = self.CLIENT_TYPES[client_type](client_name)
        self.clients.append(new_client)
        return f"{client_name} is successfully admitted as a {client_type}."

    def process_shifts(self, waiter_name: str):
        waiter = self._get_waiter(self.waiters, waiter_name)
        if not waiter:
            return f"No waiter found with the name {waiter_name}."

        return waiter.get_report()

    def process_client_order(self, client_name: str, order_amount: float):
        client = self._get_client(self.clients, client_name)
        if not client:
            return f"{client_name} is not a registered client."

        points_earned = client.earning_points(order_amount)
        return f"{client_name} earned {points_earned} points from the order."

    def apply_discount_to_client(self, client_name: str):
        client = self._get_client(self.clients, client_name)
        if not client:
            return f"{client_name} cannot get a discount because this client is not admitted!"
        discount, remaining_points = client.apply_discount()
        return f"{client_name} received a {discount}% discount. Remaining points {remaining_points}"

    def generate_report(self):
        result = "$$ Monthly Report $$\n"
        sorted_waiters = sorted(self.waiters, key=lambda w: (-w.calculate_earnings()))
        total_earnings = sum(w.calculate_earnings() for w in self.waiters)
        total_client_points = sum(c.points for c in self.clients)
        total_clients_count = len(self.clients)

        result += f"Total Earnings: ${total_earnings:.2f}\n"
        result += f"Total Clients Unused Points: {total_client_points}\n"
        result += f"Total Clients Count: {total_clients_count}\n"

        result += "** Waiter Details **\n"

        for current_waiter in sorted_waiters:
            result += current_waiter.__str__() + '\n'

        return result.strip()

    ## Helper methods
    @staticmethod
    def _get_waiter(lst, curr_name):
        found_waiter = next((w for w in lst if w.name == curr_name), None)
        return found_waiter

    @staticmethod
    def _get_client(lst, curr_name):
        found_client = next((c for c in lst if c.name == curr_name), None)
        return found_client
