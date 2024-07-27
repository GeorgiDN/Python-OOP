from project.horse_specification.horse import Horse


class Thoroughbred(Horse):
    HORSE_MAX_SPEED: int = 140
    SPEED_INCREMENT: int = 3
    TYPE = "Thoroughbred"

    def __init__(self, name: str, speed: int):
        super().__init__(name, speed)

    def train(self):
        return self.train_horse()

