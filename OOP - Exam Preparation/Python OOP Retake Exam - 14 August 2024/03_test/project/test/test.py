from project.furniture import Furniture
from unittest import TestCase, main


class FurnitureTestCase(TestCase):
    def setUp(self):
        self.furniture = Furniture("Ikea", 100.0, (20, 30, 40))

    def test_init(self):
        self.assertIsInstance(self.furniture, Furniture)
        self.assertEqual(self.furniture.model, "Ikea")
        self.assertEqual(self.furniture.price, 100.0)
        self.assertEqual(self.furniture.dimensions, (20, 30, 40))
        self.assertTrue(self.furniture.in_stock)
        self.assertIsNone(self.furniture.weight)

    def test_model_with_empty_string(self):
        with self.assertRaises(ValueError) as ve:
            self.furniture.model = ""
        self.assertEqual(str(ve.exception), "Model must be a non-empty string with a maximum length of 50 characters.")

    def test_model_with_white_spaces(self):
        with self.assertRaises(ValueError) as ve:
            self.furniture.model = "  "
        self.assertEqual(str(ve.exception), "Model must be a non-empty string with a maximum length of 50 characters.")

    def test_model_with_length_greater_than_fifty(self):
        with self.assertRaises(ValueError) as ve:
            invalid_model = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaaa"
            self.furniture.model = invalid_model
        self.assertEqual(str(ve.exception), "Model must be a non-empty string with a maximum length of 50 characters.")

    def test_model_with_valid_length(self):
        self.furniture.model = "Ikea"
        self.assertEqual(self.furniture.model, "Ikea")

    def test_price_with_negative_value_raise_error(self):
        with self.assertRaises(ValueError) as ve:
            self.furniture.price = -1
        self.assertEqual(str(ve.exception), "Price must be a non-negative number.")

    def test_price_with_zero_value(self):
        self.furniture.price = 0
        self.assertEqual(self.furniture.price, 0)

    def test_price_with_value_greater_than_zero(self):
        self.furniture.price = 10
        self.assertEqual(self.furniture.price, 10)

    def test_dimensions_with_zero_values_given(self):
        with self.assertRaises(ValueError) as ve:
            self.furniture.dimensions = ()
        self.assertEqual(str(ve.exception), "Dimensions tuple must contain 3 integers.")

    def test_dimensions_with_one_values_given(self):
        with self.assertRaises(ValueError) as ve:
            self.furniture.dimensions = (1,)
        self.assertEqual(str(ve.exception), "Dimensions tuple must contain 3 integers.")

    def test_dimensions_with_two_values_given(self):
        with self.assertRaises(ValueError) as ve:
            self.furniture.dimensions = (1, 2)
        self.assertEqual(str(ve.exception), "Dimensions tuple must contain 3 integers.")

    def test_dimensions_with_four_values_given(self):
        with self.assertRaises(ValueError) as ve:
            self.furniture.dimensions = (1, 2, 3, 4)
        self.assertEqual(str(ve.exception), "Dimensions tuple must contain 3 integers.")

    def test_dimensions_with_negative_value(self):
        with self.assertRaises(ValueError) as ve:
            self.furniture.dimensions = (1, 2, -3)
        self.assertEqual(str(ve.exception), "Dimensions tuple must contain integers greater than zero.")

    def test_dimensions_with_zero_value(self):
        with self.assertRaises(ValueError) as ve:
            self.furniture.dimensions = (1, 2, 0)
        self.assertEqual(str(ve.exception), "Dimensions tuple must contain integers greater than zero.")

    def test_dimensions_with_three_values_given(self):
        self.furniture.dimensions = (1, 2, 3)
        self.assertEqual(self.furniture.dimensions, (1, 2, 3))

    def test_weight_with_negative_value(self):
        with self.assertRaises(ValueError) as ve:
            self.furniture.weight = -1
        self.assertEqual(str(ve.exception), "Weight must be greater than zero.")

    def test_weight_with_zero_value(self):
        with self.assertRaises(ValueError) as ve:
            self.furniture.weight = 0
        self.assertEqual(str(ve.exception), "Weight must be greater than zero.")

    def test_weight_with_value_greater_than_zero(self):
        self.furniture.weight = 10
        self.assertEqual(self.furniture.weight, 10)

    def test_available_status_unavailable(self):
        self.furniture.in_stock = False
        res = self.furniture.get_available_status()
        self.assertEqual("Model: Ikea is currently unavailable.", res)

    def test_available_status_available(self):
        res = self.furniture.get_available_status()
        self.assertEqual("Model: Ikea is currently in stock.", res)

    def test_get_specifications_with_empty_weight(self):
        res = self.furniture.get_specifications()
        message = (f"Model: {self.furniture.model} has the following dimensions: "
                   f"20mm x 30mm x 40mm and weighs: N/A")
        self.assertEqual(message, res)

    def test_get_specifications_with_not_empty_weight(self):
        self.furniture.weight = 20
        res = self.furniture.get_specifications()
        message = (f"Model: {self.furniture.model} has the following dimensions: "
                   f"20mm x 30mm x 40mm and weighs: 20")
        self.assertEqual(message, res)


if __name__ == '__main__':
    main()

