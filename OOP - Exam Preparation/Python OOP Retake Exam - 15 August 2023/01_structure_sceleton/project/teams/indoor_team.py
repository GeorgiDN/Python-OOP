# from project.equipment.knee_pad import KneePad
from project.teams.base_team import BaseTeam


class IndoorTeam(BaseTeam):
    TYPE = "IndoorTeam"

    def __init__(self, name: str, country: str, advantage: int):
        super().__init__(name, country, advantage, 500.0)

    def win(self):
        self.wins += 1
        self.advantage += 145


# k = KneePad()
# print(k.price)
#

# ind = IndoorTeam('Indoor', 'USA', 100)
# ind.equipment.append(k)
# ind.win()
# print(ind.get_statistics())

