from project.loans.base_loan import BaseLoan


class StudentLoan(BaseLoan):
    TYPE = "StudentLoan"
    INTEREST_RATE = 1.5
    AMOUNT = 2000.0
    RATE_INCREASE = 0.2

    def __init__(self):
        super().__init__(interest_rate=self.INTEREST_RATE, amount=self.AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += self.RATE_INCREASE
