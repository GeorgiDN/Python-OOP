from project.band_members.musician import Musician


class Guitarist(Musician):
    ALLOWED_SKILLS = ["play metal",
                      "play rock",
                      "play jazz"
                      ]
    TYPE = "Guitarist"

    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def learn_new_skill(self, new_skill: str):
        return self.take_skill(new_skill)
