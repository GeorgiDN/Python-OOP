from project.stores.base_store import BaseStore


class FurnitureStore(BaseStore):
    CAPACITY = 50
    STATS_NAME = "Furniture"

    def __init__(self, name: str, location: str):
        super().__init__(name, location, capacity=self.CAPACITY)

    @property
    def store_type(self):
        return "FurnitureStore"
