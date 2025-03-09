from project.restaurant import Restaurant
from unittest import TestCase, main


class RestaurantTest(TestCase):
    def setUp(self):
        self.restaurant = Restaurant("detelina", 2)
        self.restaurant.waiters = []

    def test_init(self):
        self.assertEqual(self.restaurant.name, "detelina")
        self.assertEqual(self.restaurant.capacity, 2)
        self.assertEqual(self.restaurant.waiters, [])

    def test_name_with_empty_string(self):
        with self.assertRaises(ValueError) as ve:
            self.restaurant.name = ""
        self.assertEqual("Invalid name!", str(ve.exception))

    def test_capacity_with_empty_negative_value(self):
        with self.assertRaises(ValueError) as ve:
            self.restaurant.capacity = - 1
        self.assertEqual("Invalid capacity!", str(ve.exception))

    def test_add_waiter_with_no_capacity(self):
        self.restaurant.capacity = 0
        res = self.restaurant.add_waiter("Gosho")
        self.assertEqual(res, "No more places!")

    def test_add_waiter(self):
        res = self.restaurant.add_waiter("Gosho")
        self.assertEqual("The waiter Gosho has been added.", res)
        self.assertEqual([{'name': "Gosho"}], self.restaurant.waiters)

    def test_add_waiter_with_existing_name(self):
        self.restaurant.add_waiter("Gosho")
        res = self.restaurant.add_waiter("Gosho")
        self.assertEqual(f"The waiter Gosho already exists!", res)

    def test_remove_waiter_with_not_existing_name(self):
        self.restaurant.add_waiter("Gosho")
        res = self.restaurant.remove_waiter("Ivan")
        self.assertEqual("No waiter found with the name Ivan.", res)

    def test_remove_waiter_with_existing_name(self):
        self.restaurant.add_waiter("Gosho")
        res = self.restaurant.remove_waiter("Gosho")
        self.assertEqual("The waiter Gosho has been removed.", res)
        self.assertEqual([], self.restaurant.waiters)

    def test_get_total_earnings_with_zero(self):
        res = self.restaurant.get_total_earnings()
        self.assertEqual(res, 0)

    def test_get_total_earnings(self):
        self.restaurant.waiters = [
            {'name': "Gosho", "total_earnings": 10},
            {'name': "Ivan", "total_earnings": 20}
        ]

        res = self.restaurant.get_total_earnings()
        self.assertEqual(res, 30)

    def test_get_waiters_with_min_earnings_is_none_and_max_earnings_is_none(self):
        res1 = self.restaurant.waiters = [
            {'name': "Gosho", "total_earnings": 10},
            {'name': "Ivan", "total_earnings": 20}
        ]

        res2 = self.restaurant.get_waiters()
        self.assertEqual(res1, res2)

    def test_get_waiters_with_min_earnings_is_not_none_and_max_earnings_is_not_none(self):
        self.restaurant.waiters = [
            {'name': "Gosho", "total_earnings": 10},
            {'name': "Ivan", "total_earnings": 20},
            {'name': "Pesho", "total_earnings": 30}
        ]

        res1 = self.restaurant.get_waiters(15, 25)
        res2 = [{'name': "Ivan", "total_earnings": 20}]
        self.assertEqual(res1, res2)

    def test_get_waiters_with_min_earnings_is_not_none_and_max_earnings_is_none(self):
        self.restaurant.waiters = [
            {'name': "Gosho", "total_earnings": 10},
            {'name': "Ivan", "total_earnings": 20},
            {'name': "Pesho", "total_earnings": 30}
        ]

        res1 = self.restaurant.get_waiters(min_earnings=21)
        res2 = [{'name': "Pesho", "total_earnings": 30}]
        self.assertEqual(res1, res2)

    def test_get_waiters_with_min_earnings_is_none_and_max_earnings_is_not_none(self):
        self.restaurant.waiters = [
            {'name': "Gosho", "total_earnings": 10},
            {'name': "Ivan", "total_earnings": 20},
            {'name': "Pesho", "total_earnings": 30}
        ]

        res1 = self.restaurant.get_waiters(max_earnings=15)
        res2 = [{'name': "Gosho", "total_earnings": 10}]
        self.assertEqual(res1, res2)


if __name__ == "__main__":
    main()

