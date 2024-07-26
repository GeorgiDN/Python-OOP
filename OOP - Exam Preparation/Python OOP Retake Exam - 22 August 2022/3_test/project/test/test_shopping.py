from project.shopping_cart import ShoppingCart
from unittest import TestCase, main


class ShoppingCartTest(TestCase):
    def setUp(self):
        self.cart = ShoppingCart("Cart", 100.0)

    def test_init(self):
        self.assertIsInstance(self.cart, ShoppingCart)
        self.assertEqual(self.cart.shop_name, "Cart")
        self.assertEqual(self.cart.budget, 100.0)
        self.assertEqual(self.cart.products, {})

    def test_shop_name_with_digits(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = "Cart1"
        message = "Shop must contain only letters and must start with capital letter!"
        self.assertEqual(str(ve.exception), message)

    def test_shop_name_with_not_capital_letter(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.shop_name = "cart"
        message = "Shop must contain only letters and must start with capital letter!"
        self.assertEqual(str(ve.exception), message)

    def test_shop_name_with_proper_name(self):
        self.cart.shop_name = "Cart"
        self.assertEqual(self.cart.shop_name, "Cart")

    def test_add_to_cart_with_sum_greater_than_100_raise_message(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart("product1", 120.0)
        message = "Product product1 cost too much!"
        self.assertEqual(str(ve.exception), message)

    def test_add_to_cart_with_sum_greater_equal_to_100_raise_message(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.add_to_cart("product1", 100.0)
        message = "Product product1 cost too much!"
        self.assertEqual(str(ve.exception), message)

    def test_add_to_cart_with_sum_less_than(self):
        result = self.cart.add_to_cart("product1", 10.0)
        message = "product1 product was successfully added to the cart!"
        self.assertEqual(result, message)
        self.assertEqual(self.cart.products, {"product1": 10.0})

    def test_remove_from_cart_with_not_product_in_car_raise_message(self):
        with self.assertRaises(ValueError) as ve:
            self.cart.remove_from_cart("product1")
        message = f"No product with name product1 in the cart!"
        self.assertEqual(str(ve.exception), message)

    def test_remove_from_cart_with_existing_name(self):
        self.cart.add_to_cart("product1", 10.0)
        self.assertEqual(self.cart.products, {"product1": 10.0})
        result = self.cart.remove_from_cart("product1")
        message = "Product product1 was successfully removed from the cart!"
        self.assertEqual(result, message)
        self.assertEqual(self.cart.products, {})

    def test_add_multiple_items_and_remove_some(self):
        self.cart.add_to_cart("product1", 10.0)
        self.cart.add_to_cart("product2", 20.0)
        self.cart.add_to_cart("product3", 30.0)
        self.assertEqual(self.cart.products, {"product1": 10.0, "product2": 20.0, "product3": 30.0})
        self.cart.remove_from_cart("product2")
        self.assertEqual(self.cart.products, {"product1": 10.0, "product3": 30.0})

    def test_buy_products_with_not_enough_budget_raise_message(self):
        self.cart.budget = 10
        self.cart.add_to_cart("product1", 10.0)
        self.cart.add_to_cart("product2", 10.0)
        self.assertEqual(self.cart.products, {"product1": 10.0, "product2": 10.0})
        with self.assertRaises(ValueError) as ve:
            self.cart.buy_products()
        message = "Not enough money to buy the products! Over budget with 10.00lv!"
        self.assertEqual(str(ve.exception), message)

    def test_buy_products_with_enough_budget(self):
        self.cart.add_to_cart("product1", 10.0)
        self.cart.add_to_cart("product2", 10.0)
        self.assertEqual(self.cart.products, {"product1": 10.0, "product2": 10.0})
        result = self.cart.buy_products()
        message = f'Products were successfully bought! Total cost: 20.00lv.'
        self.assertEqual(result, message)

    def test_add_method(self):
        self.cart.add_to_cart("product1", 10.0)
        self.assertEqual(self.cart.products, {"product1": 10.0})

        other_cart = ShoppingCart("Othercart", 100.0)
        other_cart.add_to_cart("product2", 10.0)
        self.assertEqual(other_cart.products, {"product2": 10.0})

        new_shopping_cart = self.cart.__add__(other_cart)
        new_shop_name = f"{self.cart.shop_name}{other_cart.shop_name}"
        new_budget = self.cart.budget + other_cart.budget

        self.assertEqual(new_shopping_cart.shop_name, new_shop_name)
        self.assertEqual(new_shopping_cart.budget, new_budget)
        self.assertIsInstance(new_shopping_cart, ShoppingCart)
        self.assertEqual(new_shopping_cart.products, {"product1": 10.0, "product2": 10.0})


if __name__ == '__main__':
    main()
