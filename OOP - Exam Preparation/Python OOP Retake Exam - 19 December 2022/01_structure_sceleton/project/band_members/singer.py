from project.band_members.musician import Musician


class Singer(Musician):
    ALLOWED_SKILLS = ["sing high pitch notes", "sing low pitch notes"]
    TYPE = "Singer"

    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def learn_new_skill(self, new_skill: str):
        return self.take_skill(new_skill)
