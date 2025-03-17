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

        if len(self.clients) == self.capacity:
            return "Not enough bank capacity."

        new_client = self.VALID_CLIENTS[client_type](client_name, client_id, income)
        self.clients.append(new_client)
        return f"{client_type} was successfully added."

    def grant_loan(self, loan_type: str, client_id: str):
        client = self.get_object_by_id(self.clients, client_id)
        loan = self.get_object_by_type(self.loans, loan_type)
        client_type = client.__class__.__name__

        if (loan_type == "StudentLoan" and client_type == "Student") \
                or (loan_type == "MortgageLoan" and client_type == "Adult"):
            self.loans.remove(loan)
            client.loans.append(loan)
            return f"Successfully granted {loan_type} to {client.name} with ID {client_id}."

        else:
            raise Exception("Inappropriate loan type!")

    def remove_client(self, client_id: str):
        client = self.get_object_by_id(self.clients, client_id)
        if not client:
            raise Exception("No such client!")

        if client.loans:
            raise Exception("The client has loans! Removal is impossible!")

        self.clients.remove(client)
        return f"Successfully removed {client.name} with ID {client_id}."

    def increase_loan_interest(self, loan_type: str):
        loans_to_increase = [loan for loan in self.loans if loan.__class__.__name__ == loan_type]
        for loan in loans_to_increase:
            loan.increase_interest_rate()

        return f"Successfully changed {len(loans_to_increase)} loans."

    def increase_clients_interest(self, min_rate: float):
        clients_to_increase = [client for client in self.clients if client.interest < min_rate]
        for client in clients_to_increase:
            client.increase_clients_interest()

        return f"Number of clients affected: {len(clients_to_increase)}."

    def get_statistics(self):
        result = [f"Active Clients: {len(self.clients)}"]

        total_clients_income = sum([client.income for client in self.clients])
        result.append(f"Total Income: {total_clients_income:.2f}")

        loans_count_granted_to_clients = 0
        granted_sum = 0
        for client in self.clients:
            for loan in client.loans:
                loans_count_granted_to_clients += 1
                granted_sum += loan.amount
        result.append(f"Granted Loans: {loans_count_granted_to_clients}, Total Sum: {granted_sum:.2f}")

        loans_count_not_granted = len(self.loans)
        not_granted_sum = sum([loan.amount for loan in self.loans])
        result.append(f"Available Loans: {loans_count_not_granted}, Total Sum: {not_granted_sum:.2f}")

        avg_client_interest_rate = sum([client.interest for client in self.clients]) / len(self.clients) if self.clients else 0
        result.append(f"Average Client Interest Rate: {avg_client_interest_rate:.2f}")

        return "\n".join(result)

    @staticmethod
    def get_object_by_id(object_list, id_):
        found_object = next((obj for obj in object_list if obj.client_id == id_), None)
        return found_object

    @staticmethod
    def get_object_by_type(object_list, type_):
        found_object = next((obj for obj in object_list if obj.__class__.__name__ == type_), None)
        return found_object


# bank = BankApp(3)
#
# print(bank.add_loan('StudentLoan'))
# print(bank.add_loan('MortgageLoan'))
# print(bank.add_loan('StudentLoan'))
# print(bank.add_loan('MortgageLoan'))
#
# print(bank.add_client('Student', 'Peter Simmons', '1234567891', 500))
# print(bank.add_client('Adult', 'Samantha Peters', '1234567000', 1000))
# print(bank.add_client('Student', 'Simon Mann', '1234567999', 700))
# print(bank.add_client('Student', 'Tammy Smith', '1234567555', 700))
#
# print(bank.grant_loan('StudentLoan', '1234567891'))
# print(bank.grant_loan('MortgageLoan', '1234567000'))
# print(bank.grant_loan('MortgageLoan', '1234567000'))
#
# print(bank.remove_client('1234567999'))
#
# print(bank.increase_loan_interest('StudentLoan'))
# print(bank.increase_loan_interest('MortgageLoan'))
#
# print(bank.increase_clients_interest(1.2))
# print(bank.increase_clients_interest(3.5))
#
# print(bank.get_statistics())

"""
StudentLoan was successfully added.
MortgageLoan was successfully added.
StudentLoan was successfully added.
MortgageLoan was successfully added.
Student was successfully added.
Adult was successfully added.
Student was successfully added.
Not enough bank capacity.
Successfully granted StudentLoan to Peter Simmons with ID 1234567891.
Successfully granted MortgageLoan to Samantha Peters with ID 1234567000.
Successfully granted MortgageLoan to Samantha Peters with ID 1234567000.
Successfully removed Simon Mann with ID 1234567999.
Successfully changed 1 loans.
Successfully changed 0 loans.
Number of clients affected: 0.
Number of clients affected: 1.
Active Clients: 2
Total Income: 1500.00
Granted Loans: 3, Total Sum: 102000.00
Available Loans: 1, Total Sum: 2000.00
Average Client Interest Rate: 3.50

"""
