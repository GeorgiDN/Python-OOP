from project.formula_teams.mercedes_team import MercedesTeam
from project.formula_teams.red_bull_team import RedBullTeam


class F1SeasonApp:

    red_bull_team: RedBullTeam = None
    mercedes_team: MercedesTeam = None
    Valid_team_names = ["Red Bull", "Mercedes"]

    def __init__(self):
        pass

    def register_team_for_season(self, team_name: str, budget: int):
        if team_name not in self.Valid_team_names:
            raise ValueError("Invalid team name!")

        if team_name == "Red Bull":
            self.red_bull_team = RedBullTeam(budget)

        elif team_name == "Mercedes":
            self.mercedes_team = MercedesTeam(budget)

        return f"{team_name} has joined the new F1 season."

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        if not self.mercedes_team or not self.red_bull_team:
            raise Exception("Not all teams have registered for the season.")

        result = f"Red Bull: {self.red_bull_team.calculate_revenue_after_race(red_bull_pos)}. "
        result += f"Mercedes: {self.mercedes_team.calculate_revenue_after_race(mercedes_pos)}. "

        winner = "Red Bull" if red_bull_pos < mercedes_pos else "Mercedes"
        result += f"{winner} is ahead at the {race_name} race."

        return result

