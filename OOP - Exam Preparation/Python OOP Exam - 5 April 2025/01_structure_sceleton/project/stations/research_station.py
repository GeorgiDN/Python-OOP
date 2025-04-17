from project.stations.base_station import BaseStation


class ResearchStation(BaseStation):
    CAPACITY = 5
    USD_INCREASE = 5000

    def __init__(self, name: str):
        super().__init__(name, self.CAPACITY)

    def update_salaries(self, min_value: float):
        for astronaut in self.astronauts:
            if astronaut.__class__.__name__ == "ScientistAstronaut" and astronaut.salary <= min_value:
                astronaut.salary += self.USD_INCREASE
