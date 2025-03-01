from project.stores.base_store import BaseStore


class FurnitureStore(BaseStore):
    CAPACITY = 50
    STORE_TYPE = "FurnitureStore"

    def __init__(self, name: str, location: str):
        super().__init__(name, location, capacity=self.CAPACITY)

    def store_stats(self):
        result = [f"Store: {self.name}, location: {self.location}, available capacity: {self.capacity}"]
        result.append(self.get_estimated_profit())
        result.append("**Furniture for sale:")
        furniture = {}
        for product in self.products:
            if product.sub_type == "Furniture":
                if product.model not in furniture:
                    furniture[product.model] = []
                furniture[product.model].append(product.price)

        sorted_furniture = dict(sorted(furniture.items(), key=lambda x: x[0]))

        for model, prices in sorted_furniture.items():
            avg_price_per_model = sum(prices) / len(prices) if prices else 0
            result.append(f"{model}: {len(prices)}pcs, average price: {avg_price_per_model:.2f}")

        return "\n".join(result)

