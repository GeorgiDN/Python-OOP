from project.climbing_robot import ClimbingRobot
from unittest import TestCase, main


class ClimbingRobotTest(TestCase):

    def test_01_init(self):
        climbing_robot = ClimbingRobot("Mountain", "Part1", 100, 200)
        self.assertEqual(climbing_robot.category, "Mountain")
        self.assertEqual(climbing_robot.part_type, "Part1")
        self.assertEqual(climbing_robot.capacity, 100)
        self.assertEqual(climbing_robot.memory, 200)
        self.assertEqual([], climbing_robot.installed_software)

    def test_02_category_raise_message(self):
        with self.assertRaises(ValueError) as ve:
            climbing_robot = ClimbingRobot("USA", "Part1", 100, 200)
        expected_message = "Category should be one of ['Mountain', 'Alpine', 'Indoor', 'Bouldering']"
        output = str(ve.exception)
        self.assertEqual(output, expected_message)

    def test_03_category_setter_mountain(self):
        climbing_robot = ClimbingRobot("Mountain", "Part1", 100, 200)
        self.assertEqual(climbing_robot.category, "Mountain")

    def test_04_category_setter_alpine(self):
        climbing_robot = ClimbingRobot("Alpine", "Part1", 100, 200)
        self.assertEqual(climbing_robot.category, "Alpine")

    def test_05_category_setter_indoor(self):
        climbing_robot = ClimbingRobot("Indoor", "Part1", 100, 200)
        self.assertEqual(climbing_robot.category, "Indoor")

    def test_06_category_setter_bouldering(self):
        climbing_robot = ClimbingRobot("Bouldering", "Part1", 100, 200)
        self.assertEqual(climbing_robot.category, "Bouldering")

    def test_07_get_used_capacity(self):
        climbing_robot = ClimbingRobot("Mountain", "Part1", 100, 200)
        software1 = {'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 50}
        software2 = {'name': 'Software2', 'capacity_consumption': 40, 'memory_consumption': 70}
        climbing_robot.install_software(software1)
        climbing_robot.install_software(software2)
        res = climbing_robot.get_used_capacity()
        output = 70
        self.assertEqual(res, output)

    def test_08_get_available_capacity(self):
        climbing_robot = ClimbingRobot("Mountain", "Part1", 100, 200)
        software1 = {'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 50}
        climbing_robot.install_software(software1)
        res = climbing_robot.get_available_capacity()
        output = 70
        self.assertEqual(res, output)

    def test_09_get_available_memory(self):
        climbing_robot = ClimbingRobot("Mountain", "Part1", 100, 200)
        software1 = {'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 50}
        climbing_robot.install_software(software1)
        res = climbing_robot.get_available_memory()
        output = 150
        self.assertEqual(res, output)

    def test_10_get_used_memory(self):
        climbing_robot = ClimbingRobot("Mountain", "Part1", 100, 200)
        software1 = {'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 50}
        software2 = {'name': 'Software2', 'capacity_consumption': 40, 'memory_consumption': 70}
        climbing_robot.install_software(software1)
        climbing_robot.install_software(software2)
        res = climbing_robot.get_used_memory()
        output = 120
        self.assertEqual(res, output)

    def test_11_install_software_with_not_enough_capacity(self):
        climbing_robot = ClimbingRobot("Mountain", "Part1", 10, 200)
        software1 = {'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 50}
        res = climbing_robot.install_software(software1)
        expected_message = "Software 'Software1' cannot be installed on Mountain part."
        self.assertEqual([], climbing_robot.installed_software)
        self.assertEqual(res, expected_message)

    def test_12_install_software_with_not_enough_memory(self):
        climbing_robot = ClimbingRobot("Mountain", "Part1", 100, 20)
        software1 = {'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 50}
        res = climbing_robot.install_software(software1)
        expected_message = "Software 'Software1' cannot be installed on Mountain part."
        self.assertEqual([], climbing_robot.installed_software)
        self.assertEqual(res, expected_message)

    def test_13_install_software_with_equal_capacity(self):
        climbing_robot = ClimbingRobot("Mountain", "Part1", 100, 200)
        software1 = {'name': 'Software1', 'capacity_consumption': 100, 'memory_consumption': 50}
        res = climbing_robot.install_software(software1)
        expected_message = f"Software 'Software1' successfully installed on Mountain part."
        self.assertEqual(res, expected_message)
        self.assertEqual([{'name': 'Software1', 'capacity_consumption': 100, 'memory_consumption': 50}],
                          climbing_robot.installed_software)

    def test_14_install_software_with_more_capacity(self):
        climbing_robot = ClimbingRobot("Mountain", "Part1", 100, 200)
        software1 = {'name': 'Software1', 'capacity_consumption': 10, 'memory_consumption': 50}
        res = climbing_robot.install_software(software1)
        expected_message = f"Software 'Software1' successfully installed on Mountain part."
        self.assertEqual(res, expected_message)
        self.assertEqual([{'name': 'Software1', 'capacity_consumption': 10, 'memory_consumption': 50}],
                         climbing_robot.installed_software)

    def test_15_install_software_with_equal_memory(self):
        climbing_robot = ClimbingRobot("Mountain", "Part1", 100, 200)
        software1 = {'name': 'Software1', 'capacity_consumption': 10, 'memory_consumption': 200}
        res = climbing_robot.install_software(software1)
        expected_message = f"Software 'Software1' successfully installed on Mountain part."
        self.assertEqual(res, expected_message)
        self.assertEqual([{'name': 'Software1', 'capacity_consumption': 10, 'memory_consumption': 200}],
                          climbing_robot.installed_software)

    def test_16_install_software_with_more_memory(self):
        climbing_robot = ClimbingRobot("Mountain", "Part1", 100, 200)
        software1 = {'name': 'Software1', 'capacity_consumption': 10, 'memory_consumption': 20}
        res = climbing_robot.install_software(software1)
        expected_message = f"Software 'Software1' successfully installed on Mountain part."
        self.assertEqual(res, expected_message)
        self.assertEqual([{'name': 'Software1', 'capacity_consumption': 10, 'memory_consumption': 20}],
                          climbing_robot.installed_software)


if __name__ == "__main__":
    main()
