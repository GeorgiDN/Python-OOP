from project.animal import Animal


class Cat(Animal):
    SOUND = "Meow meow!"

    def __init__(self, name, age, gender):
        super().__init__(name, age, gender)

    def get_animal_info(self):
        return self.__repr__()
