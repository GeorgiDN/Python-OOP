from project.products.chair import Chair
from project.products.hobby_horse import HobbyHorse
from project.stores.furniture_store import FurnitureStore
from project.stores.toy_store import ToyStore


class FactoryManager:
    VALID_PRODUCTS = {"Chair": Chair, "HobbyHorse": HobbyHorse}
    VALID_STORES = {"FurnitureStore": FurnitureStore, "ToyStore": ToyStore}

    def __init__(self, name: str):
        self.name = name
        self.income: float = 0.0
        self.products: list = []
        self.stores: list = []

    def produce_item(self, product_type: str, model: str, price: float):
        if product_type not in self.VALID_PRODUCTS:
            raise Exception("Invalid product type!")

        new_product = self.VALID_PRODUCTS[product_type](model, price)
        self.products.append(new_product)
        return f"A product of sub-type {new_product.sub_type} was produced."

    def register_new_store(self, store_type: str, name: str, location: str):
        if store_type not in self.VALID_STORES:
            raise Exception(f"{store_type} is an invalid type of store!")

        new_store = self.VALID_STORES[store_type](name, location)
        self.stores.append(new_store)
        return f"A new {store_type} was successfully registered."

    def sell_products_to_store(self, store, *products):
        if store.capacity < len(products):
            return f"Store {store.name} has no capacity for this purchase."

        searched_type = ""
        num_of_purchased_products = 0

        if store.__class__.__name__ == "FurnitureStore":
            searched_type = "Furniture"
        elif store.__class__.__name__ == "ToyStore":
            searched_type = "Toys"

        for product in products:
            if product.sub_type == searched_type:
                num_of_purchased_products += 1
                self.products.remove(product)
                store.products.append(product)
                store.capacity -= 1
                self.income += product.price

        if num_of_purchased_products > 0:
            return f"Store {store.name} successfully purchased {num_of_purchased_products} items."

        return "Products do not match in type. Nothing sold."

    def unregister_store(self, store_name: str):
        store = self.find_store_by_name(self.stores, store_name)
        if not store:
            raise Exception("No such store!")

        if store.products:
            return "The store is still having products in stock! Unregistering is inadvisable."

        self.stores.remove(store)
        return f"Successfully unregistered store {store_name}, location: {store.location}."

    def discount_products(self, product_model: str):
        products_count = 0

        for product in self.products:
            if product.model == product_model:
                products_count += 1
                product.discount()

        return f"Discount applied to {products_count} products with model: {product_model}"

    def request_store_stats(self, store_name: str):
        store = self.find_store_by_name(self.stores, store_name)
        if not store:
            return "There is no store registered under this name!"

        return store.store_stats()

    def statistics(self):
        result = [f"Factory: {self.name}"]
        result.append(f"Income: {self.income:.2f}")
        result.append("***Products Statistics***")

        sorted_products = sorted(self.products, key=lambda p: p.model)
        products_sum_price = sum([p.price for p in self.products])
        result.append(f"Unsold Products: {len(self.products)}. Total net price: {products_sum_price:.2f}")

        products_data = {}
        for product in sorted_products:
            if product.model not in products_data:
                products_data[product.model] = 0
            products_data[product.model] += 1

        for product_model, qty in products_data.items():
            result.append(f"{product_model}: {qty}")

        result.append(f"***Partner Stores: {len(self.stores)}***")
        sorted_stores = sorted(self.stores, key=lambda s: s.name)
        for store in sorted_stores:
            result.append(f"{store.name}")

        return "\n".join(result)

    @staticmethod
    def find_store_by_name(lst, store_name):
        store = next((s for s in lst if s.name == store_name), None)
        return store


# Initialize the FactoryManager
# factory_manager = FactoryManager("Cool Factory")
#
# # Produce some items
# print(factory_manager.produce_item("Chair", "Classic", 80.0))
# print(factory_manager.produce_item("Chair", "Modern", 100.0))
# print(factory_manager.produce_item("Chair", "Modern", 200.0))
# print(factory_manager.produce_item("HobbyHorse", "Rocking Horse", 120.0))
# print(factory_manager.produce_item("HobbyHorse", "Rocking Horse", 100.0))
# print()
#
# # # Register new stores
# print(factory_manager.register_new_store("FurnitureStore", "Furniture Outlet", "SOF"))
# print(factory_manager.register_new_store("ToyStore", "Toy World", "VAR"))
# print()
# #
# # Sell products to stores
# chair1 = factory_manager.products[0]
# chair2 = factory_manager.products[1]
# chair3 = factory_manager.products[2]
# store1 = factory_manager.stores[0]
# store2 = factory_manager.stores[1]
# print(factory_manager.sell_products_to_store(store2, chair1, chair2))
# print(factory_manager.sell_products_to_store(store1, chair1, chair2, chair3))
# print()
#
# # Unregister store
# print(factory_manager.unregister_store("Furniture Outlet"))
# print()
#
# # Discount products
# print(factory_manager.discount_products("Classic"))
# print(factory_manager.discount_products("Rocking Horse"))
# print()
#
# # Request store statistics
# print(factory_manager.request_store_stats("Furniture Outlet"))
# print(factory_manager.request_store_stats("Toy World"))
# print()
#
# # Factory statistics
# print(factory_manager.statistics())
# print()
#
# # Unregister store
# print(factory_manager.unregister_store("Toy World"))


"""
A product of sub-type Furniture was produced.
A product of sub-type Furniture was produced.
A product of sub-type Furniture was produced.
A product of sub-type Toys was produced.
A product of sub-type Toys was produced.

A new FurnitureStore was successfully registered.
A new ToyStore was successfully registered.

Products do not match in type. Nothing sold.
Store Furniture Outlet successfully purchased 3 items.

The store is still having products in stock! Unregistering is inadvisable.

Discount applied to 0 products with model: Classic
Discount applied to 2 products with model: Rocking Horse

Store: Furniture Outlet, location: SOF, available capacity: 47
Estimated future profit for 3 products is 38.00
**Furniture for sale:
Classic: 1pcs, average price: 80.00
Modern: 2pcs, average price: 150.00
Store: Toy World, location: VAR, available capacity: 100
Estimated future profit for 0 products is 0.00
**Toys for sale:

Factory: Cool Factory
Income: 380.00
***Products Statistics***
Unsold Products: 2. Total net price: 176.00
Rocking Horse: 2
***Partner Stores: 2***
Furniture Outlet
Toy World

Successfully unregistered store Toy World, location: VAR.

"""
