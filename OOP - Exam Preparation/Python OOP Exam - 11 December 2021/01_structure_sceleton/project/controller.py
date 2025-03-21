from project.car.muscle_car import MuscleCar
from project.car.sports_car import SportsCar
from project.driver import Driver
from project.race import Race


class Controller:
    VALID_CARS = {"MuscleCar": MuscleCar, "SportsCar": SportsCar}

    def __init__(self):
        self.cars: list = []
        self.drivers: list = []
        self.races: list = []

    def create_car(self, car_type: str, model: str, speed_limit: int):
        car = self.get_object_by_model(self.cars, model)
        if car:
            raise Exception(f"Car {model} is already created!")

        if car_type in self.VALID_CARS:
            new_car = self.VALID_CARS[car_type](model, speed_limit)
            self.cars.append(new_car)
            return f"{car_type} {model} is created."

    def create_driver(self, driver_name: str):
        driver = self.get_object_by_name(self.drivers, driver_name)
        if driver:
            raise Exception(f"Driver {driver_name} is already created!")

        new_driver = Driver(driver_name)
        self.drivers.append(new_driver)
        return f"Driver {driver_name} is created."

    def create_race(self, race_name: str):
        race = self.get_object_by_name(self.races, race_name)
        if race:
            raise Exception(f"Race {race_name} is already created!")

        new_race = Race(race_name)
        self.races.append(new_race)
        return f"Race {race_name} is created."

    def add_car_to_driver(self, driver_name: str, car_type: str):
        driver = self.get_object_by_name(self.drivers, driver_name)
        car = self.get_last_added_object_by_type(self.cars, car_type)

        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if not car or car.is_taken:
            raise Exception(f"Car {car_type} could not be found!")

        if driver.car:
            old_model = driver.car.model
            new_model = car.model
            driver.car.is_taken = False
            car.is_taken = True
            driver.car = car
            return f"Driver {driver_name} changed his car from {old_model} to {new_model}."

        if driver.car is None:
            car.is_taken = True
            driver.car = car
            return f"Driver {driver_name} chose the car {car.model}."

    def add_driver_to_race(self, race_name: str, driver_name: str):
        race = self.get_object_by_name(self.races, race_name)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        driver = self.get_object_by_name(self.drivers, driver_name)
        if not driver:
            raise Exception(f"Driver {driver_name} could not be found!")

        if driver.car is None:
            raise Exception(f"Driver {driver_name} could not participate in the race!")

        if driver in race.drivers:
            return f"Driver {driver_name} is already added in {race_name} race."

        race.drivers.append(driver)
        return f"Driver {driver_name} added in {race_name} race."

    def start_race(self, race_name: str):
        race = self.get_object_by_name(self.races, race_name)
        if not race:
            raise Exception(f"Race {race_name} could not be found!")

        if len(race.drivers) < 3:
            raise Exception(f"Race {race_name} cannot start with less than 3 participants!")

        drivers = [d for d in race.drivers]
        sorted_drivers = sorted(drivers, key=lambda d: d.car.speed_limit, reverse=True)[:3]
        result = []
        for driver in sorted_drivers:
            driver.number_of_wins += 1
            result.append(f"Driver {driver.name} wins the {race_name} race with a speed of {driver.car.speed_limit}.")

        return "\n".join(result)

    @staticmethod
    def get_object_by_model(object_list, model):
        found_object = next((obj for obj in object_list if obj.model == model), None)
        return found_object

    @staticmethod
    def get_object_by_name(object_list, name):
        found_object = next((obj for obj in object_list if obj.name == name), None)
        return found_object

    @staticmethod
    def get_last_added_object_by_type(object_list, object_type):
        found_object = [obj for obj in object_list if obj.__class__.__name__ == object_type and not obj.is_taken]
        return found_object[-1] if found_object else None


# # TEST CODE
# controller = Controller()
# print(controller.create_driver("Peter"))
# print(controller.create_car("SportsCar", "Porsche 718 Boxster", 470))
# print(controller.add_car_to_driver("Peter", "SportsCar"))
# print(controller.create_car("SportsCar", "Porsche 911", 580))
# print(controller.add_car_to_driver("Peter", "SportsCar"))
# print(controller.create_car("MuscleCar", "BMW ALPINA B7", 290))
# print(controller.create_car("MuscleCar", "Mercedes-Benz AMG GLA 45", 420))
# print(controller.create_driver("John"))
# print(controller.create_driver("Jack"))
# print(controller.create_driver("Kelly"))
# print(controller.add_car_to_driver("Kelly", "MuscleCar"))
# print(controller.add_car_to_driver("Jack", "MuscleCar"))
# print(controller.add_car_to_driver("John", "SportsCar"))
# print(controller.create_race("Christmas Top Racers"))
# print(controller.add_driver_to_race("Christmas Top Racers", "John"))
# print(controller.add_driver_to_race("Christmas Top Racers", "Jack"))
# print(controller.add_driver_to_race("Christmas Top Racers", "Kelly"))
# print(controller.add_driver_to_race("Christmas Top Racers", "Peter"))
# print(controller.start_race("Christmas Top Racers"))
# [print(d.name, d.number_of_wins) for d in controller.drivers]


"""
Driver Peter is created.
SportsCar Porsche 718 Boxster is created.
Driver Peter chose the car Porsche 718 Boxster.
SportsCar Porsche 911 is created.
Driver Peter changed his car from Porsche 718 Boxster to Porsche 911.
MuscleCar BMW ALPINA B7 is created.
MuscleCar Mercedes-Benz AMG GLA 45 is created.
Driver John is created.
Driver Jack is created.
Driver Kelly is created.
Driver Kelly chose the car Mercedes-Benz AMG GLA 45.
Driver Jack chose the car BMW ALPINA B7.
Driver John chose the car Porsche 718 Boxster.
Race Christmas Top Racers is created.
Driver John added in Christmas Top Racers race.
Driver Jack added in Christmas Top Racers race.
Driver Kelly added in Christmas Top Racers race.
Driver Peter added in Christmas Top Racers race.
Driver Peter wins the Christmas Top Racers race with a speed of 580.
Driver John wins the Christmas Top Racers race with a speed of 470.
Driver Kelly wins the Christmas Top Racers race with a speed of 420.
Peter 1
John 1
Jack 0
Kelly 1
"""
