from project.services.base_service import BaseService


class SecondaryService(BaseService):
    TYPE = 'SecondaryService'
    TYPE_SERVICE = "Secondary"
    CAPACITY = 15

    def __init__(self, name: str):
        super().__init__(name, capacity=self.CAPACITY)

    def take_details(self):
        return self.details()
