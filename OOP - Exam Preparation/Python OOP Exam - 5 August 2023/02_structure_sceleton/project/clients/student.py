from project.clients.base_client import BaseClient


class Student(BaseClient):
    TYPE = "Student"
    INTEREST = 2.0
    INTEREST_INCREASE = 1.0

    def __init__(self, name: str, client_id: str, income: float):
        super().__init__(name, client_id, income, interest=self.INTEREST)

    def increase_clients_interest(self):
        self.interest += self.INTEREST_INCREASE
