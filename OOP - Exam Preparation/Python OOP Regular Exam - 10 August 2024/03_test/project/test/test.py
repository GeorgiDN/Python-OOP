from project.soccer_player import SoccerPlayer
from unittest import TestCase, main


class TestSoccerPlayer(TestCase):
    def setUp(self):
        self.player = SoccerPlayer("Ivancho", 20, 5, "Barcelona")

    def test_init(self):
        self.assertIsInstance(self.player, SoccerPlayer)
        self.assertEqual(self.player.name, "Ivancho")
        self.assertEqual(self.player.age, 20)
        self.assertEqual(self.player.goals, 5)
        self.assertEqual(self.player.team, "Barcelona")
        self.assertEqual(self.player.achievements, {})

    def test_name_with_not_valid_len_raise_error_empty_string(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = ""
        mes = "Name should be more than 5 symbols!"
        self.assertEqual(str(ve.exception), mes)

    def test_name_with_not_valid_len_raise_error_len_1(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = "I"
        mes = "Name should be more than 5 symbols!"
        self.assertEqual(str(ve.exception), mes)

    def test_name_with_not_valid_len_raise_error_len_2(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = "Iv"
        mes = "Name should be more than 5 symbols!"
        self.assertEqual(str(ve.exception), mes)

    def test_name_with_not_valid_len_raise_error_len_3(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = "Iva"
        mes = "Name should be more than 5 symbols!"
        self.assertEqual(str(ve.exception), mes)

    def test_name_with_not_valid_len_raise_error_len_4(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = "Ivan"
        mes = "Name should be more than 5 symbols!"
        self.assertEqual(str(ve.exception), mes)

    def test_name_with_not_valid_len_raise_error_len_5(self):
        with self.assertRaises(ValueError) as ve:
            self.player.name = "Ivanc"
        mes = "Name should be more than 5 symbols!"
        self.assertEqual(str(ve.exception), mes)

    def test_name_proper(self):
        self.player.name = "Ivancho"
        self.assertEqual(self.player.name, "Ivancho")

    def test_age_raise_error_negative_age(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = -1
        mes = "Players must be at least 16 years of age!"
        self.assertEqual(str(ve.exception), mes)

    def test_age_raise_error_age_0(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 0
        mes = "Players must be at least 16 years of age!"
        self.assertEqual(str(ve.exception), mes)

    def test_age_raise_error_age_15(self):
        with self.assertRaises(ValueError) as ve:
            self.player.age = 15
        mes = "Players must be at least 16 years of age!"
        self.assertEqual(str(ve.exception), mes)

    def test_age_min_age_allowed(self):
        self.player.age = 16
        self.assertEqual(self.player.age, 16)

    def test_goals_with_negative_value(self):
        self.player.goals = -1
        self.assertEqual(self.player.goals, 0)

    def test_goals_with_zero_value(self):
        self.player.goals = 0
        self.assertEqual(self.player.goals, 0)

    def test_goals_with_positive_value(self):
        self.player.goals = 1
        self.assertEqual(self.player.goals, 1)

    def test_team_with_invalid_team_name(self):
        with self.assertRaises(ValueError) as ve:
            self.player.team = "Invalid"
        mes = "Team must be one of the following: Barcelona, Real Madrid, Manchester United, Juventus, PSG!"
        self.assertEqual(str(ve.exception), mes)

    def test_team_name_with_proper_name_real(self):
        self.player.team = "Real Madrid"
        self.assertEqual(self.player.team, "Real Madrid")

    def test_team_name_with_proper_name_manchester(self):
        self.player.team = "Manchester United"
        self.assertEqual(self.player.team, "Manchester United")

    def test_team_name_with_proper_name_juventus(self):
        self.player.team = "Juventus"
        self.assertEqual(self.player.team, "Juventus")

    def test_team_name_with_proper_name_PSG(self):
        self.player.team = "PSG"
        self.assertEqual(self.player.team, "PSG")

    def test_change_team_with_invalid_team(self):
        res = self.player.change_team("Invalid")
        mes = "Invalid team name!"
        self.assertEqual(res, mes)
        self.assertEqual(self.player.team, "Barcelona")

    def test_change_team_with_valid_team(self):
        res = self.player.change_team("PSG")
        mes = "Team successfully changed!"
        self.assertEqual(res, mes)
        self.assertEqual(self.player.team, "PSG")

    def test_add_new_achievement_with_not_added_data_yet(self):
        res = self.player.add_new_achievement("achievement1")
        mes = "achievement1 has been successfully added to the achievements collection!"
        self.assertEqual(res, mes)
        self.assertEqual(self.player.achievements, {"achievement1": 1})

    def test_add_new_achievement_with_added_data_and_same_achievment_again(self):
        self.player.add_new_achievement("achievement1")
        res = self.player.add_new_achievement("achievement1")
        mes = "achievement1 has been successfully added to the achievements collection!"
        self.assertEqual(res, mes)
        self.assertEqual(self.player.achievements, {"achievement1": 2})

    def test_add_new_achievement_with_added_data_and_new_achievment(self):
        self.player.add_new_achievement("achievement1")
        self.player.add_new_achievement("achievement2")
        res = self.player.add_new_achievement("achievement2")
        mes = "achievement2 has been successfully added to the achievements collection!"
        self.assertEqual(res, mes)
        self.assertEqual(self.player.achievements, {"achievement1": 1, "achievement2": 2})

    def test_lt_method_with_other_player_have_more_goals(self):
        other = SoccerPlayer("Dragancho", 21, 6,  "PSG")
        res = self.player.__lt__(other)
        mes = f"{other.name} is a top goal scorer! S/he scored more than {self.player.name}."
        self.assertEqual(res, mes)

    def test_lt_method_with_other_player_have_less_goals(self):
        other = SoccerPlayer("Dragancho", 21, 4,  "PSG")
        res = self.player.__lt__(other)
        mes = f"{self.player.name} is a better goal scorer than {other.name}."
        self.assertEqual(res, mes)

    def test_lt_method_with_other_player_have_same_goals(self):
        other = SoccerPlayer("Dragancho", 21, 5,  "PSG")
        res = self.player.__lt__(other)
        mes = f"{self.player.name} is a better goal scorer than {other.name}."
        self.assertEqual(res, mes)


if __name__ == '__main__':
    main()

