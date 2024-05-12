from project.teams.indoor_team import IndoorTeam
from project.teams.outdoor_team import OutdoorTeam
from project.equipment.knee_pad import KneePad
from project.equipment.elbow_pad import ElbowPad


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
            raise ValueError("Invalid equipment type!")

        new_equipment = self.VALID_EQUIPMENTS[equipment_type]()
        self.equipment.append(new_equipment)
        return f"{equipment_type} was successfully added."

    def add_team(self, team_type: str, team_name: str, country: str, advantage: int):
        if team_type not in self.VALID_TEAMS:
            raise ValueError("Invalid team type!")

        if len(self.teams) >= self.capacity:
            return "Not enough tournament capacity."

        new_team = self.VALID_TEAMS[team_type](team_name, country, advantage)
        self.teams.append(new_team)
        return f"{team_type} was successfully added."

    def sell_equipment(self, equipment_type: str, team_name: str):
        curr_team = self._get_team(self.teams, team_name)
        curr_equipment = self._get_equipment(self.equipment, equipment_type)

        if curr_team.budget < curr_equipment.price:
            raise Exception("Budget is not enough!")

        self.equipment.remove(curr_equipment)
        curr_team.equipment.append(curr_equipment)
        curr_team.budget -= curr_equipment.price
        return f"Successfully sold {equipment_type} to {team_name}."

    def remove_team(self, team_name: str):
        curr_team = self._get_team(self.teams, team_name)
        if not curr_team:
            raise Exception("No such team!")

        if curr_team.wins > 0:
            raise Exception(f"The team has {curr_team.wins} wins! Removal is impossible!")

        self.teams.remove(curr_team)
        return f"Successfully removed {team_name}."

    def increase_equipment_price(self, equipment_type: str):
        number_of_changed_equipment = 0
        for equip in self.equipment:
            if equip.TYPE == equipment_type:
                equip.increase_price()
                number_of_changed_equipment += 1
        return f"Successfully changed {number_of_changed_equipment}pcs of equipment."

    def play(self, team_name1: str, team_name2: str):
        team1 = self._get_team(self.teams, team_name1)
        team2 = self._get_team(self.teams, team_name2)

        if team1.TYPE != team2.TYPE:
            raise Exception("Game cannot start! Team types mismatch!")

        team_1_total_protection = sum(t.protection for t in team1.equipment)
        team_1_points = team1.advantage + team_1_total_protection

        team_2_total_protection = sum(t.protection for t in team2.equipment)
        team_2_points = team2.advantage + team_2_total_protection

        winner = team1 if team_1_points > team_2_points \
            else team2 if team_2_points > team_1_points \
            else None

        if not winner:
            return "No winner in this game."

        winner.win()
        return f"The winner is {winner.name}."

    def get_statistics(self):
        sorted_teams = sorted(self.teams, key=lambda t: -t.wins)
        result = (f"Tournament: {self.name}\n"
                  f"Number of Teams: {len(self.teams)}\n"
                  f"Teams:\n")
        for team in sorted_teams:
            result += team.get_statistics()
            result += '\n'

        return result.strip()

    # Helper methods
    @staticmethod
    def _get_team(lst, t_name):
        found_team = next((t for t in lst if t.name == t_name), None)
        return found_team

    @staticmethod
    def _get_equipment(lst, e_type):
        found_equipment = [e for e in lst if e.TYPE == e_type]
        return found_equipment[-1] if found_equipment else None
