from project.customer import Customer
from project.dvd import DVD
from typing import List


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity():
        return DVD.CAPACITY

    @staticmethod
    def customer_capacity():
        return Customer.CAPACITY

    def add_customer(self, customer: Customer):
        if len(self.customers) < customer.CAPACITY:
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < dvd.CAPACITY:
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        customer = self._find_object_by_id(self.customers, customer_id)
        dvd = self._find_object_by_id(self.dvds, dvd_id)

        if dvd in customer.rented_dvds:
            return f"{customer.name} has already rented {dvd.name}"

        if dvd.is_rented:
            return "DVD is already rented"

        if customer.age < dvd.age_restriction:
            return f"{customer.name} should be at least {dvd.age_restriction} to rent this movie"

        customer.rented_dvds.append(dvd)
        dvd.is_rented = True
        return f"{customer.name} has successfully rented {dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        customer = self._find_object_by_id(self.customers, customer_id)
        dvd = self._find_object_by_id(self.dvds, dvd_id)

        if dvd not in customer.rented_dvds:
            return f"{customer.name} does not have that DVD"

        customer.rented_dvds.remove(dvd)
        dvd.is_rented = False
        return f"{customer.name} has successfully returned {dvd.name}"

    def __repr__(self):
        result = []
        customer_data = '\n'.join([c.__repr__() for c in self.customers])
        dvd_data = '\n'.join([d.__repr__() for d in self.dvds])
        result.append(customer_data)
        result.append(dvd_data)
        return "\n".join(result)

    @staticmethod
    def _find_object_by_id(lst, _id):
        found_object = next((obj for obj in lst if obj.id == _id), None)
        return found_object
