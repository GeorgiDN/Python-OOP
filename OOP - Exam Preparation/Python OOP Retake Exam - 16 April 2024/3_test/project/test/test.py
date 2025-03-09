from project.restaurant import Restaurant
from unittest import TestCase, main

class TestRestaurant(TestCase):
    def setUp(self):
        self.restaurant = Restaurant('Detelina', 10)

    def test_init(self):
        self.assertIsInstance(self.restaurant, Restaurant)
        self.assertEqual(self.restaurant.name, 'Detelina')
        self.assertEqual(self.restaurant.capacity, 10)
        self.assertEqual(self.restaurant.waiters, [])

    def test_name_with_empty_string(self):
        with self.assertRaises(ValueError) as ve:
            self.restaurant.name = ''
        message = "Invalid name!"
        self.assertEqual(message, str(ve.exception))

    def test_name_with_spaces_only(self):
        with self.assertRaises(ValueError) as ve:
            self.restaurant.name = '  '
        message = "Invalid name!"
        self.assertEqual(message, str(ve.exception))

    def test_capacity_with_negative_value(self):
        with self.assertRaises(ValueError) as ve:
            self.restaurant.capacity = -1
        message = "Invalid capacity!"
        self.assertEqual(message, str(ve.exception))

    def test_capacity_with_zero_value(self):
        self.restaurant.capacity = 0
        self.assertEqual(self.restaurant.capacity, 0)

    def test_get_waiters_with_both_earnings_none(self):
        result = self.restaurant.get_waiters()
        self.assertEqual(result, [])

    def test_add_waiters_with_zero_capacity(self):
        self.restaurant.capacity = 0
        result = self.restaurant.add_waiter('Ivan')
        message = "No more places!"
        self.assertEqual(result, message)

    def test_add_waiter_with_no_more_capacity(self):
        self.restaurant.capacity = 1
        self.restaurant.add_waiter('Ivan')
        result = self.restaurant.add_waiter('Ivan')
        message = "No more places!"
        self.assertEqual(result, message)

    def test_add_waiter_with_existing_name(self):
        self.restaurant.add_waiter('Ivan')
        result = self.restaurant.add_waiter('Ivan')
        message = "The waiter Ivan already exists!"
        self.assertEqual(result, message)

    def test_add_waiter_successful(self):
        result = self.restaurant.add_waiter('Ivan')
        message = "The waiter Ivan has been added."
        self.assertEqual(self.restaurant.waiters, [{'name': 'Ivan'}])
        self.assertEqual(result, message)

    def test_add_waiter_successfully_with_more_waiters(self):
        self.restaurant.add_waiter('Go6o')
        result = self.restaurant.add_waiter('Ivan')
        message = "The waiter Ivan has been added."
        self.assertEqual(self.restaurant.waiters, [{'name': 'Go6o'}, {'name': 'Ivan'}])
        self.assertEqual(result, message)

    def test_remove_waiter_with_not_existing_waiter(self):
        self.restaurant.add_waiter('Ivan')
        result = self.restaurant.remove_waiter('Go6o')
        message = f"No waiter found with the name Go6o."
        self.assertEqual(result, message)

    def test_remove_waiter_with_existing_waiter(self):
        self.restaurant.add_waiter('Ivan')
        self.restaurant.add_waiter('Go6o')
        result = self.restaurant.remove_waiter('Go6o')
        message = "The waiter Go6o has been removed."
        self.assertEqual(self.restaurant.waiters, [{'name': 'Ivan'}])
        self.assertEqual(result, message)

    def test_get_total_earnings_with_zero_earning(self):
        result = self.restaurant.get_total_earnings()
        self.assertEqual(result, 0)

    def test_get_total_earnings(self):
        self.restaurant.waiters = [
            {'name': 'Ivan', 'total_earnings': 5},
            {'name': 'Go6o', 'total_earnings': 5},
        ]
        result = self.restaurant.get_total_earnings()
        self.assertEqual(result, 10)

    def test_get_waiters_with_min_earnings_given(self):
        self.restaurant.waiters = [
            {'name': 'Ivan', 'total_earnings': 5},
            {'name': 'Go6o', 'total_earnings': 6},
        ]
        result = self.restaurant.get_waiters(min_earnings=5)
        self.assertEqual(result, [
            {'name': 'Ivan', 'total_earnings': 5},
            {'name': 'Go6o', 'total_earnings': 6}
        ])

    def test_get_waiters_with_max_earnings_given(self):
        self.restaurant.waiters = [
            {'name': 'Ivan', 'total_earnings': 5},
            {'name': 'Go6o', 'total_earnings': 6},
        ]
        result = self.restaurant.get_waiters(max_earnings=6)
        self.assertEqual(result, [
            {'name': 'Ivan', 'total_earnings': 5},
            {'name': 'Go6o', 'total_earnings': 6}
        ])

    def test_get_waiters_with_min_and_max_earnings_given(self):
        self.restaurant.waiters = [
            {'name': 'Ivan', 'total_earnings': 5},
            {'name': 'Go6o', 'total_earnings': 6},
        ]
        result = self.restaurant.get_waiters(max_earnings=6, min_earnings=5)
        self.assertEqual(result, [
            {'name': 'Ivan', 'total_earnings': 5},
            {'name': 'Go6o', 'total_earnings': 6}
        ])


if __name__ == '__main__':
    main()



#######################################################################################################
# from project.restaurant import Restaurant
# from unittest import TestCase, main
#
#
# class RestaurantTest(TestCase):
#     def setUp(self):
#         self.restaurant = Restaurant("detelina", 2)
#         self.restaurant.waiters = []
#
#     def test_init(self):
#         self.assertEqual(self.restaurant.name, "detelina")
#         self.assertEqual(self.restaurant.capacity, 2)
#         self.assertEqual(self.restaurant.waiters, [])
#
#     def test_name_with_empty_string(self):
#         with self.assertRaises(ValueError) as ve:
#             self.restaurant.name = ""
#         self.assertEqual("Invalid name!", str(ve.exception))
#
#     def test_capacity_with_empty_negative_value(self):
#         with self.assertRaises(ValueError) as ve:
#             self.restaurant.capacity = - 1
#         self.assertEqual("Invalid capacity!", str(ve.exception))
#
#     def test_add_waiter_with_no_capacity(self):
#         self.restaurant.capacity = 0
#         res = self.restaurant.add_waiter("Gosho")
#         self.assertEqual(res, "No more places!")
#
#     def test_add_waiter(self):
#         res = self.restaurant.add_waiter("Gosho")
#         self.assertEqual("The waiter Gosho has been added.", res)
#         self.assertEqual([{'name': "Gosho"}], self.restaurant.waiters)
#
#     def test_add_waiter_with_existing_name(self):
#         self.restaurant.add_waiter("Gosho")
#         res = self.restaurant.add_waiter("Gosho")
#         self.assertEqual(f"The waiter Gosho already exists!", res)
#
#     def test_remove_waiter_with_not_existing_name(self):
#         self.restaurant.add_waiter("Gosho")
#         res = self.restaurant.remove_waiter("Ivan")
#         self.assertEqual("No waiter found with the name Ivan.", res)
#
#     def test_remove_waiter_with_existing_name(self):
#         self.restaurant.add_waiter("Gosho")
#         res = self.restaurant.remove_waiter("Gosho")
#         self.assertEqual("The waiter Gosho has been removed.", res)
#         self.assertEqual([], self.restaurant.waiters)
#
#     def test_get_total_earnings_with_zero(self):
#         res = self.restaurant.get_total_earnings()
#         self.assertEqual(res, 0)
#
#     def test_get_total_earnings(self):
#         self.restaurant.waiters = [
#             {'name': "Gosho", "total_earnings": 10},
#             {'name': "Ivan", "total_earnings": 20}
#         ]
#
#         res = self.restaurant.get_total_earnings()
#         self.assertEqual(res, 30)
#
#     def test_get_waiters_with_min_earnings_is_none_and_max_earnings_is_none(self):
#         res1 = self.restaurant.waiters = [
#             {'name': "Gosho", "total_earnings": 10},
#             {'name': "Ivan", "total_earnings": 20}
#         ]
#
#         res2 = self.restaurant.get_waiters()
#         self.assertEqual(res1, res2)
#
#     def test_get_waiters_with_min_earnings_is_not_none_and_max_earnings_is_not_none(self):
#         self.restaurant.waiters = [
#             {'name': "Gosho", "total_earnings": 10},
#             {'name': "Ivan", "total_earnings": 20},
#             {'name': "Pesho", "total_earnings": 30}
#         ]
#
#         res1 = self.restaurant.get_waiters(15, 25)
#         res2 = [{'name': "Ivan", "total_earnings": 20}]
#         self.assertEqual(res1, res2)
#
#     def test_get_waiters_with_min_earnings_is_not_none_and_max_earnings_is_none(self):
#         self.restaurant.waiters = [
#             {'name': "Gosho", "total_earnings": 10},
#             {'name': "Ivan", "total_earnings": 20},
#             {'name': "Pesho", "total_earnings": 30}
#         ]
#
#         res1 = self.restaurant.get_waiters(min_earnings=21)
#         res2 = [{'name': "Pesho", "total_earnings": 30}]
#         self.assertEqual(res1, res2)
#
#     def test_get_waiters_with_min_earnings_is_none_and_max_earnings_is_not_none(self):
#         self.restaurant.waiters = [
#             {'name': "Gosho", "total_earnings": 10},
#             {'name': "Ivan", "total_earnings": 20},
#             {'name': "Pesho", "total_earnings": 30}
#         ]
#
#         res1 = self.restaurant.get_waiters(max_earnings=15)
#         res2 = [{'name': "Gosho", "total_earnings": 10}]
#         self.assertEqual(res1, res2)
#
#
# if __name__ == "__main__":
#     main()

