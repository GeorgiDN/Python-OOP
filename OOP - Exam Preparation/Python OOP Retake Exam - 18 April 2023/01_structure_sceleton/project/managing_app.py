from typing import List

from project.route import Route
from project.user import User
from project.vehicles.cargo_van import CargoVan
from project.vehicles.passenger_car import PassengerCar


class ManagingApp:
    VEHICLES_TYPES = {"PassengerCar": PassengerCar, "CargoVan": CargoVan}

    def __init__(self):
        self.users: list = []
        self.vehicles: list = []
        self.routes: list = []

    def register_user(self, first_name: str, last_name: str, driving_license_number: str):
        user = self._get_user_by_number(self.users, driving_license_number)
        if user:
            return f"{driving_license_number} has already been registered to our platform."
        new_user = User(first_name, last_name, driving_license_number)
        self.users.append(new_user)
        return f"{first_name} {last_name} was successfully registered under DLN-{driving_license_number}"

    def upload_vehicle(self, vehicle_type: str, brand: str, model: str, license_plate_number: str):
        if vehicle_type not in self.VEHICLES_TYPES:
            return f"Vehicle type {vehicle_type} is inaccessible."

        vehicle = self._get_vehicle(self.vehicles, license_plate_number)
        if vehicle:
            return f"{license_plate_number} belongs to another vehicle."

        new_vehicle = self.VEHICLES_TYPES[vehicle_type](brand, model, license_plate_number)
        self.vehicles.append(new_vehicle)
        return f"{brand} {model} was successfully uploaded with LPN-{license_plate_number}."

    def allow_route(self, start_point: str, end_point: str, length: float):
        route_id = len(self.routes) + 1
        if self.routes:
            for route in self.routes:
                if route.start_point == start_point and route.end_point == end_point:
                    if route.length == length:
                        return f"{start_point}/{end_point} - {length} km had already been added to our platform."
                    elif route.length < length:
                        return f"{start_point}/{end_point} shorter route had already been added to our platform."
                    elif route.length > length:
                        route.is_locked = True

        new_route = Route(start_point, end_point, length, route_id)
        self.routes.append(new_route)
        return f"{start_point}/{end_point} - {length} km is unlocked and available to use."

    def make_trip(self, driving_license_number: str, license_plate_number: str, route_id: int,  is_accident_happened: bool):
        user = self._get_user_by_number(self.users, driving_license_number)
        if user.is_blocked:
            return f"User {driving_license_number} is blocked in the platform! This trip is not allowed."

        vehicle = self._get_vehicle(self.vehicles, license_plate_number)
        if vehicle.is_damaged:
            return f"Vehicle {license_plate_number} is damaged! This trip is not allowed."

        route = self._get_route(self.routes, route_id)
        if route.is_locked:
            return f"Route {route_id} is locked! This trip is not allowed."

        current_mileage = route.length
        vehicle.drive(current_mileage)
        if is_accident_happened:
            vehicle.is_damaged = True
            user.decrease_rating()
        else:
            user.increase_rating()

        return str(vehicle)

    def repair_vehicles(self, count: int):
        damaged_vehicles = [vehicle for vehicle in self.vehicles if vehicle.is_damaged]
        selected_vehicles = sorted(damaged_vehicles, key=lambda vehicle: (vehicle.brand, vehicle.model))[:count]
        for vehicle in selected_vehicles:
            vehicle.is_damaged = False
            vehicle.battery_level = 100
        return f"{len(selected_vehicles)} vehicles were successfully repaired!"

    def users_report(self):
        sorted_users = sorted(self.users, key=lambda user: user.rating, reverse=True)
        result = "*** E-Drive-Rent ***\n"
        for user in sorted_users:
            result += str(user) + "\n"

        return result.strip()

    @staticmethod
    def _get_user_by_number(lst, license_number):
        found_user = next((user for user in lst if user.driving_license_number == license_number), None)
        return found_user

    @staticmethod
    def _get_vehicle(lst, license_number):
        found_vehicle = next((v for v in lst if v.license_plate_number == license_number), None)
        return found_vehicle

    @staticmethod
    def _get_route(lst, _id):
        found_route = next((route for route in lst if route.route_id == _id), None)
        return found_route
