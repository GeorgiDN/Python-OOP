from project.astronaut.astronaut import Astronaut


class Biologist(Astronaut):
    OXYGEN = 70
    BREATH_UNIT = 5

    def __init__(self, name):
        super().__init__(name, self.OXYGEN)

    def breathe(self):
        self.oxygen -= self.BREATH_UNIT
