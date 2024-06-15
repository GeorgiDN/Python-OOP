from project.railway_station import RailwayStation
from collections import deque
from unittest import main, TestCase


class TestsRailwayStation(TestCase):
    def setUp(self):
        self.station = RailwayStation("Station")

    def test_init(self):
        self.station.name = "Station"
        self.station.arrival_trains = deque()
        self.station.departure_trains = deque()

    def test_name_setter_with_empty_string(self):
        with self.assertRaises(ValueError) as ve:
            self.station.name = ''
        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_name_setter_with_len_string_equal_to_one(self):
        with self.assertRaises(ValueError) as ve:
            self.station.name = 'S'
        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_name_setter_with_len_string_equal_to_two(self):
        with self.assertRaises(ValueError) as ve:
            self.station.name = 'St'
        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_name_setter_with_len_string_equal_to_three(self):
        with self.assertRaises(ValueError) as ve:
            self.station.name = 'Sta'
        self.assertEqual("Name should be more than 3 symbols!", str(ve.exception))

    def test_new_arrival_on_board(self):
        self.station.new_arrival_on_board("train1")
        self.assertEqual(self.station.arrival_trains, deque(["train1"]))

    def test_train_has_arrived_with_other_train_before(self):
        self.station.arrival_trains = deque(["train1", "train2"])
        res = self.station.train_has_arrived("train3")
        self.assertEqual(res, f"There are other trains to arrive before train3.")

    def test_train_has_arrived_with_train_info_equal_to_first_train(self):
        self.station.new_arrival_on_board("train1")
        self.station.new_arrival_on_board("train2")
        res = self.station.train_has_arrived("train1")
        self.assertEqual(res, "train1 is on the platform and will leave in 5 minutes.")
        self.assertEqual(self.station.arrival_trains, deque(["train2"]))
        self.assertEqual(self.station.departure_trains, deque(["train1"]))

    def test_train_has_arrived_with_train_info_equal_to_the_only_train_in_the_list(self):
        self.station.new_arrival_on_board("train1")
        res = self.station.train_has_arrived("train1")
        self.assertEqual(res, "train1 is on the platform and will leave in 5 minutes.")
        self.assertEqual(self.station.arrival_trains, deque())
        self.assertEqual(self.station.departure_trains, deque(["train1"]))

    def test_train_has_left_with_empty_departure_trains(self):
        res = self.station.train_has_left("train1")
        self.assertFalse(res)

    def test_train_has_left_with_first_train_from_departure_trains_not_equal_to_train_info(self):
        self.station.new_arrival_on_board("train1")
        self.station.new_arrival_on_board("train2")
        self.station.train_has_arrived("train1")
        res = self.station.train_has_left("train3")
        self.assertFalse(res)

    def test_train_has_left_with_first_train_from_departure_trains_equal_to_train_info(self):
        self.station.new_arrival_on_board("train1")
        self.station.new_arrival_on_board("train2")
        self.station.train_has_arrived("train1")
        res = self.station.train_has_left("train1")
        self.assertTrue(res)
        self.assertEqual(self.station.departure_trains, deque())


if __name__ == '__main__':
    main()










# from project.railway_station import RailwayStation
# from collections import deque
# from unittest import main, TestCase
#
#
# class TestsRailwayStation(TestCase):
#     def test_01_init(self):
#         railwaystation = RailwayStation("London")
#         self.assertEqual("London", railwaystation.name)
#         self.assertEqual(deque(), railwaystation.arrival_trains)
#         self.assertEqual(deque(), railwaystation.departure_trains)
#
#     def test_02_name_with_less_than_3_symbols(self):
#         # No symbol
#         with self.assertRaises(ValueError) as ve:
#             railwaystation = RailwayStation("")
#
#         expected_message = "Name should be more than 3 symbols!"
#         output = str(ve.exception)
#         self.assertEqual(expected_message, output)
#
#         # One symbol
#         with self.assertRaises(ValueError) as ve:
#             railwaystation = RailwayStation("L")
#
#         expected_message = "Name should be more than 3 symbols!"
#         output = str(ve.exception)
#         self.assertEqual(expected_message, output)
#
#         # Two symbol
#         with self.assertRaises(ValueError) as ve:
#             railwaystation = RailwayStation("Lo")
#
#         expected_message = "Name should be more than 3 symbols!"
#         output = str(ve.exception)
#         self.assertEqual(expected_message, output)
#
#     def test_03_name_with_less_than_3_symbols(self):
#         # Three symnols
#         with self.assertRaises(ValueError) as ve:
#             railwaystation = RailwayStation("Lon")
#
#         expected_message = "Name should be more than 3 symbols!"
#         output = str(ve.exception)
#         self.assertEqual(expected_message, output)
#
#     def test_04_name_expect_to_success(self):
#         railwaystation = RailwayStation("London")
#         self.assertEqual("London", railwaystation.name)
#
#     def test_05_new_arrival_on_board(self):
#         railwaystation = RailwayStation("London")
#         res = railwaystation.new_arrival_on_board("train_info")
#         self.assertEqual(deque(["train_info"]), railwaystation.arrival_trains)
#
#     def test_06_train_has_arrived_not_equal_to_train_info(self):
#         railwaystation = RailwayStation("London")
#         railwaystation.new_arrival_on_board("train_info")
#         self.assertEqual(deque(["train_info"]), railwaystation.arrival_trains)
#         res = railwaystation.train_has_arrived("Other")
#         expected_message = f"There are other trains to arrive before Other."
#         self.assertEqual(res, expected_message)
#
#     def test_07_train_has_arrived_equal_to_train_info(self):
#         railwaystation = RailwayStation("London")
#         railwaystation.new_arrival_on_board("train_info")
#         railwaystation.new_arrival_on_board("train_info_2")
#         self.assertEqual(deque(["train_info", "train_info_2"]), railwaystation.arrival_trains)
#         res = railwaystation.train_has_arrived("train_info")
#         expected_message = f"train_info is on the platform and will leave in 5 minutes."
#         self.assertEqual(res, expected_message)
#
#     def test_08_train_has_left_with_true(self):
#         railwaystation = RailwayStation("London")
#         railwaystation.new_arrival_on_board("train_info")
#         self.assertEqual(deque(["train_info"]), railwaystation.arrival_trains)
#         railwaystation.train_has_arrived("train_info")
#         res = railwaystation.train_has_left("train_info")
#         self.assertEqual(True, res)
#
#     def test_09_train_has_left_with_true(self):
#         railwaystation = RailwayStation("London")
#         railwaystation.new_arrival_on_board("train_info")
#         self.assertEqual(deque(["train_info"]), railwaystation.arrival_trains)
#         railwaystation.train_has_arrived("train_info")
#         res = railwaystation.train_has_left("other")
#         self.assertEqual(False, res)
#
#
# if __name__ == "__main__":
#     main()
