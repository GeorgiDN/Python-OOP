from project.astronaut.astronaut import Astronaut


class Meteorologist(Astronaut):
    OXYGEN = 90
    BREATH_UNIT = 15

    def __init__(self, name):
        super().__init__(name, self.OXYGEN)

    def breathe(self):
        self.oxygen -= self.BREATH_UNIT
