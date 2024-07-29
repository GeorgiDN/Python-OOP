from project.equipment.knee_pad import KneePad
from project.equipment.elbow_pad import ElbowPad
from project.teams.outdoor_team import OutdoorTeam
from project.teams.indoor_team import IndoorTeam


class Tournament:
    VALID_EQUIPMENTS = {"KneePad": KneePad, "ElbowPad": ElbowPad}
    VALID_TEAMS = {"OutdoorTeam": OutdoorTeam, "IndoorTeam": IndoorTeam}

    def __init__(self, name: str, capacity: int):
        self.name = name
        self.capacity = capacity
        self.equipment: list = []
        self.teams: list = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.isalnum():
            raise ValueError("Tournament name should contain letters and digits only!")
        self.__name = value

    def add_equipment(self, equipment_type: str):
        if equipment_type not in self.VALID_EQUIPMENTS:
            raise Exception("Invalid equipment type!")

        new_equipment = self.VALID_EQUIPMENTS[equipment_type]()
        self.equipment.append(new_equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.VALID_TEAMS:
            raise Exception("Invalid team type!")

        if len(self.teams) >= self.capacity:
            return f"Not enough tournament capacity."

        new_team = self.VALID_TEAMS[team_type](team_name, country, advantage)
        self.teams.append(new_team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        team = self._get_object_by_name(self.teams, team_name)
        curr_equipment = self._get_last_added_object_by_type(self.equipment, equipment_type)

        if team.budget < curr_equipment.price:
            raise Exception("Budget is not enough!")

        team.budget -= curr_equipment.price
        team.equipment.append(curr_equipment)
        self.equipment.remove(curr_equipment)
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        team = self._get_object_by_name(self.teams, team_name)
        if team is None:
            raise Exception("No such team!")

        if team.wins > 0:
            raise Exception(f"The team has {team.wins} wins! Removal is impossible!")

        self.teams.remove(team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        number_of_changed_equipment = 0
        for equipment in self.equipment:
            if equipment.TYPE == equipment_type:
                equipment.increase_price()
                number_of_changed_equipment += 1

        return f"Successfully changed {number_of_changed_equipment}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = self._get_object_by_name(self.teams, team_name1)
        team2 = self._get_object_by_name(self.teams, team_name2)

        if team1.TYPE != team2.TYPE:
            raise Exception("Game cannot start! Team types mismatch!")

        team1_total_points = sum(e.protection for e in team1.equipment) + team1.advantage
        team2_total_points = sum(e.protection for e in team2.equipment) + team2.advantage

        winner = None
        if team1_total_points > team2_total_points:
            winner = team1
        elif team1_total_points < team2_total_points:
            winner = team2

        if winner:
            winner.win()
            return f"The winner is {winner.name}."

        return "No winner in this game."

    def get_statistics(self):
        result = [f"Tournament: {self.name}"]
        result.append(f"Number of Teams: {len(self.teams)}")
        result.append("Teams:")
        sorted_teams = sorted(self.teams, key=lambda x: -x.wins)
        for team in sorted_teams:
            result.append(team.get_statistics())

        return "\n".join(result)

    ###
    @staticmethod
    def _get_object_by_name(object_list, name):
        found_object = next((obj for obj in object_list if obj.name == name), None)
        return found_object

    @staticmethod
    def _get_last_added_object_by_type(object_list, object_type):
        found_object = [obj for obj in object_list if obj.TYPE == object_type]
        return found_object[-1] if found_object else None


# t = Tournament('SoftUniada2023', 2)
#
# print(t.add_equipment('KneePad'))
# print(t.add_equipment('ElbowPad'))
#
# print(t.add_team('OutdoorTeam', 'Levski', 'BG', 250))
# print(t.add_team('OutdoorTeam', 'Spartak', 'BG', 250))
# print(t.add_team('IndoorTeam', 'Dobrich', 'BG', 280))
#
# print(t.sell_equipment('KneePad', 'Spartak'))
#
# print(t.remove_team('Levski'))
# print(t.add_team('OutdoorTeam', 'Lokomotiv', 'BG', 250))
#
# print(t.increase_equipment_price('ElbowPad'))
# print(t.increase_equipment_price('KneePad'))
#
# print(t.play('Lokomotiv', 'Spartak'))
#
# print(t.get_statistics())



"""
KneePad was successfully added.
ElbowPad was successfully added.
OutdoorTeam was successfully added.
OutdoorTeam was successfully added.
Not enough tournament capacity.
Successfully sold KneePad to Spartak.
Successfully removed Levski.
OutdoorTeam was successfully added.
Successfully changed 1pcs of equipment.
Successfully changed 0pcs of equipment.
The winner is Spartak.
Tournament: SoftUniada2023
Number of Teams: 2
Teams:
Name: Spartak
Country: BG
Advantage: 365 points
Budget: 985.00EUR
Wins: 1
Total Equipment Price: 15.00
Average Protection: 120
Name: Lokomotiv
Country: BG
Advantage: 250 points
Budget: 1000.00EUR
Wins: 0
Total Equipment Price: 0.00
Average Protection: 0
"""
