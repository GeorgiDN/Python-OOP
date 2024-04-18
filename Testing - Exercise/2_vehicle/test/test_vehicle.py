from unittest import TestCase, main

from project.vehicle import Vehicle


class VehicleTest(TestCase):
    def setUp(self):
        self.vehicle = Vehicle(100.00, 200.00)

    def test_init(self):
        self.assertEqual(100.00, self.vehicle.fuel)
        self.assertEqual(self.vehicle.fuel, self.vehicle.capacity)
        self.assertEqual(200.00, self.vehicle.horse_power)
        self.assertEqual(1.25, self.vehicle.DEFAULT_FUEL_CONSUMPTION)

    def test_drive_with_not_enough_fuel_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.drive(100)
        self.assertEqual("Not enough fuel", str(ex.exception))

    def test_drive_with_enough_fuel_and_reduce_fuel_with_passed_kilometers_multiplied_by_fuel_consumption(self):
        self.vehicle.drive(10)
        self.assertEqual(self.vehicle.fuel, 87.50)

    def test_refuel_with_fuel_more_than_capacity_raise_exception(self):
        with self.assertRaises(Exception) as ex:
            self.vehicle.refuel(200)
        self.assertEqual("Too much fuel", str(ex.exception))

    def test_refuel_with_fuel_less_than_capacity(self):
        self.vehicle.fuel = 20
        self.vehicle.refuel(30)
        self.assertEqual(50.0, self.vehicle.fuel)

    def test_str_method(self):
        res = f"The vehicle has {self.vehicle.horse_power} " \
               f"horse power with {self.vehicle.fuel} fuel left and {self.vehicle.fuel_consumption} fuel consumption"
        self.assertEqual(res, self.vehicle.__str__())


if __name__ == '__main__':
    main()
