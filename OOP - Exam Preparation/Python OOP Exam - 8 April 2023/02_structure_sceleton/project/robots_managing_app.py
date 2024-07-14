from project.robots.male_robot import MaleRobot
from project.robots.female_robot import FemaleRobot
from project.services.main_service import MainService
from project.services.secondary_service import SecondaryService


class RobotsManagingApp:
    SERVICES_TYPES = {"MainService": MainService, "SecondaryService": SecondaryService}
    ROBOTS_TYPES = {"MaleRobot": MaleRobot, "FemaleRobot": FemaleRobot}

    def __init__(self):
        self.robots: list = []
        self.services: list = []

    def add_service(self, service_type: str, name: str):
        if service_type not in self.SERVICES_TYPES:
            raise Exception("Invalid service type!")

        new_service = self.SERVICES_TYPES[service_type](name)
        self.services.append(new_service)
        return f"{service_type} is successfully added."

    def add_robot(self, robot_type: str, name: str, kind: str, price: float):
        if robot_type not in self.ROBOTS_TYPES:
            raise Exception("Invalid robot type!")

        new_robot = self.ROBOTS_TYPES[robot_type](name, kind, price)
        self.robots.append(new_robot)
        return f"{robot_type} is successfully added."

    def add_robot_to_service(self, robot_name: str, service_name: str):
        robot = self._get_robot_by_name(self.robots, robot_name)
        service = self._get_service_by_name(self.services, service_name)

        if (robot.TYPE == "MaleRobot" and service.TYPE == "SecondaryService") or \
                (robot.TYPE == "FemaleRobot" and service.TYPE == "MainService"):
            return "Unsuitable service."

        if len(service.robots) >= service.capacity:
            raise Exception("Not enough capacity for this robot!")

        self.robots.remove(robot)
        service.robots.append(robot)
        return f"Successfully added {robot_name} to {service_name}."

    def remove_robot_from_service(self, robot_name: str, service_name: str):
        service = self._get_service_by_name(self.services, service_name)
        robot = self._get_robot_by_name(service.robots, robot_name)

        if robot is None:
            raise Exception("No such robot in this service!")

        service.robots.remove(robot)
        self.robots.append(robot)
        return f"Successfully removed {robot_name} from {service_name}."

    def feed_all_robots_from_service(self, service_name: str):
        service = self._get_service_by_name(self.services, service_name)
        number_of_robots_fed = 0

        for robot in service.robots:
            robot.eating()
            number_of_robots_fed += 1

        return f"Robots fed: {number_of_robots_fed}."

    def service_price(self, service_name: str):
        service = self._get_service_by_name(self.services, service_name)
        total_price = 0

        for robot in service.robots:
            total_price += robot.price

        return f"The value of service {service_name} is {total_price:.2f}."

    def __str__(self):
        result = ""
        for service in self.services:
            result += service.details() + "\n"

        return result.strip()

    # # Helper methods
    @staticmethod
    def _get_robot_by_name(my_list, robot_name):
        found_robot = next((r for r in my_list if r.name == robot_name), None)
        return found_robot

    @staticmethod
    def _get_service_by_name(my_list, service_name):
        found_service = next((s for s in my_list if s.name == service_name), None)
        return found_service




