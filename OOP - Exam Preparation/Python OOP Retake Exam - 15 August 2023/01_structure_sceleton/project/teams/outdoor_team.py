from project.teams.base_team import BaseTeam


class OutdoorTeam(BaseTeam):
    TYPE = "OutdoorTeam"

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, 1000.0)

    def win(self):
        self.wins += 1
        self.advantage += 115
