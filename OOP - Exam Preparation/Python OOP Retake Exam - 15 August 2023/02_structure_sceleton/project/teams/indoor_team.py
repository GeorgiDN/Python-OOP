from project.teams.base_team import BaseTeam


class IndoorTeam(BaseTeam):
    TYPE = "IndoorTeam"
    ADVANTAGE_INCREASE = 145

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, 500.0)

    def win(self):
        self.advantage += self.ADVANTAGE_INCREASE
        self.wins += 1
