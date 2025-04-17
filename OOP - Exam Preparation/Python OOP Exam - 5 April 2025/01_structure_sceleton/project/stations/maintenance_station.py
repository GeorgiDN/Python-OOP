from project.stations.base_station import BaseStation


class MaintenanceStation(BaseStation):
    CAPACITY = 3
    USD_INCREASE = 3000

    def __init__(self, name: str):
        super().__init__(name, self.CAPACITY)

    def update_salaries(self, min_value: float):
        for astronaut in self.astronauts:
            if astronaut.__class__.__name__ == "EngineerAstronaut" and astronaut.salary <= min_value:
                astronaut.salary += self.USD_INCREASE
