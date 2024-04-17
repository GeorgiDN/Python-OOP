from project.cat import Cat

from unittest import TestCase, main


class CatTests(TestCase):
    def setUp(self):
        self.cat = Cat("Pisana")

    def test_01_initialization(self):
        self.assertEqual("Pisana", self.cat.name)
        self.assertEqual(False, self.cat.fed)
        self.assertEqual(False, self.cat.sleepy)
        self.assertEqual(0, self.cat.size)

    def test_02_eat_method_with_already_fed_raise_exception(self):
        self.cat.fed = True
        with self.assertRaises(Exception) as ex:
            self.cat.eat()
        self.assertEqual('Already fed.', str(ex.exception))

    def test_03_eat_set_fed_and_sleepy_true_and_increase_size(self):
        expected_size = 1
        self.cat.eat()
        self.assertEqual(self.cat.fed, True)
        self.assertEqual(self.cat.sleepy, True)
        self.assertEqual(self.cat.size, expected_size)

    def test_04_sleep_when_the_cat_is_not_fed_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.cat.sleep()
        self.assertEqual('Cannot sleep while hungry', str(ex.exception))

    def test_05_sleep_when_the_cat_is_fed(self):
        self.cat.eat()
        self.cat.sleep()
        self.assertEqual(False, self.cat.sleepy)


if __name__ == '__main__':
    main()
