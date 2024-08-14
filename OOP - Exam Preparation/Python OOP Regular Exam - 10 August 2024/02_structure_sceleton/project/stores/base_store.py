from abc import ABC, abstractmethod


class BaseStore(ABC):
    STATS_NAME = "BaseStore"

    def __init__(self, name: str, location: str, capacity: int):
        self.name = name
        self.location = location
        self.capacity = capacity
        self.products: list = []

    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, value):
        if not value.strip():
            raise ValueError("Store name cannot be empty!")
        self.__name = value

    @property
    def location(self):
        return self.__location

    @location.setter
    def location(self, value):
        if len(value.strip()) != 3:
            raise ValueError("Store location must be 3 chars long!")
        self.__location = value

    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, value):
        if value < 0:
            raise ValueError("Store capacity must be a positive number or 0!")
        self.__capacity = value

    def get_estimated_profit(self):
        total_sum = sum(p.price for p in self.products)
        profit = total_sum * 0.1
        return f"Estimated future profit for {len(self.products)} products is {profit:.2f}"

    @abstractmethod
    def store_type(self):
        pass

    def store_stats(self):
        result = [f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}"]
        result.append(self.get_estimated_profit())
        result.append(f"**{self.STATS_NAME} for sale:")

        available_furniture = {}
        for product in self.products:
            if product.model not in available_furniture:
                available_furniture[product.model] = []
            available_furniture[product.model].append(product.price)

        sorted_available_furniture = sorted(available_furniture.items())
        for model, pieces in sorted_available_furniture:
            num_of_product_pieces = len(pieces)
            avg_price_per_model = sum(pieces) / num_of_product_pieces
            result.append(f"{model}: {num_of_product_pieces}pcs, average price: {avg_price_per_model:.2f}")

        # for model in sorted(available_furniture):
        #     num_of_product_pieces = len(available_furniture[model])
        #     avg_price_per_model = sum(available_furniture[model]) / num_of_product_pieces
        #     result.append(f"{model}: {num_of_product_pieces}pcs, average price: {avg_price_per_model:.2f}")

        return "\n".join(result)
