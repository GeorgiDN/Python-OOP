from project.customer import Customer
from typing import List
from project.dvd import DVD


class MovieWorld:
    def __init__(self, name: str):
        self.name = name
        self.customers: List[Customer] = []
        self.dvds: List[DVD] = []

    @staticmethod
    def dvd_capacity():
        return 15

    @staticmethod
    def customer_capacity():
        return 10

    def add_customer(self, customer: Customer):
        if len(self.customers) < MovieWorld.customer_capacity():
            self.customers.append(customer)

    def add_dvd(self, dvd: DVD):
        if len(self.dvds) < self.dvd_capacity():
            self.dvds.append(dvd)

    def rent_dvd(self, customer_id: int, dvd_id: int):
        current_customer = self._find_item_by_id(self.customers, customer_id)
        current_dvd = self._find_item_by_id(self.dvds, dvd_id)

        if current_dvd in current_customer.rented_dvds:
            return f"{current_customer.name} has already rented {current_dvd.name}"

        if current_dvd.is_rented:
            return "DVD is already rented"

        if current_customer.age < current_dvd.age_restriction:
            return f"{current_customer.name} should be at least {current_dvd.age_restriction} to rent this movie"

        current_dvd.is_rented = True
        current_customer.rented_dvds.append(current_dvd)
        return f"{current_customer.name} has successfully rented {current_dvd.name}"

    def return_dvd(self, customer_id, dvd_id):
        current_customer = self._find_item_by_id(self.customers, customer_id)
        current_dvd = self._find_item_by_id(self.dvds, dvd_id)

        if current_dvd in current_customer.rented_dvds:
            current_customer.rented_dvds.remove(current_dvd)
            current_dvd.is_rented = False
            return f"{current_customer.name} has successfully returned {current_dvd.name}"
        return f"{current_customer.name} does not have that DVD"

    def __repr__(self):
        result = []
        result.extend(self.customers)
        result.extend(self.dvds)
        return '\n'.join(str(el) for el in result)

    # Helper method
    def _find_item_by_id(self, lst, id_number):
        found_element = next((element for element in lst if element.id == id_number), None)
        return found_element






# from project.customer import Customer
# from typing import List
# from project.dvd import DVD
#
#
# class MovieWorld:
#     def __init__(self, name: str):
#         self.name = name
#         self.customers: List[Customer] = []
#         self.dvds: List[DVD] = []
#
#     @staticmethod
#     def dvd_capacity():
#         return 15
#
#     @staticmethod
#     def customer_capacity():
#         return 10
#
#     def add_customer(self, customer: Customer):
#         if len(self.customers) < MovieWorld.customer_capacity():
#             self.customers.append(customer)
#
#     def add_dvd(self, dvd: DVD):
#         if len(self.dvds) < self.dvd_capacity():
#             self.dvds.append(dvd)
#
#     def rent_dvd(self, customer_id: int, dvd_id: int):
#         current_customer = self._find_element_by_id(self.customers, customer_id)
#         current_dvd = self._find_element_by_id(self.dvds, dvd_id)
#
#         if current_dvd is not None and current_customer is not None:
#             if current_dvd.is_rented:
#                 if current_dvd in current_customer.rented_dvds:
#                     return f"{current_customer.name} has already rented {current_dvd.name}"
#                 return "DVD is already rented"
#
#             if current_customer.age < current_dvd.age_restriction:
#                 return f"{current_customer.name} should be at least {current_dvd.age_restriction} to rent this movie"
#
#             current_dvd.is_rented = True
#             current_customer.rented_dvds.append(current_dvd)
#             return f"{current_customer.name} has successfully rented {current_dvd.name}"
#
#     def return_dvd(self, customer_id, dvd_id):
#         current_customer = self._find_element_by_id(self.customers, customer_id)
#         current_dvd = self._find_element_by_id(self.dvds, dvd_id)
#         if current_dvd is not None and current_customer is not None and current_dvd.is_rented:
#             if current_dvd in current_customer.rented_dvds:
#                 current_customer.rented_dvds.remove(current_dvd)
#                 current_dvd.is_rented = False
#                 return f"{current_customer.name} has successfully returned {current_dvd.name}"
#         return f"{current_customer.name} does not have that DVD"
#
#     def __repr__(self):
#         result = []
#         result.extend(self.customers)
#         result.extend(self.dvds)
#         return '\n'.join(str(el) for el in result)
#
#     # Helper method
#     def _find_element_by_id(self, lst, id_number):
#         found_element = next((element for element in lst if element.id == id_number), None)
#         return found_element
