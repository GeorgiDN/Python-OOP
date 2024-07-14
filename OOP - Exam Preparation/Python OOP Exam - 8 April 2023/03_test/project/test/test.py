from project.tennis_player import TennisPlayer
from unittest import TestCase, main


class TestTennisPlayer(TestCase):
    def setUp(self):
        self.player = TennisPlayer("Gosho", 20, 100.0)

    def test_init(self):
        self.assertEqual(self.player.name, "Gosho")
        self.assertEqual(self.player.age, 20)
        self.assertEqual(self.player.points, 100.0)

    def test_name_with_empty_string_raise_valueerror(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = ''
        message = "Name should be more than 2 symbols!"
        self.assertEqual(str(ve.exception), message)

    def test_name_with_len_name_equal_to_one_raise_valueerror(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = 'g'
        message = "Name should be more than 2 symbols!"
        self.assertEqual(str(ve.exception), message)

    def test_name_with_len_name_equal_to_two_raise_valueerror(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = 'Go'
        message = "Name should be more than 2 symbols!"
        self.assertEqual(str(ve.exception), message)

    def test_name_with_valid_name(self):
        self.player.name = 'Gosho'
        self.assertEqual(self.player.name, 'Gosho')

    def test_age_equal_to_zero_raise_valueerror(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 0
        message = "Players must be at least 18 years of age!"
        self.assertEqual(str(ve.exception), message)

    def test_negative_age_raise_valueerror(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = -1
        message = "Players must be at least 18 years of age!"
        self.assertEqual(str(ve.exception), message)

    def test_age_below_18_raise_valueerror(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 17
        message = "Players must be at least 18 years of age!"
        self.assertEqual(str(ve.exception), message)

    def test_age_equal_18(self):
        self.player.age = 18
        self.assertEqual(self.player.age, 18)

    def test_add_new_win_with_already_added_tournament_name(self):
        self.player.add_new_win("Tournament1")
        self.assertEqual(self.player.wins, ["Tournament1"])
        result = self.player.add_new_win("Tournament1")
        message = "Tournament1 has been already added to the list of wins!"
        self.assertEqual(result, message)

    def test_add_new_win_with_not_existing_tournament_name(self):
        self.player.add_new_win("Tournament1")
        self.assertEqual(self.player.wins, ["Tournament1"])

    def test_less_than_method_with_points_less_than_other(self):
        self.other_player = TennisPlayer("Ivan", 21, 110.0)
        result = self.player.__lt__(self.other_player)
        message = f'{self.other_player.name} is a top seeded player and he/she is better than {self.player.name}'
        self.assertEqual(result, message)

    def test_less_than_method_with_points_equal_than_other(self):
        self.other_player = TennisPlayer("Ivan", 21, 100.0)
        result = self.player.__lt__(self.other_player)
        message = f'{self.player.name} is a better player than {self.other_player.name}'
        self.assertEqual(result, message)

    def test_less_than_method_with_points_greater_than_other(self):
        self.other_player = TennisPlayer("Ivan", 21, 95.0)
        result = self.player.__lt__(self.other_player)
        message = f'{self.player.name} is a better player than {self.other_player.name}'
        self.assertEqual(result, message)

    def test_str_method(self):
        self.player.add_new_win("Tournament1")
        self.player.add_new_win("Tournament2")

        expected = f"Tennis Player: {self.player.name}\n" \
                   f"Age: {self.player.age}\n" \
                   f"Points: {self.player.points:.1f}\n" \
                   f"Tournaments won: {', '.join(self.player.wins)}"

        result = self.player.__str__()
        self.assertEqual(result, expected)


if __name__ == '__main__':
    main()


