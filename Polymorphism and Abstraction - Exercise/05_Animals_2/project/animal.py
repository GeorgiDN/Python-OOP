from abc import ABC, abstractmethod


class Animal(ABC):
    SOUND = ''

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def get_animal_info(self):
        pass

    def __repr__(self):
        return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {self.__class__.__name__}"
        # return f"This is {self.name}. {self.name} is a {self.age} year old {self.gender} {type(self).__name__}"

    def make_sound(self):
        return self.SOUND
