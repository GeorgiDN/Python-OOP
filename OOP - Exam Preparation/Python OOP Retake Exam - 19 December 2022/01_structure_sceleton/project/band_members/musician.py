from abc import ABC, abstractmethod


class Musician(ABC):
    ALLOWED_SKILLS = []

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        self.skills: list = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Musician name cannot be empty!")
        self.__name = value

    @property
    def age(self):
        return self.__age

    @age.setter
    def age(self, value):
        if value < 16:
            raise ValueError("Musicians should be at least 16 years old!")
        self.__age = value

    @abstractmethod
    def learn_new_skill(self, new_skill: str):
        pass

    def take_skill(self, new_skill):
        if new_skill not in self.ALLOWED_SKILLS:
            raise ValueError(f"{new_skill} is not a needed skill!")
        elif new_skill in self.skills:
            raise Exception(f"{new_skill} is already learned!")
        else:
            self.skills.append(new_skill)
            return f"{self.name} learned to {new_skill}."


# m = Musician("musician", 17)
# print(m.take_skill("sing high pitch notes"))
# print(m.skills)
# print(m.take_skill("sing high pitch note"))
