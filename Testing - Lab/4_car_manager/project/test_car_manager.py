from unittest import TestCase, main

from project.car_manager import Car


class CarTest(TestCase):
    def setUp(self):
        self.car = Car("vw", "golf", 10, 100)

    def test_make_with_empty_string_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("", "golf", 10, 100)
        self.assertEqual("Make cannot be null or empty!", str(ex.exception))

    def test_make_with_not_empty_string(self):
        self.car = Car("vw", "golf", 10, 100)
        self.assertEqual(self.car.make, "vw")

    def test_model_with_empty_string_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("vw", "", 10, 100)
        self.assertEqual("Model cannot be null or empty!", str(ex.exception))

    def test_model_with_not_empty_string(self):
        self.car = Car("vw", "golf", 10, 100)
        self.assertEqual(self.car.model, "golf")

    def test_fuel_consumption_with_negative_value(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("vw", "golf", -1, 100)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_consumption_with_zero_value(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("vw", "golf", 0, 100)
        self.assertEqual("Fuel consumption cannot be zero or negative!", str(ex.exception))

    def test_fuel_consumption_with_value_greater_than_zero(self):
        self.car = Car("vw", "golf", 10, 100)
        self.assertEqual(self.car.fuel_consumption, 10)

    def test_fuel_capacity_with_negative_value(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("vw", "golf", 10, -1)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_with_zero_value(self):
        with self.assertRaises(Exception) as ex:
            self.car = Car("vw", "golf", 1, 0)
        self.assertEqual("Fuel capacity cannot be zero or negative!", str(ex.exception))

    def test_fuel_capacity_with_value_greater_than_zero(self):
        self.car = Car("vw", "golf", 10, 100)
        self.assertEqual(self.car.fuel_capacity, 100)

    def test_fuel_amount_with_negative_value(self):
        with self.assertRaises(Exception) as ex:
            self.car.fuel_amount = -1
        self.assertEqual("Fuel amount cannot be negative!", str(ex.exception))

    def test_fuel_amount_with_not_negative_value(self):
        self.car.fuel_amount = 0
        self.assertEqual(self.car.fuel_amount, 0)

    def test_refuel_with_negative_fuel_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(-1)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_with_zero_fuel_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.car.refuel(0)
        self.assertEqual("Fuel amount cannot be zero or negative!", str(ex.exception))

    def test_refuel_with_value_greater_than_zero_and_greater_than_capacity(self):
        self.car.fuel_amount = 95
        self.car.refuel(10)
        self.assertEqual(self.car.fuel_amount, 100)

    def test_refuel_with_value_greater_than_zero_and_less_than_capacity(self):
        self.car.fuel_amount = 80
        self.car.refuel(10)
        self.assertEqual(self.car.fuel_amount, 90)

    def test_drive_with_not_enough_fuel(self):
        self.car.fuel_amount = 1
        with self.assertRaises(Exception) as ex:
            self.car.drive(100)
        self.assertEqual("You don't have enough fuel to drive!", str(ex.exception))

    def test_drive_with_enough_fuel_and_reduce_fuel_amount(self):
        self.car.fuel_amount = 50
        self.car.drive(10)
        self.assertEqual(49, self.car.fuel_amount)


if __name__ == '__main__':
    main()
