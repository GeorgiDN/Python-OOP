from project.climbing_robot import ClimbingRobot
from unittest import TestCase, main


class ClimbingRobotTest(TestCase):
    def setUp(self):
        self.robot = ClimbingRobot("Mountain", "Part1", 100, 100)

    def test_init(self):
        self.assertEqual(self.robot.category, "Mountain")
        self.assertEqual(self.robot.part_type, "Part1")
        self.assertEqual(self.robot.capacity, 100)
        self.assertEqual(self.robot.memory, 100)
        self.assertEqual([], self.robot.installed_software)

    def test_with_not_allowed_category_raise_exception(self):
        with self.assertRaises(ValueError) as ve:
            climbing_robot = ClimbingRobot("Invalid", "Part1", 100, 200)
        expected_message = f"Category should be one of {self.robot.ALLOWED_CATEGORIES}"
        self.assertEqual(expected_message, str(ve.exception))

    def test_category_with_Mountain(self):
        self.robot.category = "Mountain"
        self.assertEqual(self.robot.category, "Mountain")

    def test_category_with_Alpine(self):
        self.robot.category = "Alpine"
        self.assertEqual(self.robot.category, "Alpine")

    def test_category_with_Indoor(self):
        self.robot.category = "Indoor"
        self.assertEqual(self.robot.category, "Indoor")

    def test_category_with_Bouldering(self):
        self.robot.category = "Bouldering"
        self.assertEqual(self.robot.category, "Bouldering")

    def test_get_used_capacity_with_zero(self):
        res = self.robot.get_used_capacity()
        self.assertEqual(res, 0)

    def test_get_used_capacity(self):
        software1 = {"name": "test1", "capacity_consumption": 10, "memory_consumption": 10}
        software2 = {"name": "test2", "capacity_consumption": 20, "memory_consumption": 10}
        self.robot.install_software(software1)
        self.robot.install_software(software2)
        res = self.robot.get_used_capacity()
        self.assertEqual(res, 30)

    def test_get_available_capacity(self):
        software = {"name": "test1", "capacity_consumption": 10, "memory_consumption": 10}
        software2 = {"name": "test2", "capacity_consumption": 10, "memory_consumption": 10}
        self.robot.install_software(software)
        self.robot.install_software(software2)
        res = self.robot.get_available_capacity()
        self.assertEqual(res, 80)

    def test_get_used_memory_with_zero(self):
        res = self.robot.get_used_memory()
        self.assertEqual(res, 0)

    def test_get_used_memory(self):
        software = {"name": "test1", "capacity_consumption": 10, "memory_consumption": 10}
        software2 = {"name": "test2", "capacity_consumption": 10, "memory_consumption": 10}
        self.robot.install_software(software)
        self.robot.install_software(software2)
        res = self.robot.get_used_memory()
        self.assertEqual(res, 20)

    def test_get_available_memory(self):
        software = {"name": "test1", "capacity_consumption": 10, "memory_consumption": 10}
        software2 = {"name": "test2", "capacity_consumption": 10, "memory_consumption": 10}
        self.robot.install_software(software)
        self.robot.install_software(software2)
        res = self.robot.get_available_memory()
        self.assertEqual(res, 80)

    def test_install_software_with_lower_consumption_and_memory(self):
        software = {"name": "test1", "capacity_consumption": 10, "memory_consumption": 10}
        res = self.robot.install_software(software)
        self.assertEqual(res, f"Software '{software['name']}' successfully installed on {self.robot.category} part.")
        self.assertEqual([software], self.robot.installed_software)

    def test_install_software_with_equal_consumption_and_memory(self):
        software = {"name": "test1", "capacity_consumption": 100, "memory_consumption": 100}
        res = self.robot.install_software(software)
        self.assertEqual(res, f"Software '{software['name']}' successfully installed on {self.robot.category} part.")
        self.assertEqual([software], self.robot.installed_software)

    def test_install_software_with_greater_consumption_and_memory(self):
        software = {"name": "test1", "capacity_consumption": 1000, "memory_consumption": 1000}
        res = self.robot.install_software(software)
        self.assertEqual(res, f"Software '{software['name']}' cannot be installed on {self.robot.category} part.")
        self.assertEqual([], self.robot.installed_software)

    def test_install_software_with_greater_consumption(self):
        software = {"name": "test1", "capacity_consumption": 1000, "memory_consumption": 10}
        res = self.robot.install_software(software)
        self.assertEqual(res, f"Software '{software['name']}' cannot be installed on {self.robot.category} part.")
        self.assertEqual([], self.robot.installed_software)

    def test_install_software_with_greater_memory(self):
        software = {"name": "test1", "capacity_consumption": 100, "memory_consumption": 1000}
        res = self.robot.install_software(software)
        self.assertEqual(res, f"Software '{software['name']}' cannot be installed on {self.robot.category} part.")
        self.assertEqual([], self.robot.installed_software)


if __name__ == '__main__':
    main()




###################################################################################################
# from project.climbing_robot import ClimbingRobot
# from unittest import TestCase, main
#
#
# class ClimbingRobotTest(TestCase):
#
#     def test_01_init(self):
#         climbing_robot = ClimbingRobot("Mountain", "Part1", 100, 200)
#         self.assertEqual(climbing_robot.category, "Mountain")
#         self.assertEqual(climbing_robot.part_type, "Part1")
#         self.assertEqual(climbing_robot.capacity, 100)
#         self.assertEqual(climbing_robot.memory, 200)
#         self.assertEqual([], climbing_robot.installed_software)
#
#     def test_02_category_raise_message(self):
#         with self.assertRaises(ValueError) as ve:
#             climbing_robot = ClimbingRobot("USA", "Part1", 100, 200)
#         expected_message = "Category should be one of ['Mountain', 'Alpine', 'Indoor', 'Bouldering']"
#         output = str(ve.exception)
#         self.assertEqual(output, expected_message)
#
#     def test_03_category_setter_mountain(self):
#         climbing_robot = ClimbingRobot("Mountain", "Part1", 100, 200)
#         self.assertEqual(climbing_robot.category, "Mountain")
#
#     def test_04_category_setter_alpine(self):
#         climbing_robot = ClimbingRobot("Alpine", "Part1", 100, 200)
#         self.assertEqual(climbing_robot.category, "Alpine")
#
#     def test_05_category_setter_indoor(self):
#         climbing_robot = ClimbingRobot("Indoor", "Part1", 100, 200)
#         self.assertEqual(climbing_robot.category, "Indoor")
#
#     def test_06_category_setter_bouldering(self):
#         climbing_robot = ClimbingRobot("Bouldering", "Part1", 100, 200)
#         self.assertEqual(climbing_robot.category, "Bouldering")
#
#     def test_07_get_used_capacity(self):
#         climbing_robot = ClimbingRobot("Mountain", "Part1", 100, 200)
#         software1 = {'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 50}
#         software2 = {'name': 'Software2', 'capacity_consumption': 40, 'memory_consumption': 70}
#         climbing_robot.install_software(software1)
#         climbing_robot.install_software(software2)
#         res = climbing_robot.get_used_capacity()
#         output = 70
#         self.assertEqual(res, output)
#
#     def test_08_get_available_capacity(self):
#         climbing_robot = ClimbingRobot("Mountain", "Part1", 100, 200)
#         software1 = {'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 50}
#         climbing_robot.install_software(software1)
#         res = climbing_robot.get_available_capacity()
#         output = 70
#         self.assertEqual(res, output)
#
#     def test_09_get_available_memory(self):
#         climbing_robot = ClimbingRobot("Mountain", "Part1", 100, 200)
#         software1 = {'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 50}
#         climbing_robot.install_software(software1)
#         res = climbing_robot.get_available_memory()
#         output = 150
#         self.assertEqual(res, output)
#
#     def test_10_get_used_memory(self):
#         climbing_robot = ClimbingRobot("Mountain", "Part1", 100, 200)
#         software1 = {'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 50}
#         software2 = {'name': 'Software2', 'capacity_consumption': 40, 'memory_consumption': 70}
#         climbing_robot.install_software(software1)
#         climbing_robot.install_software(software2)
#         res = climbing_robot.get_used_memory()
#         output = 120
#         self.assertEqual(res, output)
#
#     def test_11_install_software_with_not_enough_capacity(self):
#         climbing_robot = ClimbingRobot("Mountain", "Part1", 10, 200)
#         software1 = {'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 50}
#         res = climbing_robot.install_software(software1)
#         expected_message = "Software 'Software1' cannot be installed on Mountain part."
#         self.assertEqual([], climbing_robot.installed_software)
#         self.assertEqual(res, expected_message)
#
#     def test_12_install_software_with_not_enough_memory(self):
#         climbing_robot = ClimbingRobot("Mountain", "Part1", 100, 20)
#         software1 = {'name': 'Software1', 'capacity_consumption': 30, 'memory_consumption': 50}
#         res = climbing_robot.install_software(software1)
#         expected_message = "Software 'Software1' cannot be installed on Mountain part."
#         self.assertEqual([], climbing_robot.installed_software)
#         self.assertEqual(res, expected_message)
#
#     def test_13_install_software_with_equal_capacity(self):
#         climbing_robot = ClimbingRobot("Mountain", "Part1", 100, 200)
#         software1 = {'name': 'Software1', 'capacity_consumption': 100, 'memory_consumption': 50}
#         res = climbing_robot.install_software(software1)
#         expected_message = f"Software 'Software1' successfully installed on Mountain part."
#         self.assertEqual(res, expected_message)
#         self.assertEqual([{'name': 'Software1', 'capacity_consumption': 100, 'memory_consumption': 50}],
#                           climbing_robot.installed_software)
#
#     def test_14_install_software_with_more_capacity(self):
#         climbing_robot = ClimbingRobot("Mountain", "Part1", 100, 200)
#         software1 = {'name': 'Software1', 'capacity_consumption': 10, 'memory_consumption': 50}
#         res = climbing_robot.install_software(software1)
#         expected_message = f"Software 'Software1' successfully installed on Mountain part."
#         self.assertEqual(res, expected_message)
#         self.assertEqual([{'name': 'Software1', 'capacity_consumption': 10, 'memory_consumption': 50}],
#                          climbing_robot.installed_software)
#
#     def test_15_install_software_with_equal_memory(self):
#         climbing_robot = ClimbingRobot("Mountain", "Part1", 100, 200)
#         software1 = {'name': 'Software1', 'capacity_consumption': 10, 'memory_consumption': 200}
#         res = climbing_robot.install_software(software1)
#         expected_message = f"Software 'Software1' successfully installed on Mountain part."
#         self.assertEqual(res, expected_message)
#         self.assertEqual([{'name': 'Software1', 'capacity_consumption': 10, 'memory_consumption': 200}],
#                           climbing_robot.installed_software)
#
#     def test_16_install_software_with_more_memory(self):
#         climbing_robot = ClimbingRobot("Mountain", "Part1", 100, 200)
#         software1 = {'name': 'Software1', 'capacity_consumption': 10, 'memory_consumption': 20}
#         res = climbing_robot.install_software(software1)
#         expected_message = f"Software 'Software1' successfully installed on Mountain part."
#         self.assertEqual(res, expected_message)
#         self.assertEqual([{'name': 'Software1', 'capacity_consumption': 10, 'memory_consumption': 20}],
#                           climbing_robot.installed_software)
#
#
# if __name__ == "__main__":
#     main()
