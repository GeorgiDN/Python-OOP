from project.band_members.musician import Musician


class Drummer(Musician):
    ALLOWED_SKILLS = ["play the drums with drumsticks",
                      "play the drums with drum brushes",
                      "read sheet music"
                      ]
    TYPE = "Drummer"

    def __init__(self, name: str, age: int):
        super().__init__(name, age)

    def learn_new_skill(self, new_skill: str):
        return self.take_skill(new_skill)
