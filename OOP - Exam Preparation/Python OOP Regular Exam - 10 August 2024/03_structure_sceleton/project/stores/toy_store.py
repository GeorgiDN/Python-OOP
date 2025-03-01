from project.stores.base_store import BaseStore


class ToyStore(BaseStore):
    CAPACITY = 100
    STORE_TYPE = "ToyStore"

    def __init__(self, name: str, location: str):
        super().__init__(name, location, capacity=self.CAPACITY)

    def store_stats(self):
        result = [f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}"]
        result.append(self.get_estimated_profit())
        result.append("**Toys for sale:")
        toys = {}
        for product in self.products:
            if product.sub_type == "Toys":
                if product.model not in toys:
                    toys[product.model] = []
                toys[product.model].append(product.price)

        sorted_furniture = dict(sorted(toys.items(), key=lambda x: x[0]))

        for model, prices in sorted_furniture.items():
            avg_price_per_model = sum(prices) / len(prices) if prices else 0
            result.append(f"{model}: {len(prices)}pcs, average price: {avg_price_per_model:.2f}")

        return "\n".join(result)
