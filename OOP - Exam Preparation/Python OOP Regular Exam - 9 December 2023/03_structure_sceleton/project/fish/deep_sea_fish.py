from project.fish.base_fish import BaseFish


class DeepSeaFish(BaseFish):
    TYPE = "DeepSeaFish"
    TIME_TO_CATCH = 180

    def __init__(self, name: str, points: float):
        super().__init__(name, points, time_to_catch=self.TIME_TO_CATCH)

    def show_fish_details(self):
        return self.fish_details()


# f = DeepSeaFish("Fish Name", 9)
# print(f.show_fish_details())
