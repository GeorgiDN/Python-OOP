from project.clients.student import Student
from project.clients.adult import Adult
from project.loans.student_loan import StudentLoan
from project.loans.mortgage_loan import MortgageLoan


class BankApp:
    VALID_LOANS = {"StudentLoan": StudentLoan, "MortgageLoan": MortgageLoan}
    VALID_CLIENTS = {"Student": Student, "Adult": Adult}

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.loans: list = []
        self.clients: list = []

    def add_loan(self, loan_type: str):
        if loan_type not in self.VALID_LOANS:
            raise Exception("Invalid loan type!")

        new_loan = self.VALID_LOANS[loan_type]()
        self.loans.append(new_loan)
        return f"{loan_type} was successfully added."

    def add_client(self, client_type: str, client_name: str, client_id: str, income: float):
        if client_type not in self.VALID_CLIENTS:
            raise Exception("Invalid client type!")

        if len(self.clients) >= self.capacity:
            return "Not enough bank capacity."

        new_client = self.VALID_CLIENTS[client_type](client_name, client_id, income)
        self.clients.append(new_client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        loan = self._get_loan(self.loans, loan_type)
        client = self._get_client(self.clients, client_id)

        inappropriate_loan_type = self._check_loan_condition(loan, client)
        if not inappropriate_loan_type:
            raise Exception("Inappropriate loan type!")

        self.loans.remove(loan)
        client.loans.append(loan)
        return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

    def remove_client(self, client_id: str):
        client = self._get_client(self.clients, client_id)
        if not client:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        granted_loans = [loan for cl in self.clients for loan in cl.loans]
        number_of_changed_loans = 0
        for loan in self.loans:
            if loan.TYPE == loan_type and loan not in granted_loans:
                loan.increase_interest_rate()
                number_of_changed_loans += 1
        return f"Successfully changed {number_of_changed_loans} loans."

    def increase_clients_interest(self, min_rate: float):
        changed_client_rates_number = 0
        for client in self.clients:
            if client.interest < min_rate:
                client.increase_clients_interest()
                changed_client_rates_number += 1
        return f"Number of clients affected: {changed_client_rates_number}."

    def get_statistics(self):
        total_clients_income = sum([cl.income for cl in self.clients])
        granted_loans = [loan for cl in self.clients for loan in cl.loans]
        not_granted_loans = [loan for loan in self.loans if loan not in granted_loans]
        total_interest_rate = sum([client.interest for client in self.clients])
        avg_client_interest_rate = total_interest_rate / len(self.clients) if self.clients else 0

        result = (f"Active Clients: {len(self.clients)}\n"
                  f"Total Income: {total_clients_income:.2f}\n"
                  f"Granted Loans: {len(granted_loans)}, Total Sum: {sum([loan.amount for loan in granted_loans]):.2f}\n"
                  f"Available Loans: {len(not_granted_loans)}, Total Sum: {sum([loan.amount for loan in not_granted_loans]):.2f}\n"
                  f"Average Client Interest Rate: {avg_client_interest_rate:.2f}")

        return result

    # Helper methods
    @staticmethod
    def _check_loan_condition(loan, client):
        return loan.TYPE == "StudentLoan" and client.TYPE == "Student" \
            or loan.TYPE == "MortgageLoan" and client.TYPE == "Adult"

    @staticmethod
    def _get_loan(lst, loan_type):
        found_loan = next((loan for loan in lst if loan.TYPE == loan_type), None)
        return found_loan

    @staticmethod
    def _get_client(lst, client_id):
        found_client = next((client for client in lst if client.client_id == client_id), None)
        return found_client
