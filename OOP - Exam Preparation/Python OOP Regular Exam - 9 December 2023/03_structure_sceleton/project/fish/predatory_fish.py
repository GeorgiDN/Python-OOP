from project.fish.base_fish import BaseFish


class PredatoryFish(BaseFish):
    TYPE = "PredatoryFish"
    TIME_TO_CATCH = 90

    def __init__(self, name: str, points: float):
        super().__init__(name, points, time_to_catch=self.TIME_TO_CATCH)

    def show_fish_details(self):
        return self.fish_details()


# f = PredatoryFish("Fish Name", 9)
# print(f.show_fish_details())
