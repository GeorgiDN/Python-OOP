from project.stores.base_store import BaseStore


class ToyStore(BaseStore):
    CAPACITY = 100
    STATS_NAME = "Toys"

    def __init__(self, name: str, location: str):
        super().__init__(name, location, capacity=self.CAPACITY)

    @property
    def store_type(self):
        return "ToyStore"


# t = ToyStore("test1", "usa")
# print(t.store_type)
# print(t.store_stats())
