from project.astronauts.engineer_astronaut import EngineerAstronaut
from project.astronauts.scientist_astronaut import ScientistAstronaut
from project.stations.maintenance_station import MaintenanceStation
from project.stations.research_station import ResearchStation


class SpaceAgency:
    VALID_ASTRONAUTS = {"EngineerAstronaut": EngineerAstronaut, "ScientistAstronaut": ScientistAstronaut}
    VALID_STATIONS = {"ResearchStation": ResearchStation, "MaintenanceStation": MaintenanceStation}

    def __init__(self):
        self.astronauts: list = []
        self.stations: list = []

    def add_astronaut(self, astronaut_type: str, astronaut_id_number: str, astronaut_salary: float):
        if astronaut_type not in self.VALID_ASTRONAUTS:
            raise ValueError("Invalid astronaut type!")

        astronaut = self.get_object_by_id(self.astronauts, astronaut_id_number)
        if astronaut:
            raise ValueError(f"{astronaut_id_number} has been already added!")

        new_astronaut = self.VALID_ASTRONAUTS[astronaut_type](astronaut_id_number, astronaut_salary)
        self.astronauts.append(new_astronaut)
        return f"{astronaut_id_number} is successfully hired as {astronaut_type}."

    def add_station(self, station_type: str, station_name: str):
        if station_type not in self.VALID_STATIONS:
            raise ValueError("Invalid station type!")

        station = self.get_object_by_name(self.stations, station_name)
        if station:
            raise ValueError(f"{station_name} has been already added!")

        new_station = self.VALID_STATIONS[station_type](station_name)
        self.stations.append(new_station)
        return f"{station_name} is successfully added as a {station_type}."

    def assign_astronaut(self, station_name: str, astronaut_type: str):
        station = self.get_object_by_name(self.stations, station_name)
        if not station:
            raise ValueError(f"Station {station_name} does not exist!")

        astronaut = self.get_object_by_type(self.astronauts, astronaut_type)
        if not astronaut:
            raise ValueError("No available astronauts of the type!")

        if station.capacity == 0:
            return "This station has no available capacity."

        self.astronauts.remove(astronaut)
        station.astronauts.append(astronaut)
        station.capacity -= 1
        return f"{astronaut.id_number} was assigned to {station_name}."

    def train_astronauts(self, station, sessions_number: int):
        for session in range(sessions_number):
            for astronaut in station.astronauts:
                astronaut.train()
        total_stamina = sum(a.stamina for a in station.astronauts)
        return (f"{station.name} astronauts have {total_stamina} total stamina "
                f"after {sessions_number} training session/s.")

    def retire_astronaut(self, station, astronaut_id_number: str):
        astronaut = self.get_object_by_id(station.astronauts, astronaut_id_number)

        if not astronaut or astronaut.stamina == 100:
            return "The retirement process was canceled."

        station.astronauts.remove(astronaut)
        station.capacity += 1
        return f"Retired astronaut {astronaut_id_number}."

    def agency_update(self, min_value: float):
        for station in self.stations:
            station.update_salaries(min_value)

        result = ["*Space Agency Up-to-Date Report*"]

        available_astronauts_count = len(self.astronauts)
        result.append(f"Total number of available astronauts: {available_astronauts_count}")

        stations_total_count = len(self.stations)
        result.append(
            f"**Stations count: {stations_total_count}; "
            f"Total available capacity: {sum(s.capacity for s in self.stations)}**")

        sorted_stations = sorted(self.stations, key=lambda s: (-len(s.astronauts), s.name))

        for station in sorted_stations:
            result.append(station.status())

        return "\n".join(result)

    ###
    @staticmethod
    def get_object_by_id(object_list, id_):
        found_object = next((obj for obj in object_list if obj.id_number == id_), None)
        return found_object

    @staticmethod
    def get_object_by_name(object_list, name):
        found_object = next((obj for obj in object_list if obj.name == name), None)
        return found_object

    @staticmethod
    def get_object_by_type(object_list, type_):
        found_object = next((obj for obj in object_list if obj.__class__.__name__ == type_), None)
        return found_object


#########################################################################################
# # Create an instance of the Space Agency Manager
# manager = SpaceAgency()
#
# # Add astronauts (engineers & scientists)
# print(manager.add_astronaut("EngineerAstronaut", "02345", 780_000.0))
# print(manager.add_astronaut("EngineerAstronaut", "1234", 500_000.0))
# print(manager.add_astronaut("EngineerAstronaut", "789123", 800_000.0))
# print(manager.add_astronaut("EngineerAstronaut", "45678999", 702_000.0))
# print(manager.add_astronaut("ScientistAstronaut", "321654", 401_000.0))
# print(manager.add_astronaut("ScientistAstronaut", "6543211", 490_000.0))
# print(manager.add_astronaut("ScientistAstronaut", "334654", 600_000.0))
# print(manager.add_astronaut("ScientistAstronaut", "034654", 395_000.0))
# print()
#
# # Add stations
# print(manager.add_station("MaintenanceStation", "Lunar-Base"))
# print(manager.add_station("ResearchStation", "ISS-3"))
# print(manager.add_station("ResearchStation", "Mars-Habitat"))
# print()
#
# # Assign astronauts to stations
# print(manager.assign_astronaut("Lunar-Base", "EngineerAstronaut"))
# print(manager.assign_astronaut("Lunar-Base", "EngineerAstronaut"))
# print(manager.assign_astronaut("Lunar-Base", "ScientistAstronaut"))
# print(manager.assign_astronaut("ISS-3", "ScientistAstronaut"))
# print(manager.assign_astronaut("ISS-3", "ScientistAstronaut"))
# print(manager.assign_astronaut("ISS-3", "EngineerAstronaut"))
# print(manager.assign_astronaut("ISS-3", "EngineerAstronaut"))
# print()
#
# # Conduct training sessions
# print(manager.train_astronauts(manager.stations[0], 0))
# print(manager.train_astronauts(manager.stations[0], 1))
# print(manager.train_astronauts(manager.stations[0], 2))
# print(manager.train_astronauts(manager.stations[0], 3))
# print(manager.train_astronauts(manager.stations[0], 3))
# print(manager.train_astronauts(manager.stations[1], 0))
# print(manager.train_astronauts(manager.stations[2], 1))
# print()
#
# # Retire an astronaut
# print(manager.retire_astronaut(manager.stations[2], "334654"))
# print(manager.retire_astronaut(manager.stations[0], "02345"))
# print(manager.stations[0].astronauts[0].id_number, manager.stations[0].astronauts[0].stamina)
# print(manager.retire_astronaut(manager.stations[0], "111111"))
# print(manager.retire_astronaut(manager.stations[1], "45678999"))
# print()
#
# # Perform an agency-wide update
# print(manager.agency_update(500_000.0))
# print()
#
# # Check astronaut salaries after the update
# print(manager.stations[0].astronauts[0].salary)
# print(manager.stations[0].astronauts[1].salary)
# print(manager.stations[0].astronauts[2].salary)
# print()
# print(manager.stations[1].astronauts[0].salary)
# print(manager.stations[1].astronauts[1].salary)
# print(manager.stations[1].astronauts[2].salary)
# print()
# print(manager.astronauts[0].salary)


"""
02345 is successfully hired as EngineerAstronaut.
1234 is successfully hired as EngineerAstronaut.
789123 is successfully hired as EngineerAstronaut.
45678999 is successfully hired as EngineerAstronaut.
321654 is successfully hired as ScientistAstronaut.
6543211 is successfully hired as ScientistAstronaut.
334654 is successfully hired as ScientistAstronaut.
034654 is successfully hired as ScientistAstronaut.

Lunar-Base is successfully added as a MaintenanceStation.
ISS-3 is successfully added as a ResearchStation.
Mars-Habitat is successfully added as a ResearchStation.

02345 was assigned to Lunar-Base.
1234 was assigned to Lunar-Base.
321654 was assigned to Lunar-Base.
6543211 was assigned to ISS-3.
334654 was assigned to ISS-3.
789123 was assigned to ISS-3.
45678999 was assigned to ISS-3.

Lunar-Base astronauts have 230 total stamina after 0 training session/s.
Lunar-Base astronauts have 243 total stamina after 1 training session/s.
Lunar-Base astronauts have 269 total stamina after 2 training session/s.
Lunar-Base astronauts have 288 total stamina after 3 training session/s.
Lunar-Base astronauts have 297 total stamina after 3 training session/s.
ISS-3 astronauts have 300 total stamina after 0 training session/s.
Mars-Habitat astronauts have 0 total stamina after 1 training session/s.

The retirement process was canceled.
The retirement process was canceled.
02345 100
The retirement process was canceled.
Retired astronaut 45678999.

*Space Agency Up-to-Date Report*
Total number of available astronauts: 1
**Stations count: 3; Total available capacity: 7**
Station name: ISS-3; Astronauts: 334654 #6543211 #789123; Total salaries: 1895000.00
Station name: Lunar-Base; Astronauts: 02345 #1234 #321654; Total salaries: 1684000.00
Station name: Mars-Habitat; Astronauts: N/A; Total salaries: 0.00

780000.0
503000.0
401000.0

495000.0
600000.0
800000.0

395000.0
"""
