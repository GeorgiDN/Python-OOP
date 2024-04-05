from project.cat import Cat


class Tomcat(Cat):
    SOUND = "Hiss"

    def __init__(self, name, age):
        super().__init__(name, age, "Male")
