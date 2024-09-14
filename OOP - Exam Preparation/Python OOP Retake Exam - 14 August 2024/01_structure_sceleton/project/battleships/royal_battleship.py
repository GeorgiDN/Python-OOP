from project.battleships.base_battleship import BaseBattleship


class RoyalBattleship(BaseBattleship):
    AMMUNITION = 100

    def __init__(self, name: str, health: int, hit_strength: int):
        super().__init__(name, health, hit_strength, ammunition=self.AMMUNITION)

    def attack(self):
        self.ammunition = max(0, self.ammunition - 25)