from project.astronaut.astronaut import Astronaut


class Geodesist(Astronaut):
    OXYGEN = 50
    BREATH_UNIT = 10

    def __init__(self, name):
        super().__init__(name, self.OXYGEN)

    def breathe(self):
        self.oxygen -= self.BREATH_UNIT
