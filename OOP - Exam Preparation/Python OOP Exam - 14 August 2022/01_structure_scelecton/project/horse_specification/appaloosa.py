from project.horse_specification.horse import Horse


class Appaloosa(Horse):
    HORSE_MAX_SPEED: int = 120
    SPEED_INCREMENT: int = 2
    TYPE = "Appaloosa"

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        return self.train_horse()
