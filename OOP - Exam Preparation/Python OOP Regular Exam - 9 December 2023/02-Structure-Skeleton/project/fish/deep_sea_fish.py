from project.fish.base_fish import BaseFish


class DeepSeaFish(BaseFish):
    def __init__(self, name: str, points: float):
        super().__init__(name, points, 180)

    def get_fish_details(self):
        return self.fish_details()
