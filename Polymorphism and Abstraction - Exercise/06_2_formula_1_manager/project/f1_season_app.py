from project.formula_teams.mercedes_team import MercedesTeam
from project.formula_teams.red_bull_team import RedBullTeam


class F1SeasonApp:
    VALID_TEAMS = {"Red Bull": RedBullTeam, "Mercedes": MercedesTeam}

    red_bull_team = None
    mercedes_team = None

    def __init__(self):
        pass

    def register_team_for_season(self, team_name: str, budget: int):
        if team_name not in self.VALID_TEAMS:
            raise ValueError("Invalid team name!")

        if team_name == "Red Bull":
            self.red_bull_team = self.VALID_TEAMS[team_name](budget)
        else:
            self.mercedes_team = self.VALID_TEAMS[team_name](budget)

        return f"{team_name} has joined the new F1 season."

    def new_race_results(self, race_name: str, red_bull_pos: int, mercedes_pos: int):
        if self.red_bull_team is None or self.mercedes_team is None:
            raise Exception("Not all teams have registered for the season.")

        winner = "Red Bull" if red_bull_pos < mercedes_pos else "Mercedes"

        return (f"Red Bull: {self.red_bull_team.calculate_revenue_after_race(red_bull_pos)}. "
                f"Mercedes: {self.mercedes_team.calculate_revenue_after_race(mercedes_pos)}. "
                f"{winner} is ahead at the {race_name} race.")
