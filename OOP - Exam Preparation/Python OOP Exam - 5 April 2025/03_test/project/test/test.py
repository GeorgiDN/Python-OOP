from unittest import TestCase, main
from project.star_system import StarSystem


class StarSystemTest(TestCase):
    def setUp(self):
        self.star_system = StarSystem('system', 'Red giant', 'Single', 2)

    def test_init(self):
        self.assertIsInstance(self.star_system, StarSystem)
        self.assertEqual(self.star_system.name, 'system')
        self.assertEqual(self.star_system.star_type, 'Red giant')
        self.assertEqual(self.star_system.system_type, 'Single')
        self.assertEqual(self.star_system.num_planets, 2)
        self.assertEqual(self.star_system.habitable_zone_range, None)

    def test_test_is_habitable_return_false(self):
        res = self.star_system.is_habitable
        self.assertFalse(res)

    def test_test_is_habitable_return_true(self):
        self.star_system.habitable_zone_range = (3, 4)
        self.assertEqual(self.star_system.habitable_zone_range, (3, 4))
        res = self.star_system.is_habitable
        self.assertTrue(res)

    def test_name_with_empty_string_raise_error(self):
        with self.assertRaises(ValueError) as ve:
            self.star_system.name = ''
        msg = 'Name must be a non-empty string.'
        self.assertEqual(str(ve.exception), msg)

    def test_star_type_with_invalid_value(self):
        with self.assertRaises(ValueError) as ve:
            self.star_system.star_type = 'invalid'
        msg = f"Star type must be one of {sorted(self.star_system._STAR_TYPES)}."
        self.assertEqual(str(ve.exception), msg)

    def test_system_type_with_invalid_value(self):
        with self.assertRaises(ValueError) as ve:
            self.star_system.system_type = 'invalid'
        msg = f"System type must be one of {sorted(self.star_system._STAR_SYSTEM_TYPES)}."
        self.assertEqual(str(ve.exception), msg)

    def test_num_planets_with_negative_value(self):
        with self.assertRaises(ValueError) as ve:
            self.star_system.num_planets = -1
        msg = "Number of planets must be a non-negative integer."
        self.assertEqual(str(ve.exception), msg)

    def test_habitable_zone_range_with_len_equal_to_one(self):
        with self.assertRaises(ValueError) as ve:
            self.star_system.habitable_zone_range = (3,)
        msg = "Habitable zone range must be a tuple of two numbers (start, end) where start < end."
        self.assertEqual(str(ve.exception), msg)

    def test_habitable_zone_range_with_len_equal_to_three(self):
        with self.assertRaises(ValueError) as ve:
            self.star_system.habitable_zone_range = (3, 4, 5)
        msg = "Habitable zone range must be a tuple of two numbers (start, end) where start < end."
        self.assertEqual(str(ve.exception), msg)

    def test_habitable_zone_range_with_first_value_greater_than_second(self):
        with self.assertRaises(ValueError) as ve:
            self.star_system.habitable_zone_range = (5, 4)
        msg = "Habitable zone range must be a tuple of two numbers (start, end) where start < end."
        self.assertEqual(str(ve.exception), msg)

    def test_greater_than_method_with_both_systems_is_habitable_empty(self):
        self.other_system = StarSystem('other', 'Blue giant', 'Binary', 4)
        with self.assertRaises(ValueError) as ve:
            self.star_system.__gt__(self.other_system)
        msg = "Comparison not possible: One or both systems lack a defined habitable zone or planets."
        self.assertEqual(str(ve.exception), msg)

    def test_greater_than_method_with_self_systems_is_habitable_empty(self):
        self.star_system.habitable_zone_range = (3, 4)
        self.other_system = StarSystem('other', 'Blue giant', 'Binary', 4)
        with self.assertRaises(ValueError) as ve:
            self.star_system.__gt__(self.other_system)
        msg = "Comparison not possible: One or both systems lack a defined habitable zone or planets."
        self.assertEqual(str(ve.exception), msg)

    def test_greater_than_method_with_other_systems_is_habitable_empty(self):
        self.other_system = StarSystem('other', 'Blue giant', 'Binary', 4)
        self.other_system.habitable_zone_range = (3, 4)
        with self.assertRaises(ValueError) as ve:
            self.star_system.__gt__(self.other_system)
        msg = "Comparison not possible: One or both systems lack a defined habitable zone or planets."
        self.assertEqual(str(ve.exception), msg)

    def test_greate_than_method_return_false(self):
        self.other_system = StarSystem('other', 'Blue giant', 'Binary', 4)
        self.other_system.habitable_zone_range = (3, 5)
        self.star_system.habitable_zone_range = (5, 6)
        res = self.star_system.__gt__(self.other_system)
        self.assertFalse(res)

    def test_greate_than_method_return_false_with_equal_values(self):
        self.other_system = StarSystem('other', 'Blue giant', 'Binary', 4)
        self.other_system.habitable_zone_range = (3, 4)
        self.star_system.habitable_zone_range = (5, 6)
        res = self.star_system.__gt__(self.other_system)
        self.assertFalse(res)

    def test_greate_than_method_return_true(self):
        self.other_system = StarSystem('other', 'Blue giant', 'Binary', 4)
        self.other_system.habitable_zone_range = (3, 4)
        self.star_system.habitable_zone_range = (5, 7)
        res = self.star_system.__gt__(self.other_system)
        self.assertTrue(res)

    def test_compare_star_systems_first_has_a_wider_habitable_zone(self):
        other_system = StarSystem('other', 'Blue giant', 'Binary', 4)
        other_system.habitable_zone_range = (3, 4)
        star_system = StarSystem('system', 'Red giant', 'Single', 2)
        star_system.habitable_zone_range = (5, 7)
        res = StarSystem.compare_star_systems(star_system, other_system)
        msg = f"{star_system.name} has a wider habitable zone than {other_system.name}."
        self.assertEqual(res, msg)

    def test_compare_star_systems_second_has_a_wider_habitable_zone(self):
        other_system = StarSystem('other', 'Blue giant', 'Binary', 4)
        other_system.habitable_zone_range = (3, 6)
        star_system = StarSystem('system', 'Red giant', 'Single', 2)
        star_system.habitable_zone_range = (5, 7)
        res = StarSystem.compare_star_systems(star_system, other_system)
        msg = f"{other_system.name} has a wider or equal habitable zone compared to {star_system.name}."
        self.assertEqual(res, msg)

    def test_compare_star_systems_with_equal_sums_of_habitable_zone(self):
        other_system = StarSystem('other', 'Blue giant', 'Binary', 4)
        other_system.habitable_zone_range = (3, 6)
        star_system = StarSystem('system', 'Red giant', 'Single', 2)
        star_system.habitable_zone_range = (5, 8)
        res = StarSystem.compare_star_systems(star_system, other_system)
        msg = f"{other_system.name} has a wider or equal habitable zone compared to {star_system.name}."
        self.assertEqual(res, msg)

    def test_compare_star_systems_both_no_have_habitable_zone_and_planets(self):
        star_system = StarSystem("Polaris", "Red giant", "Single", 0, None)
        other_system = StarSystem("Antares", "Blue giant", "Binary", 0, None)
        result = StarSystem.compare_star_systems(star_system, other_system)
        self.assertEqual(result, "Comparison not possible: One or both systems lack a defined habitable zone or planets.")

    # WITHOUT these test 100/100 again
    def test_compare_star_systems_both_no_have_habitable_zone(self):
        star_system = StarSystem("Polaris", "Red giant", "Single", 2, None)
        other_system = StarSystem("Antares", "Blue giant", "Binary", 3, None)
        result = StarSystem.compare_star_systems(star_system, other_system)
        self.assertEqual(result, "Comparison not possible: One or both systems lack a defined habitable zone or planets.")

    def test_greater_than_method_with_zero_num_of_planets(self):
        self.other_system = StarSystem('other', 'Blue giant', 'Binary', 0)
        self.other_system.habitable_zone_range = (3, 4)
        self.star_system.num_planets = 0
        self.star_system.habitable_zone_range = (5, 7)
        with self.assertRaises(ValueError) as ve:
            self.star_system.__gt__(self.other_system)
        msg = "Comparison not possible: One or both systems lack a defined habitable zone or planets."
        self.assertEqual(str(ve.exception), msg)


if __name__ == '__main__':
    main()
