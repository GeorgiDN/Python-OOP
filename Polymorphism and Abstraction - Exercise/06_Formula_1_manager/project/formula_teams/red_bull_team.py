from project.formula_teams.formula_team import FormulaTeam


class RedBullTeam(FormulaTeam):
    EXPENSES = 250000

    def calculate_revenue_after_race(self, race_pos: int):
        revenue = 0
        sponsors = {"Oracle": {1: 1500000, 2: 800000},
                    "Honda": {8: 20000, 10: 10000}}

        for positions in sponsors.values():
            for position, money in positions.items():
                if race_pos <= position:
                    revenue += money
                    break

        revenue -= self.EXPENSES
        self.budget += revenue
        return f"The revenue after the race is {revenue}$. Current budget {self.budget}$"
