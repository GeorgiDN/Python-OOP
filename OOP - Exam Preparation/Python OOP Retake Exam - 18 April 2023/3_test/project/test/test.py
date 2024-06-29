from project.robot import Robot
from unittest import TestCase, main


class TestRobot(TestCase):
    def setUp(self):
        self.robot = Robot('1', 'Military', 10, 10)

    def test_init(self):
        self.assertIsInstance(self.robot, Robot)
        self.assertEqual(self.robot. robot_id, '1')
        self.assertEqual(self.robot. category, 'Military')
        self.assertEqual(self.robot. available_capacity, 10)
        self.assertEqual(self.robot. price, 10)
        self.assertEqual(self.robot.hardware_upgrades, [])
        self.assertEqual(self.robot.software_updates, [])

    def test_invalid_category_raise_valueerror(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.category = 'invalid'
        message = f"Category should be one of '{self.robot.ALLOWED_CATEGORIES}'"
        self.assertEqual(str(ve.exception), message)

    def test_valid_category(self):
        self.robot.category = 'Military'
        self.assertEqual(self.robot.category, 'Military')

    def test_valid_category2(self):
        self.robot.category = 'Education'
        self.assertEqual(self.robot.category, 'Education')

    def test_valid_category3(self):
        self.robot.category = 'Entertainment'
        self.assertEqual(self.robot.category, 'Entertainment')

    def test_valid_category4(self):
        self.robot.category = 'Humanoids'
        self.assertEqual(self.robot.category, 'Humanoids')

    def test_price_with_negative_value(self):
        with self.assertRaises(ValueError) as ve:
            self.robot.price = -1
        message = "Price cannot be negative!"
        self.assertEqual(str(ve.exception), message)

    def test_price_with_positive_value(self):
        self.robot.price = 10
        self.assertEqual(self.robot.price, 10)

    def test_price_with_zero_value(self):
        self.robot.price = 0
        self.assertEqual(self.robot.price, 0)

    def test_upgrade_hardware_component_in_hardware_upgrades_not_upgrated(self):
        self.robot.hardware_upgrades = ['part1']
        res = self.robot.upgrade('part1', 2.0)
        message = f"Robot {self.robot.robot_id} was not upgraded."
        self.assertEqual(res, message)

    def test_upgrade_hardware_component_not_in_hardware_upgrade_successful(self):
        res = self.robot.upgrade('part1', 2.0)
        message = f"Robot {self.robot.robot_id} was upgraded with part1."
        self.assertEqual(res, message)
        self.assertEqual(self.robot.hardware_upgrades, ['part1'])
        self.assertEqual(self.robot.price, 13.0)  # 10 + (2 * 1.5)

    def test_update_with_software_updates_and_version_less_than_max_software_updates_not_updated(self):
        self.robot.software_updates = [1.0, 2.0]
        res = self.robot.update(1.0, 5)
        message = f"Robot {self.robot.robot_id} was not updated."
        self.assertEqual(res, message)

    def test_update_with_software_updates_and_version_equal_to_max_software_updates_not_updated(self):
        self.robot.software_updates = [1.0, 2.0]
        res = self.robot.update(2.0, 5)
        message = f"Robot {self.robot.robot_id} was not updated."
        self.assertEqual(res, message)

    def test_update_with_software_updates_available_capacity_less_than_needed_capacity(self):
        self.robot.software_updates = [1.0, 2.0]
        res = self.robot.update(3.0, 11)
        message = f"Robot {self.robot.robot_id} was not updated."
        self.assertEqual(res, message)

    def test_update_successful(self):
        self.robot.software_updates = [1.0, 2.0]
        res = self.robot.update(3.0, 2)
        message = f'Robot {self.robot.robot_id} was updated to version 3.0.'
        self.assertEqual(res, message)
        self.assertEqual(self.robot.available_capacity, 8)
        self.assertEqual(self.robot.software_updates, [1.0, 2.0, 3.0])

    def test_gt_method_price_greater_than_other_price(self):
        self.other = Robot('2', 'Education', 10, 9)
        res = self.robot.__gt__(self.other)
        message = f'Robot with ID {self.robot.robot_id} is more expensive than Robot with ID {self.other.robot_id}.'
        self.assertEqual(res, message)

    def test_gt_method_price_equal_to_other_price(self):
        self.other = Robot('2', 'Education', 10, 10)
        res = self.robot.__gt__(self.other)
        message = f'Robot with ID {self.robot.robot_id} costs equal to Robot with ID {self.other.robot_id}.'
        self.assertEqual(res, message)

    def test_gt_method_price_less_than_other_price(self):
        self.other = Robot('2', 'Education', 10, 11)
        res = self.robot.__gt__(self.other)
        message = f'Robot with ID {self.robot.robot_id} is cheaper than Robot with ID {self.other.robot_id}.'
        self.assertEqual(res, message)


if __name__ == '__main__':
    main()

