from abc import ABC, abstractmethod


class Animal(ABC):
    SOUND = ''

    def __init__(self, name, age, gender):
        self.name = name
        self.age = age
        self.gender = gender

    @abstractmethod
    def __repr__(self):
        pass

    def make_sound(self):
        return self.SOUND
