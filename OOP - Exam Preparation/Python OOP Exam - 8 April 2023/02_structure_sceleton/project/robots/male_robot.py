from project.robots.base_robot import BaseRobot


class MaleRobot(BaseRobot):
    TYPE = 'MaleRobot'
    MALE_ROBOT_WEIGHT = 9

    def __init__(self, name: str, kind: str, price: float):
        super().__init__(name, kind, price, weight=self.MALE_ROBOT_WEIGHT)

    def eating(self):
        self.weight += 3
