from project.robots.base_robot import BaseRobot


class FemaleRobot(BaseRobot):
    TYPE = "FemaleRobot"
    FEMALE_ROBOT_WEIGHT = 7

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, weight=self.FEMALE_ROBOT_WEIGHT)

    def eating(self):
        self.weight += 1
