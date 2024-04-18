from project.mammal import Mammal

from unittest import TestCase, main


class MammalTest(TestCase):
    def setUp(self):
        self.mammal = Mammal("Reks", "dog", "bau" )

    def test_initializing(self):
        self.assertEqual("Reks", self.mammal.name)
        self.assertEqual("dog", self.mammal.type)
        self.assertEqual("bau", self.mammal.sound)
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_make_sound(self):
        self.assertEqual(f"{self.mammal.name} makes {self.mammal.sound}", self.mammal.make_sound())

    def test_get_kingdom(self):
        self.assertEqual("animals", self.mammal.get_kingdom())

    def test_info(self):
        self.assertEqual(f"{self.mammal.name} is of type {self.mammal.type}", self.mammal.info())


if __name__ == "__main__":
    main()
