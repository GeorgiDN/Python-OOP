from project.second_hand_car import SecondHandCar
from unittest import TestCase, main


class SecondHandCarTest(TestCase):
    def setUp(self):
        self.car1 = SecondHandCar("vw", "golf", 200, 100.0)

    def test_name_init(self):
        self.assertEqual("vw", self.car1.model)
        self.assertEqual("golf", self.car1.car_type)
        self.assertEqual(200, self.car1.mileage)
        self.assertEqual(100.0, self.car1.price)

    def test_price_less_than_one(self):
        with self.assertRaises(ValueError) as ve:
            self.car1.price = 0
        expected_message = 'Price should be greater than 1.0!'
        self.assertEqual(expected_message, str(ve.exception))

    def test_price_equal_to_one(self):
        with self.assertRaises(ValueError) as ve:
            self.car1.price = 1.0
        expected_message = 'Price should be greater than 1.0!'
        self.assertEqual(expected_message, str(ve.exception))

    def test_price_greater_than_one(self):
        self.car1.price = 200
        self.assertEqual(self.car1.price, 200.0)

    def test_mileage_less_than_100(self):
        with self.assertRaises(ValueError) as ve:
            self.car1.mileage = 1.0
        expected_message = 'Please, second-hand cars only! Mileage must be greater than 100!'
        self.assertEqual(expected_message, str(ve.exception))

    def test_mileage_equal_to_100(self):
        with self.assertRaises(ValueError) as ve:
            self.car1.mileage = 100.0
        expected_message = 'Please, second-hand cars only! Mileage must be greater than 100!'
        self.assertEqual(expected_message, str(ve.exception))

    def test_mileage_greater_than_100(self):
        self.car1.mileage = 200
        self.assertEqual(self.car1.mileage, 200.0)

    def test_set_promotional_price_with_greater_price(self):
        with self.assertRaises(ValueError) as ve:
            self.car1.set_promotional_price(300.0)
        expected_message = 'You are supposed to decrease the price!'
        self.assertEqual(expected_message, str(ve.exception))

    def test_set_promotional_price_with_equal_price(self):
        with self.assertRaises(ValueError) as ve:
            self.car1.set_promotional_price(100.0)
        expected_message = 'You are supposed to decrease the price!'
        self.assertEqual(expected_message, str(ve.exception))

    def test_set_promotional_price_less_than_price(self):
        result = self.car1.set_promotional_price(90.0)
        self.assertEqual(self.car1.price, 90.0)
        message = 'The promotional price has been successfully set.'
        self.assertEqual(message, result)

    def test_need_to_repair_with_greater_repair_price_impossible_repair(self):
        result = self.car1.need_repair(100.0, "turbo")
        message = 'Repair is impossible!'
        self.assertEqual(message, result)

    def test_need_to_repair_successful_with_equal_repair_price(self):
        result = self.car1.need_repair(50.0, "turbo")
        message = 'Price has been increased due to repair charges.'
        self.assertEqual(message, result)
        self.assertEqual(self.car1.price, 150.0)
        self.assertEqual(self.car1.repairs, ["turbo"])

    def test_need_to_repair_successful_with_less_repair_price(self):
        result = self.car1.need_repair(20.0, "turbo")
        message = 'Price has been increased due to repair charges.'
        self.assertEqual(message, result)
        self.assertEqual(self.car1.price, 120.0)
        self.assertEqual(self.car1.repairs, ["turbo"])

    def test_greater_than_method_with_different_types(self):
        self.car2 = SecondHandCar("vw", "passat", 200, 100.0)
        result = self.car1.__gt__(self.car2)
        message = 'Cars cannot be compared. Type mismatch!'
        self.assertEqual(result, message)

    def test_greater_than_method_with_same_types_equal_price(self):
        self.car2 = SecondHandCar("vw", "golf", 200, 100.0)
        result = self.car1.__gt__(self.car2)
        self.assertFalse(result)

    def test_greater_than_method_with_same_types_greater_price(self):
        self.car2 = SecondHandCar("vw", "golf", 200, 200.0)
        result = self.car1.__gt__(self.car2)
        self.assertFalse(result)

    def test_greater_than_method_with_same_types_lower_price(self):
        self.car2 = SecondHandCar("vw", "golf", 200, 90.0)
        result = self.car1.__gt__(self.car2)
        self.assertTrue(result)

    def test_str_method(self):
        self.car1.need_repair(20.0, "turbo")
        result = f"""Model {self.car1.model} | Type {self.car1.car_type} | Milage {self.car1.mileage}km
Current price: {self.car1.price:.2f} | Number of Repairs: {len(self.car1.repairs)}"""
        self.assertEqual(self.car1.__str__(), result)


if __name__ == '__main__':
    main()



# from project.second_hand_car import SecondHandCar
# from unittest import TestCase, main
#
#
# class SecondHandCarTest(TestCase):
#
#     def test_01_init(self):
#         second_hand_car = SecondHandCar("VW", "Golf", 100000, 10000.0)
#         self.assertEqual(second_hand_car.model, "VW")
#         self.assertEqual(second_hand_car.car_type, "Golf")
#         self.assertEqual(second_hand_car.mileage, 100000)
#         self.assertEqual(second_hand_car.price, 10000.0)
#         self.assertEqual([], second_hand_car.repairs)
#
#     def test_02_price_equal_to_one(self):
#         with self.assertRaises(ValueError) as ve:
#             second_hand_car = SecondHandCar("VW", "Golf", 100000, 1.0)
#
#         expected_message = 'Price should be greater than 1.0!'
#         output = str(ve.exception)
#         self.assertEqual(expected_message, output)
#
#     def test_03_price_equal_to_zero(self):
#         with self.assertRaises(ValueError) as ve:
#             second_hand_car = SecondHandCar("VW", "Golf", 100000, 0.0)
#
#         expected_message = 'Price should be greater than 1.0!'
#         output = str(ve.exception)
#         self.assertEqual(expected_message, output)
#
#     def test_04_negative_price(self):
#         with self.assertRaises(ValueError) as ve:
#             second_hand_car = SecondHandCar("VW", "Golf", 100000, -1.0)
#
#         expected_message = 'Price should be greater than 1.0!'
#         output = str(ve.exception)
#         self.assertEqual(expected_message, output)
#
#     def test_05_price_greater_than_one(self):
#         second_hand_car = SecondHandCar("VW", "Golf", 100000, 10000.0)
#         self.assertEqual(second_hand_car.price, 10000.0)
#
#     def test_06_mileage_equal_to_100(self):
#         with self.assertRaises(ValueError) as ve:
#             second_hand_car = SecondHandCar("VW", "Golf", 100, 10000.0)
#
#         expected_message = 'Please, second-hand cars only! Mileage must be greater than 100!'
#         output = str(ve.exception)
#         self.assertEqual(expected_message, output)
#
#     def test_07_mileage_less_than_100(self):
#         with self.assertRaises(ValueError) as ve:
#             second_hand_car = SecondHandCar("VW", "Golf", 90, 10000.0)
#
#         expected_message = 'Please, second-hand cars only! Mileage must be greater than 100!'
#         output = str(ve.exception)
#         self.assertEqual(expected_message, output)
#
#     def test_08_negative_mileage(self):
#         with self.assertRaises(ValueError) as ve:
#             second_hand_car = SecondHandCar("VW", "Golf", -20, 10000.0)
#
#         expected_message = 'Please, second-hand cars only! Mileage must be greater than 100!'
#         output = str(ve.exception)
#         self.assertEqual(expected_message, output)
#
#     def test_09_mileage_greater_than_100(self):
#         second_hand_car = SecondHandCar("VW", "Golf", 100000, 10000.0)
#         self.assertEqual(second_hand_car.mileage, 100000)
#
#     def test_10_set_promotional_price_with_new_price_greater_than_the_initial_price(self):
#         second_hand_car = SecondHandCar("VW", "Golf", 100000, 10000.0)
#
#         with self.assertRaises(ValueError) as ve:
#             second_hand_car.set_promotional_price(20000.0)
#         expected_error = 'You are supposed to decrease the price!'
#         self.assertEqual(str(ve.exception), expected_error)
#
#     def test_11_set_promotional_price_with_new_price_equal_to_the_initial_price(self):
#         second_hand_car = SecondHandCar("VW", "Golf", 100000, 10000.0)
#
#         with self.assertRaises(ValueError) as ve:
#             second_hand_car.set_promotional_price(10000.0)
#         expected_error = 'You are supposed to decrease the price!'
#         self.assertEqual(str(ve.exception), expected_error)
#
#     def test_12_set_promotional_price_with_new_price_less_than_the_initial_price(self):
#         second_hand_car = SecondHandCar("VW", "Golf", 100000, 10000.0)
#
#         res = second_hand_car.set_promotional_price(5000.0)
#         expected_message = 'The promotional price has been successfully set.'
#         self.assertEqual(res, expected_message)
#
#     def test_13_need_to_repair_with_bigger_repair_price(self):
#         second_hand_car = SecondHandCar("VW", "Golf", 100000, 10000.0)
#
#         res = second_hand_car.need_repair(6000.0, "Fuel pomp")
#         expected_message = 'Repair is impossible!'
#         self.assertEqual(res, expected_message)
#
#     def test_14_need_to_repair_increase_self_price(self):
#         second_hand_car = SecondHandCar("VW", "Golf", 100000, 10000.0)
#
#         second_hand_car.need_repair(1000.0, "Fuel pomp")
#         self.assertEqual(11000.0, second_hand_car.price)
#
#     def test_15_need_to_repair_increase_self_repairs_append_repair_description(self):
#         second_hand_car = SecondHandCar("VW", "Golf", 100000, 10000.0)
#
#         second_hand_car.need_repair(1000.0, "Fuel pomp")
#         self.assertEqual(["Fuel pomp"], second_hand_car.repairs)
#
#     def test_16_need_to_repair_with_proper_price_expected_message(self):
#         second_hand_car = SecondHandCar("VW", "Golf", 100000, 10000.0)
#         res = second_hand_car.need_repair(1000.0, "Fuel pomp")
#         expected_message = 'Price has been increased due to repair charges.'
#         self.assertEqual(expected_message, res)
#
#     def test_17__gt__method_with_not_the_same_type(self):
#         second_hand_car = SecondHandCar("VW", "Golf", 100000, 10000.0)
#         second_hand_car_2 = SecondHandCar("Audi", "Quatro", 200000, 9000.0)
#         res = second_hand_car.__gt__(second_hand_car_2)
#         expected_message = 'Cars cannot be compared. Type mismatch!'
#         self.assertEqual(res, expected_message)
#
#     def test_18__gt__method_with_price_greater_than_self_price_same_car_type(self):
#         second_hand_car = SecondHandCar("VW", "Golf", 100000, 10000.0)
#         second_hand_car_2 = SecondHandCar("VW", "Golf", 200000, 11000.0)
#         res = second_hand_car.__gt__(second_hand_car_2)
#         self.assertFalse(res)
#
#     def test_19__gt__method_with_price_less_than_self_price_same_car_type(self):
#         second_hand_car = SecondHandCar("VW", "Golf", 100000, 10000.0)
#         second_hand_car_2 = SecondHandCar("VW", "Golf", 200000, 9000.0)
#         res = second_hand_car.__gt__(second_hand_car_2)
#         self.assertTrue(res)
#
#     def test_20__gt__method_with_price_equal_to_self_price_same_car_type(self):
#         second_hand_car = SecondHandCar("VW", "Golf", 100000, 10000.0)
#         second_hand_car_2 = SecondHandCar("VW", "Golf", 200000, 10000.0)
#         res = second_hand_car.__gt__(second_hand_car_2)
#         self.assertFalse(res)
#
#     def test_21__str__method(self):
#         second_hand_car = SecondHandCar("VW", "Golf", 100000, 10000.0)
#         output = "Model VW | Type Golf | Milage 100000km\nCurrent price: 10000.00 | Number of Repairs: 0"
#         self.assertEqual(second_hand_car.__str__(), output)
#
#
# if __name__ == "__main__":
#     main()
