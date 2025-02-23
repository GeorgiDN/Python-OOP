from project.formula_teams.formula_team import FormulaTeam


class MercedesTeam(FormulaTeam):
    EXPENSES_PER_RACE = 200000

    def __init__(self, budget: int):
        super().__init__(budget)

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0
        sponsors = {"Mercedes ": {1: 1000000, 3: 500000},
                    "TeamViewer": {5: 100000, 7: 50000}}

        for positions in sponsors.values():
            for position, money in positions.items():
                if race_pos <= position:
                    revenue += money
                    break

        revenue -= self.EXPENSES_PER_RACE
        self.budget += revenue

        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"

