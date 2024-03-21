from project.product import Product
from project.food import Food
from project.drink import Drink


class ProductRepository:
    def __init__(self):
        self.products = []

    def add(self, product: Product):
        self.products.append(product)

    def find(self, product_name: str):
        searched_product = self._find_product_by_name(product_name)
        return searched_product

    def remove(self, product_name):
        searched_product = self._find_product_by_name(product_name)
        if searched_product is not None:
            return self.products.remove(searched_product)

    def __repr__(self):
        # result = []
        # for item in self.products:
        #     result.append(f"{item.name}: {item.quantity}")
        # return '\n'.join(result)
        return '\n'.join(f"{item.name}: {item.quantity}" for item in self.products)

    ###
    def _find_product_by_name(self, pr_name):
        searched_product = next((p for p in self.products if p.name == pr_name), None)
        return searched_product
