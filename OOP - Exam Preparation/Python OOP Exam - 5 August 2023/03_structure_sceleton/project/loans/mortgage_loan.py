from project.loans.base_loan import BaseLoan


class MortgageLoan(BaseLoan):
    INTEREST_RATE = 3.5
    AMOUNT = 50000
    RATE_INCREASE = 0.5

    def __init__(self):
        super().__init__(self.INTEREST_RATE, self.AMOUNT)

    def increase_interest_rate(self):
        self.interest_rate += self.RATE_INCREASE
