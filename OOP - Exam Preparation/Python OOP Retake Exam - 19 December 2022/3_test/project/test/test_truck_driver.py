from unittest import TestCase, main

from project.truck_driver import TruckDriver


class TestTruckDriver(TestCase):
    def setUp(self):
        self.driver = TruckDriver("driver", 10.0)

    def test_init(self):
        self.assertIsInstance(self.driver, TruckDriver)
        self.assertEqual(self.driver.name, "driver")
        self.assertEqual(self.driver.money_per_mile, 10.0)
        self.assertEqual(self.driver.available_cargos, {})
        self.assertEqual(self.driver.earned_money, 0)
        self.assertEqual(self.driver.miles, 0)

    def test_earned_money_with_negative_value_raise_exception(self):
        with self.assertRaises(ValueError) as ve:
            self.driver.earned_money = -1
        self.assertEqual(str(ve.exception), f"{self.driver.name} went bankrupt.")

    def test_earned_money(self):
        self.driver.earned_money = 100
        self.assertEqual(self.driver.earned_money, 100)

    def test_add_cargo_offer(self):
        result = self.driver.add_cargo_offer("sofia", 10)
        message = f"Cargo for 10 to sofia was added as an offer."
        self.assertEqual(result, message)
        self.assertEqual(self.driver.available_cargos, {'sofia': 10})

    def test_add_cargo_offer_with_already_added_cargo(self):
        self.driver.add_cargo_offer("sofia", 10)
        with self.assertRaises(Exception) as ex:
            self.driver.add_cargo_offer("sofia", 10)
        message = "Cargo offer is already added."
        self.assertEqual(str(ex.exception), message)
        self.assertEqual(self.driver.available_cargos, {'sofia': 10})

    def test_drive_best_cargo_offer(self):
        self.driver.add_cargo_offer("sofia", 2)
        self.driver.add_cargo_offer("varna", 1)
        self.assertEqual(self.driver.available_cargos, {'sofia': 2, 'varna': 1})
        result = self.driver.drive_best_cargo_offer()
        message = f"{self.driver.name} is driving 2 to sofia."
        self.assertEqual(result, message)
        self.assertEqual(self.driver.earned_money, 20)
        self.assertEqual(self.driver.miles, 2)

    def test_drive_best_cargo_offer_and_eat(self):
        self.driver.add_cargo_offer("sofia", 250)
        self.driver.add_cargo_offer("varna", 1)
        self.assertEqual(self.driver.available_cargos, {'sofia': 250, 'varna': 1})
        result = self.driver.drive_best_cargo_offer()
        message = f"{self.driver.name} is driving 250 to sofia."
        self.assertEqual(result, message)
        self.assertEqual(self.driver.earned_money, 2480.0)
        self.assertEqual(self.driver.miles, 250)

    def test_drive_best_cargo_offer_and_sleep(self):
        self.driver.add_cargo_offer("sofia", 1000)
        self.driver.add_cargo_offer("varna", 1)
        self.assertEqual(self.driver.available_cargos, {'sofia': 1000, 'varna': 1})
        result = self.driver.drive_best_cargo_offer()
        message = f"{self.driver.name} is driving 1000 to sofia."
        self.assertEqual(result, message)
        self.assertEqual(self.driver.earned_money, 9875.0)
        self.assertEqual(self.driver.miles, 1000)

    def test_drive_best_cargo_offer_and_pump_gas(self):
        self.driver.add_cargo_offer("sofia", 1500)
        self.driver.add_cargo_offer("varna", 1)
        self.assertEqual(self.driver.available_cargos, {'sofia': 1500, 'varna': 1})
        result = self.driver.drive_best_cargo_offer()
        message = f"{self.driver.name} is driving 1500 to sofia."
        self.assertEqual(result, message)
        self.assertEqual(self.driver.earned_money, 14335.0)
        self.assertEqual(self.driver.miles, 1500)

    def test_drive_best_cargo_offer_and_repair_truck(self):
        self.driver.add_cargo_offer("sofia", 10000)
        self.driver.add_cargo_offer("varna", 1)
        self.assertEqual(self.driver.available_cargos, {'sofia': 10000, 'varna': 1})
        result = self.driver.drive_best_cargo_offer()
        message = f"{self.driver.name} is driving 10000 to sofia."
        self.assertEqual(result, message)
        self.assertEqual(self.driver.earned_money, 88250.0)
        self.assertEqual(self.driver.miles, 10000)

    def test_drive_best_cargo_offer_with_no_offer_raise_valueerror(self):
        result = self.driver.drive_best_cargo_offer()
        message = "There are no offers available."
        self.assertEqual(result, message)

    def test_repr(self):
        result = self.driver.__repr__()
        message = f"{self.driver.name} has {self.driver.miles} miles behind his back."
        self.assertEqual(result, message)


if __name__ == '__main__':
    main()


