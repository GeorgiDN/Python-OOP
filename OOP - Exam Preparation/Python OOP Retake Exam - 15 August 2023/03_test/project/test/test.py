from project.trip import Trip
from unittest import TestCase, main


class TripTest(TestCase):
    def setUp(self):
        self.trip = Trip(100000.0, 2, True)

    def test_init(self):
        self.assertEqual(100000.0, self.trip.budget)
        self.assertEqual(2, self.trip.travelers)
        self.assertTrue(self.trip.is_family)
        self.assertEqual({}, self.trip.booked_destinations_paid_amounts)

    def test_travelers_with_zero_travelers(self):
        with self.assertRaises(ValueError) as ve:
            self.trip.travelers = 0
        self.assertEqual('At least one traveler is required!', str(ve.exception))

    def test_travelers_with_negative_travelers(self):
        with self.assertRaises(ValueError) as ve:
            self.trip.travelers = -1
        self.assertEqual('At least one traveler is required!', str(ve.exception))

    def test_is_family__True_set_to_False(self):
        self.trip2 = Trip(1000.0, 1, True)
        self.assertEqual(1000, self.trip2.budget)
        self.assertEqual(1, self.trip2.travelers)
        self.assertFalse(self.trip2.is_family)
        self.assertEqual(self.trip2.booked_destinations_paid_amounts, {})

    def test_travelers_with_one_traveler(self):
        self.trip.travelers = 1
        self.assertEqual(self.trip.travelers, 1)

    def test_travelers_with_two_travelers(self):
        self.trip.travelers = 2
        self.assertEqual(self.trip.travelers, 2)

    def test_is_family_with_one_traveler_is_family_false(self):
        self.trip2 = Trip(100000.0, 1, False)
        result = self.trip2.is_family
        self.assertFalse(result)

    def test_is_family_with_two_travelers_is_family_true(self):
        self.trip2 = Trip(100000.0, 2, True)
        result = self.trip2.is_family
        self.assertTrue(result)

    #DOES not work with this test
    # def test_book_a_trip_with_invalid_destination_return_message(self):
    #     self.trip = Trip(100000.0, 2, True)
    #     result = self.trip.book_a_trip("Invalid")
    #     expected_message = 'This destination is not in our offers, please choose a new one!'
    #     self.assertTrue(result, expected_message)

    def test_book_trip_with_invalid_destination_return_message_is_family_true(self):
        trip = Trip(1000.0, 2, True)
        res = trip.book_a_trip("Makedoniq")
        expected_message = 'This destination is not in our offers, please choose a new one!'
        self.assertEqual(res, expected_message)

    def test_book_a_trip_with_not_enough_budget_is_family_false(self):
        self.trip2 = Trip(100.0, 1, False)
        res = self.trip2.book_a_trip("New Zealand")
        ex_message = 'Your budget is not enough!'
        self.assertEqual(res, ex_message)

    def test_book_a_trip_with_not_enough_budget_is_family_true(self):
        self.trip2 = Trip(100.0, 2, True)
        res = self.trip2.book_a_trip("New Zealand")
        ex_message = 'Your budget is not enough!'
        self.assertEqual(res, ex_message)

    def test_book_a_trip_with_enough_budget_is_family_false(self):
        self.trip2 = Trip(100000.0, 1, False)
        res = self.trip2.book_a_trip("Bulgaria")
        ex_message = 'Successfully booked destination Bulgaria! Your budget left is 99500.00'
        self.assertEqual(res, ex_message)
        self.assertEqual(99500.0, self.trip2.budget)
        self.assertEqual(self.trip2.booked_destinations_paid_amounts, {"Bulgaria": 500.0})

    def test_book_a_trip_with_enough_budget_is_family_true(self):
        res = self.trip.book_a_trip("Bulgaria")
        ex_message = 'Successfully booked destination Bulgaria! Your budget left is 99100.00'
        self.assertEqual(res, ex_message)
        self.assertEqual(99100.0, self.trip.budget)
        self.assertEqual(self.trip.booked_destinations_paid_amounts, {"Bulgaria": 900.0})

    def test_booking_status_with_no_booking_yes(self):
        res = self.trip.booking_status()
        ex_message = f'No bookings yet. Budget: {self.trip.budget:.2f}'
        self.assertEqual(res, ex_message)

    def test_booking_status_with_already_made_bookings(self):
        self.trip2 = Trip(100000.0, 1, False)
        self.trip2.book_a_trip("Bulgaria")
        self.trip2.book_a_trip("New Zealand")
        self.assertEqual(self.trip2.booked_destinations_paid_amounts, {"Bulgaria": 500.0, "New Zealand": 7500.0})
        result = self.trip2.booking_status()
        expected_info = "Booked Destination: Bulgaria\n" \
                        "Paid Amount: 500.00\n" \
                        "Booked Destination: New Zealand\n" \
                        "Paid Amount: 7500.00\n" \
                        "Number of Travelers: 1\n" \
                        "Budget Left: 92000.00"
        self.assertEqual(result, expected_info)

if __name__ == "__main__":
    main()







# from project.trip import Trip
# from unittest import TestCase, main
#
#
# class TripTest(TestCase):
#
#     def test_01_init(self):
#         trip = Trip(1000.0, 2, True)
#         self.assertEqual(1000, trip.budget)
#         self.assertEqual(2, trip.travelers)
#         self.assertEqual(True, trip.is_family)
#         self.assertEqual(trip.booked_destinations_paid_amounts, {})
#
#     def test_02_travelers_less_than_1_raises(self):
#
#         with self.assertRaises(ValueError) as ve:
#             trip = Trip(1000.0, 0, False)
#
#         expected_message = 'At least one traveler is required!'
#         output = str(ve.exception)
#         self.assertEqual(expected_message, output)
#
#     def test_03_negative_travelers_raises(self):
#         with self.assertRaises(ValueError) as ve:
#             trip = Trip(1000.0, -1, False)
#
#         expected_message = 'At least one traveler is required!'
#         output = str(ve.exception)
#         self.assertEqual(expected_message, output)
#
#     def test_04_is_family__True_set_to_False(self):
#         trip = Trip(1000.0, 1, True)
#         self.assertEqual(1000, trip.budget)
#         self.assertEqual(1, trip.travelers)
#         self.assertFalse(trip.is_family)
#         self.assertEqual(trip.booked_destinations_paid_amounts, {})
#
#     def test_05_travelers_setter_with_1_traveler(self):
#         trip = Trip(1000.0, 1, False)
#         self.assertEqual(1, trip.travelers)
#
#     def test_06_travelers_setter_with_2_travelers(self):
#         trip = Trip(1000.0, 2, True)
#         self.assertEqual(2, trip.travelers)
#
#     def test_07_is_family_false(self):
#         trip = Trip(1000.0, 1, False)
#         self.assertFalse(trip.is_family)
#
#     def test_08_is_family_true(self):
#         trip = Trip(1000.0, 2, True)
#         self.assertTrue(trip.is_family)
#
#     def test_09_book_trip_not_valid_destination_return_message(self):
#         trip = Trip(1000.0, 2, True)
#         res = trip.book_a_trip("Makedoniq")
#         expected_message = 'This destination is not in our offers, please choose a new one!'
#         self.assertEqual(res, expected_message)
#
#     def test_10_book_trip_with_not_enough_budget_return_message(self):
#         trip = Trip(1000.0, 2, True)
#         res = trip.book_a_trip("Australia")
#         expected_message = 'Your budget is not enough!'
#         self.assertEqual(res, expected_message)
#
#     def test_11_book_trip_required_price_and_budget_is_family_false(self):
#         trip = Trip(1000.0, 2, False)
#         res = trip.book_a_trip("Bulgaria")
#         expected_message = 'Successfully booked destination Bulgaria! Your budget left is 0.00'
#         self.assertEqual(res, expected_message)
#         self.assertEqual(trip.booked_destinations_paid_amounts, {"Bulgaria": 1000.0})
#
#     def test_12_book_trip_required_price_and_budget_is_family_true(self):
#         trip = Trip(1000.0, 2, True)
#         res = trip.book_a_trip("Bulgaria")
#         expected_message = 'Successfully booked destination Bulgaria! Your budget left is 100.00'
#         self.assertEqual(res, expected_message)
#         self.assertEqual(trip.booked_destinations_paid_amounts, {"Bulgaria": 900.0})
#
#     def test_13_booking_status_with_no_paid_amounts(self):
#         trip = Trip(1000.0, 2, True)
#         res = trip.booking_status()
#         expected_message = f'No bookings yet. Budget: 1000.00'
#         self.assertEqual(res, expected_message)
#
#     def test_14_booking_status_with_paid_amounts(self):
#         trip = Trip(30000.0, 2, True)
#         trip.book_a_trip("Bulgaria")
#         trip.book_a_trip("New Zealand")
#
#         self.assertEqual(trip.booked_destinations_paid_amounts, {"Bulgaria": 900.0, "New Zealand": 13500.0})
#         res = trip.booking_status()
#         output = "Booked Destination: Bulgaria\nPaid Amount: 900.00\n" \
#               "Booked Destination: New Zealand\nPaid Amount: 13500.00\n" \
#               "Number of Travelers: 2\nBudget Left: 15600.00"
#         self.assertEqual(res, output)
#
#
# if __name__ == "__main__":
#     main()
