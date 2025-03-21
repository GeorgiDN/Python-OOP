from project.team import Team
from unittest import TestCase, main


class TestTeam(TestCase):
    def setUp(self):
        self.team = Team('team')

    def test_init(self):
        self.assertEqual(self.team.name, 'team')
        self.assertEqual(self.team.members, {})

    def test_invalid_team_name(self):
        with self.assertRaises(ValueError) as ex:
            self.team.name = "Team123"  # Invalid name (contains numbers)
        self.assertEqual(str(ex.exception), "Team Name can contain only letters!")

    def test_add_member(self):
        res = self.team.add_member(ivan=20, gosho=30)
        self.assertEqual(self.team.members, {'ivan': 20, 'gosho': 30})
        msg = "Successfully added: ivan, gosho"
        self.assertEqual(res, msg)

    def test_add_member_with_no_arguments(self):
        res = self.team.add_member()
        self.assertEqual(self.team.members, {})
        self.assertEqual(res, "Successfully added: ")

    def test_add_member_with_existing_members(self):
        self.team.add_member(ivan=20, gosho=30)
        res = self.team.add_member(ivan=20, gosho=30)
        self.assertEqual(self.team.members, {'ivan': 20, 'gosho': 30})
        msg = "Successfully added: "
        self.assertEqual(res, msg)

    def test_remove_member(self):
        self.team.add_member(ivan=20, gosho=30)
        res = self.team.remove_member('ivan')
        self.assertEqual(self.team.members, {'gosho': 30})
        msg = f"Member ivan removed"
        self.assertEqual(res, msg)

    def test_remove_member_with_non_existing_member(self):
        self.team.add_member(ivan=20, gosho=30)
        res = self.team.remove_member('invalid')
        msg = f"Member with name invalid does not exist"
        self.assertEqual(res, msg)

    def test_greater_than_method_return_false(self):
        self.other_team = Team('otherteam')
        self.team.add_member(ivan=20)
        self.other_team.add_member(ivan=20, gosho=30)
        res = self.team.__gt__(self.other_team)
        self.assertFalse(res)

    def test_greater_than_method_with_equal_length_return_false(self):
        self.other_team = Team('otherteam')
        self.team.add_member(ivan=20, gosho=30)
        self.other_team.add_member(ivan=20, gosho=30)
        res = self.team.__gt__(self.other_team)
        self.assertFalse(res)
        self.assertTrue(len(self.team.members) > len(self.other_team.members))

    def test_greater_than_method_return_true(self):
        self.other_team = Team('otherteam')
        self.team.add_member(ivan=20, gosho=30, pesho=40)
        self.other_team.add_member(dragan=20, petkan=30)
        res = self.team.__gt__(self.other_team)
        self.assertTrue(res)
        self.assertTrue(len(self.team.members) > len(self.other_team.members))

    def test_gt_by_len_of_team_members_self_return_true(self):
        self.team.add_member(ivan=20)
        self.team.add_member(gosho=30)

        other = Team("Other")
        other.add_member(pesho=40)
        result = self.team > other
        self.assertEqual(True, result)
        self.assertTrue(len(self.team.members) > len(other.members))

    def test_len_method(self):
        self.team.add_member(ivan=20, gosho=30)
        res = self.team.__len__()
        self.assertEqual(res, 2)

    def test_len_method_on_empty_team(self):
        res = len(self.team)
        self.assertEqual(res, 0)

    def test_add_method(self):
        self.other_team = Team('otherteam')
        self.team.add_member(ivan=20)
        self.other_team.add_member(gosho=30, pesho=40)

        res = self.team.__add__(self.other_team)  # Creates a new team

        expected = "Team name: teamotherteam\n" \
                   "Member: pesho - 40-years old\n" \
                   "Member: gosho - 30-years old\n" \
                   "Member: ivan - 20-years old"

        self.assertEqual(str(res), expected)

    def test_str_method(self):
        self.team.add_member(ivan=20, gosho=30, pesho=40)
        res = self.team.__str__()
        expected = "Team name: team\n" \
                   "Member: pesho - 40-years old\n" \
                   "Member: gosho - 30-years old\n" \
                   "Member: ivan - 20-years old"

        self.assertEqual(str(res), expected)


if __name__ == '__main__':
    main()
