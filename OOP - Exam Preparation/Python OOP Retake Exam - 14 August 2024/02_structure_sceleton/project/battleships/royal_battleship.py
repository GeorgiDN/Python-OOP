from project.battleships.base_battleship import BaseBattleship


class RoyalBattleship(BaseBattleship):
    AMMUNITION = 100
    AMMUNITION_DECREASE = 25

    def __init__(self, name: str, health: int, hit_strength: int):
        super().__init__(name, health, hit_strength, self.AMMUNITION)

    def attack(self):
        self.ammunition = max(self.ammunition - self.AMMUNITION_DECREASE, 0)
