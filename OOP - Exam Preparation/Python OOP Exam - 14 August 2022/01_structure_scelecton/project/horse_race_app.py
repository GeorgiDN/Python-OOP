from project.horse_race import HorseRace
from project.horse_specification.appaloosa import Appaloosa
from project.horse_specification.thoroughbred import Thoroughbred
from project.jockey import Jockey


class HorseRaceApp:
    VALID_HORSE_TYPES = {"Appaloosa": Appaloosa, "Thoroughbred": Thoroughbred}

    def __init__(self):
        self.horses: list = []
        self.jockeys: list = []
        self.horse_races: list = []

    def add_horse(self, horse_type: str, horse_name: str, horse_speed: int):
        horse = self._get_object_by_name(self.horses, horse_name)
        if horse:
            raise Exception(f"Horse {horse_name} has been already added!")

        if horse_type in self.VALID_HORSE_TYPES:
            new_horse = self.VALID_HORSE_TYPES[horse_type](horse_name, horse_speed)
            self.horses.append(new_horse)
            return f"{horse_type} horse {horse_name} is added."

    def add_jockey(self, jockey_name: str, age: int):
        jockey = self._get_object_by_name(self.jockeys, jockey_name)
        if jockey:
            raise Exception(f"Jockey {jockey_name} has been already added!")

        new_jockey = Jockey(jockey_name, age)
        self.jockeys.append(new_jockey)
        return f"Jockey {jockey_name} is added."

    def create_horse_race(self, race_type: str):
        race = self._get_object_by_type(self.horse_races, race_type)
        if race:
            raise Exception(f"Race {race_type} has been already created!")

        new_race = HorseRace(race_type)
        self.horse_races.append(new_race)
        return f"Race {race_type} is created."

    def add_horse_to_jockey(self, jockey_name: str, horse_type: str):
        jockey = self._get_object_by_name(self.jockeys, jockey_name)
        current_horse = self._get_last_added_horse_by_type(self.horses, horse_type)

        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if current_horse is None:
            raise Exception(f"Horse breed {horse_type} could not be found!")

        if jockey.horse is not None:
            return f"Jockey {jockey_name} already has a horse."

        jockey.horse = current_horse
        current_horse.is_taken = True
        return f"Jockey {jockey_name} will ride the horse {current_horse.name}."

    def add_jockey_to_horse_race(self, race_type: str, jockey_name: str):
        horse_race = self._get_object_by_type(self.horse_races, race_type)
        jockey = self._get_object_by_name(self.jockeys, jockey_name)

        if horse_race is None:
            raise Exception(f"Race {race_type} could not be found!")

        if jockey is None:
            raise Exception(f"Jockey {jockey_name} could not be found!")

        if jockey.horse is None:
            raise Exception(f"Jockey {jockey_name} cannot race without a horse!")

        if jockey in horse_race.jockeys:
            return f"Jockey {jockey_name} has been already added to the {race_type} race."

        horse_race.jockeys.append(jockey)
        return f"Jockey {jockey_name} added to the {race_type} race."

    def start_horse_race(self, race_type: str):
        horse_race = self._get_object_by_type(self.horse_races, race_type)
        if horse_race is None:
            raise Exception(f"Race {race_type} could not be found!")

        if len(horse_race.jockeys) < 2:
            raise Exception(f"Horse race {race_type} needs at least two participants!")

        winner = max(horse_race.jockeys, key=lambda jokey: jokey.horse.speed)

        return (f"The winner of the {horse_race.race_type} race, "
                f"with a speed of {winner.horse.speed}km/h is {winner.name}! Winner's horse: {winner.horse.name}.")

    # # Helper methods
    @staticmethod
    def _get_object_by_name(object_list, name):
        found_object = next((obj for obj in object_list if obj.name == name), None)
        return found_object

    @staticmethod
    def _get_object_by_type(object_list, type_):
        found_object = next((obj for obj in object_list if obj.race_type == type_), None)
        return found_object

    @staticmethod
    def _get_last_added_horse_by_type(horse_list, type_):
        found_horses = [h for h in horse_list if h.TYPE == type_ and not h.is_taken]
        return found_horses[-1] if found_horses else None


# horseRaceApp = HorseRaceApp()
# print(horseRaceApp.add_horse("Appaloosa", "Spirit", 80))
# print(horseRaceApp.add_horse("Thoroughbred", "Rocket", 110))
# print(horseRaceApp.add_jockey("Peter", 19))
# print(horseRaceApp.add_jockey("Mariya", 21))
# print(horseRaceApp.create_horse_race("Summer"))
# print(horseRaceApp.add_horse_to_jockey("Peter", "Appaloosa"))
# print(horseRaceApp.add_horse_to_jockey("Peter", "Thoroughbred"))
# print(horseRaceApp.add_horse_to_jockey("Mariya", "Thoroughbred"))
# print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
# print(horseRaceApp.add_jockey_to_horse_race("Summer", "Peter"))
# print(horseRaceApp.add_jockey_to_horse_race("Summer", "Mariya"))
# print(horseRaceApp.start_horse_race("Summer"))



"""
Appaloosa horse Spirit is added.
Thoroughbred horse Rocket is added.
Jockey Peter is added.
Jockey Mariya is added.
Race Summer is created.
Jockey Peter will ride the horse Spirit.
Jockey Peter already has a horse.
Jockey Mariya will ride the horse Rocket.
Jockey Mariya added to the Summer race.
Jockey Peter added to the Summer race.
Jockey Mariya has been already added to the Summer race.
The winner of the Summer race, with a speed of 110km/h is Mariya! Winner's horse: Rocket.
"""
