from project.furniture import Furniture
from unittest import TestCase, main


class TestFurniture(TestCase):
    def setUp(self):
        self.furniture = Furniture('Model1', 100.0, (10, 20, 30))

    def test_init(self):
        self.assertIsInstance(self.furniture, Furniture)
        self.assertEqual(self.furniture.model, 'Model1')
        self.assertEqual(self.furniture.price, 100.0)
        self.assertEqual(self.furniture.dimensions, (10, 20, 30))
        self.assertTrue(self.furniture.in_stock)

    def test_model_with_empty_string(self):
        with self.assertRaises(ValueError) as ve:
            self.furniture.model = ''
        message = "Model must be a non-empty string with a maximum length of 50 characters."
        self.assertEqual(str(ve.exception), message)

    def test_model_with_len_string_greater_than_50(self):
        with self.assertRaises(ValueError) as ve:
            self.furniture.model = ''.join('a' for _ in range(51))
        message = "Model must be a non-empty string with a maximum length of 50 characters."
        self.assertEqual(str(ve.exception), message)

    def test_price_with_negative_values(self):
        with self.assertRaises(ValueError) as ve:
            self.furniture.price = -1
        message = "Price must be a non-negative number."
        self.assertEqual(str(ve.exception), message)

    def test_dimensions_with_empty_tuple(self):
        with self.assertRaises(ValueError) as ve:
            self.furniture.dimensions = ()
        message = "Dimensions tuple must contain 3 integers."
        self.assertEqual(str(ve.exception), message)

    def test_dimensions_with_len_equal_to_one(self):
        with self.assertRaises(ValueError) as ve:
            self.furniture.dimensions = (1,)
        message = "Dimensions tuple must contain 3 integers."
        self.assertEqual(str(ve.exception), message)

    def test_dimensions_with_len_equal_to_two(self):
        with self.assertRaises(ValueError) as ve:
            self.furniture.dimensions = (1, 2)
        message = "Dimensions tuple must contain 3 integers."
        self.assertEqual(str(ve.exception), message)

    def test_dimensions_with_len_more_than_3(self):
        with self.assertRaises(ValueError) as ve:
            self.furniture.dimensions = (1, 2, 3, 4)
        message = "Dimensions tuple must contain 3 integers."
        self.assertEqual(str(ve.exception), message)

    def test_dimensions_with_one_value_equal_to_zero(self):
        with self.assertRaises(ValueError) as ve:
            self.furniture.dimensions = (0, 2, 3)
        message = "Dimensions tuple must contain integers greater than zero."
        self.assertEqual(str(ve.exception), message)

    def test_dimensions_with_one_negative_value(self):
        with self.assertRaises(ValueError) as ve:
            self.furniture.dimensions = (-1, 2, 3)
        message = "Dimensions tuple must contain integers greater than zero."
        self.assertEqual(str(ve.exception), message)

    def test_weight_with_zero_value(self):
        with self.assertRaises(ValueError) as ve:
            self.furniture.weight = 0
        message = "Weight must be greater than zero."
        self.assertEqual(str(ve.exception), message)

    def test_weight_with_negative_value(self):
        with self.assertRaises(ValueError) as ve:
            self.furniture.weight = -1
        message = "Weight must be greater than zero."
        self.assertEqual(str(ve.exception), message)

    def test_weight_with_positive_value(self):
        self.furniture.weight = 10
        self.assertEqual(self.furniture.weight, 10)

    def test_get_available_status_in_stock(self):
        result = self.furniture.get_available_status()
        message = f"Model: Model1 is currently in stock."
        self.assertEqual(result, message)

    def test_get_available_status_unavailable(self):
        self.furniture.in_stock = False
        result = self.furniture.get_available_status()
        message = "Model: Model1 is currently unavailable."
        self.assertEqual(result, message)

    def test_get_specifications_with_none_weight(self):
        result = self.furniture.get_specifications()
        message = (f"Model: {self.furniture.model} has the following dimensions: "
                   f"10mm x 20mm x 30mm and weighs: N/A")
        self.assertEqual(result, message)

    def test_get_specifications_with_set_weight(self):
        self.furniture.weight = 10
        result = self.furniture.get_specifications()
        message = (f"Model: {self.furniture.model} has the following dimensions: "
                   f"10mm x 20mm x 30mm and weighs: 10")
        self.assertEqual(result, message)


if __name__ == '__main__':
    main()



#######################################################################################################################
# from project.furniture import Furniture
# from unittest import TestCase, main
#
#
# class FurnitureTestCase(TestCase):
#     def setUp(self):
#         self.furniture = Furniture("Ikea", 100, (10, 20, 30), True)
#
#     def test_init(self):
#         self.assertIsInstance(self.furniture, Furniture)
#         self.assertEqual(self.furniture.model, "Ikea")
#         self.assertEqual(self.furniture.price, 100)
#         self.assertEqual(self.furniture.dimensions, (10, 20, 30))
#         self.assertTrue(self.furniture.in_stock)
#         self.assertIsNone(self.furniture.weight)
#
#     def test_model_empty(self):
#         with self.assertRaises(ValueError) as ve:
#             self.furniture.model = ""
#         error = "Model must be a non-empty string with a maximum length of 50 characters."
#         self.assertEqual(str(ve.exception), error)
#
#     def test_model_len_greater_than_50(self):
#         with self.assertRaises(ValueError) as ve:
#             self.furniture.model = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
#         error = "Model must be a non-empty string with a maximum length of 50 characters."
#         self.assertEqual(str(ve.exception), error)
#
#     def test_price_negative(self):
#         with self.assertRaises(ValueError) as ve:
#             self.furniture.price = -100
#         error = "Price must be a non-negative number."
#         self.assertEqual(str(ve.exception), error)
#
#     def test_dimensions_len_0(self):
#         with self.assertRaises(ValueError) as ve:
#             self.furniture.dimensions = ()
#         error = "Dimensions tuple must contain 3 integers."
#         self.assertEqual(str(ve.exception), error)
#
#     def test_dimensions_len_1(self):
#         with self.assertRaises(ValueError) as ve:
#             self.furniture.dimensions = ()
#         error = "Dimensions tuple must contain 3 integers."
#         self.assertEqual(str(ve.exception), error)
#
#     def test_dimensions_len_2(self):
#         with self.assertRaises(ValueError) as ve:
#             self.furniture.dimensions = ()
#         error = "Dimensions tuple must contain 3 integers."
#         self.assertEqual(str(ve.exception), error)
#
#     def test_dimensions_len_4(self):
#         with self.assertRaises(ValueError) as ve:
#             self.furniture.dimensions = ()
#         error = "Dimensions tuple must contain 3 integers."
#         self.assertEqual(str(ve.exception), error)
#
#     def test_dimensions_negative_value(self):
#         with self.assertRaises(ValueError) as ve:
#             self.furniture.dimensions = (-1, 20,30)
#         error = "Dimensions tuple must contain integers greater than zero."
#         self.assertEqual(str(ve.exception), error)
#
#     def test_dimensions_zero_value(self):
#         with self.assertRaises(ValueError) as ve:
#             self.furniture.dimensions = (20, 0,30)
#         error = "Dimensions tuple must contain integers greater than zero."
#         self.assertEqual(str(ve.exception), error)
#
#     def test_weight_zero_value(self):
#         with self.assertRaises(ValueError) as ve:
#             self.furniture.weight = 0
#         error = "Weight must be greater than zero."
#         self.assertEqual(str(ve.exception), error)
#
#     def test_weight_negative_value(self):
#         with self.assertRaises(ValueError) as ve:
#             self.furniture.weight = -1
#         error = "Weight must be greater than zero."
#         self.assertEqual(str(ve.exception), error)
#
#     def test_get_available_status_available(self):
#         res = self.furniture.get_available_status()
#         expect = "Model: Ikea is currently "
#         expect += "in stock."
#         self.assertEqual(res, expect)
#
#     def test_get_available_status_unavailable(self):
#         self.furniture.in_stock= False
#         res = self.furniture.get_available_status()
#         expect = "Model: Ikea is currently "
#         expect += "unavailable."
#         self.assertEqual(res, expect)
#
#     def test_get_specifications_empty_weight(self):
#         res = self.furniture.get_specifications()
#         expect = "Model: Ikea has the following dimensions: "
#         expect += "10mm x 20mm x 30mm and weighs: N/A"
#         self.assertEqual(res, expect)
#
#     def test_get_specifications_weight_not_none(self):
#         self.furniture.weight = 80
#         res = self.furniture.get_specifications()
#         expect = "Model: Ikea has the following dimensions: "
#         expect += "10mm x 20mm x 30mm and weighs: 80"
#         self.assertEqual(res, expect)
#
#
# if __name__ == '__main__':
#     main()


#######################################################################################################################
# from project.furniture import Furniture
# from unittest import TestCase, main
#
#
# class FurnitureTestCase(TestCase):
#     def setUp(self):
#         self.furniture = Furniture("Ikea", 100.0, (20, 30, 40))
#
#     def test_init(self):
#         self.assertIsInstance(self.furniture, Furniture)
#         self.assertEqual(self.furniture.model, "Ikea")
#         self.assertEqual(self.furniture.price, 100.0)
#         self.assertEqual(self.furniture.dimensions, (20, 30, 40))
#         self.assertTrue(self.furniture.in_stock)
#         self.assertIsNone(self.furniture.weight)
#
#     def test_model_with_empty_string(self):
#         with self.assertRaises(ValueError) as ve:
#             self.furniture.model = ""
#         self.assertEqual(str(ve.exception), "Model must be a non-empty string with a maximum length of 50 characters.")
#
#     def test_model_with_white_spaces(self):
#         with self.assertRaises(ValueError) as ve:
#             self.furniture.model = "  "
#         self.assertEqual(str(ve.exception), "Model must be a non-empty string with a maximum length of 50 characters.")
#
#     def test_model_with_length_greater_than_fifty(self):
#         with self.assertRaises(ValueError) as ve:
#             invalid_model = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
#             self.furniture.model = invalid_model
#         self.assertEqual(str(ve.exception), "Model must be a non-empty string with a maximum length of 50 characters.")
#
#     def test_model_with_valid_length(self):
#         self.furniture.model = "Ikea"
#         self.assertEqual(self.furniture.model, "Ikea")
#
#     def test_price_with_negative_value_raise_error(self):
#         with self.assertRaises(ValueError) as ve:
#             self.furniture.price = -1
#         self.assertEqual(str(ve.exception), "Price must be a non-negative number.")
#
#     def test_price_with_zero_value(self):
#         self.furniture.price = 0
#         self.assertEqual(self.furniture.price, 0)
#
#     def test_price_with_value_greater_than_zero(self):
#         self.furniture.price = 10
#         self.assertEqual(self.furniture.price, 10)
#
#     def test_dimensions_with_zero_values_given(self):
#         with self.assertRaises(ValueError) as ve:
#             self.furniture.dimensions = ()
#         self.assertEqual(str(ve.exception), "Dimensions tuple must contain 3 integers.")
#
#     def test_dimensions_with_one_values_given(self):
#         with self.assertRaises(ValueError) as ve:
#             self.furniture.dimensions = (1,)
#         self.assertEqual(str(ve.exception), "Dimensions tuple must contain 3 integers.")
#
#     def test_dimensions_with_two_values_given(self):
#         with self.assertRaises(ValueError) as ve:
#             self.furniture.dimensions = (1, 2)
#         self.assertEqual(str(ve.exception), "Dimensions tuple must contain 3 integers.")
#
#     def test_dimensions_with_four_values_given(self):
#         with self.assertRaises(ValueError) as ve:
#             self.furniture.dimensions = (1, 2, 3, 4)
#         self.assertEqual(str(ve.exception), "Dimensions tuple must contain 3 integers.")
#
#     def test_dimensions_with_negative_value(self):
#         with self.assertRaises(ValueError) as ve:
#             self.furniture.dimensions = (1, 2, -3)
#         self.assertEqual(str(ve.exception), "Dimensions tuple must contain integers greater than zero.")
#
#     def test_dimensions_with_zero_value(self):
#         with self.assertRaises(ValueError) as ve:
#             self.furniture.dimensions = (1, 2, 0)
#         self.assertEqual(str(ve.exception), "Dimensions tuple must contain integers greater than zero.")
#
#     def test_dimensions_with_three_values_given(self):
#         self.furniture.dimensions = (1, 2, 3)
#         self.assertEqual(self.furniture.dimensions, (1, 2, 3))
#
#     def test_weight_with_negative_value(self):
#         with self.assertRaises(ValueError) as ve:
#             self.furniture.weight = -1
#         self.assertEqual(str(ve.exception), "Weight must be greater than zero.")
#
#     def test_weight_with_zero_value(self):
#         with self.assertRaises(ValueError) as ve:
#             self.furniture.weight = 0
#         self.assertEqual(str(ve.exception), "Weight must be greater than zero.")
#
#     def test_weight_with_value_greater_than_zero(self):
#         self.furniture.weight = 10
#         self.assertEqual(self.furniture.weight, 10)
#
#     def test_available_status_unavailable(self):
#         self.furniture.in_stock = False
#         res = self.furniture.get_available_status()
#         self.assertEqual("Model: Ikea is currently unavailable.", res)
#
#     def test_available_status_available(self):
#         res = self.furniture.get_available_status()
#         self.assertEqual("Model: Ikea is currently in stock.", res)
#
#     def test_get_specifications_with_empty_weight(self):
#         res = self.furniture.get_specifications()
#         message = (f"Model: {self.furniture.model} has the following dimensions: "
#                    f"20mm x 30mm x 40mm and weighs: N/A")
#         self.assertEqual(message, res)
#
#     def test_get_specifications_with_not_empty_weight(self):
#         self.furniture.weight = 20
#         res = self.furniture.get_specifications()
#         message = (f"Model: {self.furniture.model} has the following dimensions: "
#                    f"20mm x 30mm x 40mm and weighs: 20")
#         self.assertEqual(message, res)
#
#
# if __name__ == '__main__':
#     main()
