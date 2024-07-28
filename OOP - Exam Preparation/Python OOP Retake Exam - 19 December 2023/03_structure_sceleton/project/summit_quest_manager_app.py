from typing import List
from project.peaks.arctic_peak import ArcticPeak
from project.peaks.summit_peak import SummitPeak
from project.climbers.arctic_climber import ArcticClimber
from project.climbers.summit_climber import SummitClimber


class SummitQuestManagerApp:
    VALID_CLIMBERS = {"ArcticClimber": ArcticClimber, "SummitClimber": SummitClimber}
    VALID_PEAKS = {"ArcticPeak": ArcticPeak, "SummitPeak": SummitPeak}

    def __init__(self):
        self.climbers: list = []
        self.peaks: list = []

    def register_climber(self, climber_type: str, climber_name: str):
        if climber_type not in self.VALID_CLIMBERS:
            return f"{climber_type} doesn't exist in our register."

        climber = self._get_object_by_name(self.climbers, climber_name)
        if climber:
            return f"{climber_name} has been already registered."

        new_climber = self.VALID_CLIMBERS[climber_type](climber_name)
        self.climbers.append(new_climber)
        return f"{climber_name} is successfully registered as a {climber_type}."

    def peak_wish_list(self, peak_type: str, peak_name: str, peak_elevation: int):
        if peak_type not in self.VALID_PEAKS:
            return f"{peak_type} is an unknown type of peak."

        new_peak = self.VALID_PEAKS[peak_type](peak_name, peak_elevation)
        self.peaks.append(new_peak)
        return f"{peak_name} is successfully added to the wish list as a {peak_type}."

    def check_gear(self, climber_name: str, peak_name: str, gear: List[str]):
        climber = self._get_object_by_name(self.climbers, climber_name)
        peak = self._get_object_by_name(self.peaks, peak_name)

        missing_equipment = [eq for eq in peak.get_recommended_gear() if eq not in gear]
        if not missing_equipment:
            return f"{climber.name} is prepared to climb {peak_name}."

        climber.is_prepared = False
        sorted_missing_gear = ', '.join(sorted(missing_equipment))
        return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {sorted_missing_gear}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        climber = self._get_object_by_name(self.climbers, climber_name)
        if not climber:
            return f"Climber {climber_name} is not registered yet."

        peak = self._get_object_by_name(self.peaks, peak_name)
        if not peak:
            return f"Peak {peak_name} is not part of the wish list."

        if climber.is_prepared and climber.can_climb():
            climber.climb(peak)
            return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."

        elif not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."

        else:
            climber.rest()
            return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

    def get_statistics(self):
        climbers_with_peaks = [climber for climber in self.climbers if climber.conquered_peaks]
        sorted_climbers_with_peaks = sorted(climbers_with_peaks, key=lambda c: (-len(c.conquered_peaks), c.name))
        result = [f"Total climbed peaks: {len(self.peaks)}"]
        result.append("**Climber's statistics:**")
        for cl in sorted_climbers_with_peaks:
            result.append(cl.__str__())

        return "\n".join(result)

    ###
    @staticmethod
    def _get_object_by_name(object_list, name):
        found_object = next((obj for obj in object_list if obj.name == name), None)
        return found_object


# # Create an instance of SummitQuestManagerApp
# climbing_app = SummitQuestManagerApp()
#
# # Register climbers
# print(climbing_app.register_climber("ArcticClimber", "Alice"))
# print(climbing_app.register_climber("SummitClimber", "Bob"))
# print(climbing_app.register_climber("ExtremeClimber", "Dave"))
# print(climbing_app.register_climber("ArcticClimber", "Charlie"))
# print(climbing_app.register_climber("ArcticClimber", "Alice"))
# print(climbing_app.register_climber("SummitClimber", "Eve"))
# print(climbing_app.register_climber("SummitClimber", "Frank"))
#
# # Add peaks to the wish list
# print(climbing_app.peak_wish_list("ArcticPeak", "MountEverest", 4000))
# print(climbing_app.peak_wish_list("SummitPeak", "K2", 3000))
# print(climbing_app.peak_wish_list("ArcticPeak", "Denali", 2500))
# print(climbing_app.peak_wish_list("UnchartedPeak", "MysteryMountain", 2000))
#
# # Prepare climbers for climbing
# print(climbing_app.check_gear("Alice", "MountEverest", ["Ice axe", "Crampons", "Insulated clothing", "Helmet"]))
# print(climbing_app.check_gear("Bob", "K2", ["Climbing helmet", "Harness", "Climbing shoes", "Ropes"]))
# print(climbing_app.check_gear("Charlie", "Denali", ["Ice axe", "Crampons"]))
#
# # Perform climbing
# print(climbing_app.perform_climbing("Alice", "MountEverest"))
# print(climbing_app.perform_climbing("Bob", "K2"))
# print(climbing_app.perform_climbing("Kelly", "Denali"))
# print(climbing_app.perform_climbing("Alice", "K2"))
# print(climbing_app.perform_climbing("Alice", "MysteryMountain"))
# print(climbing_app.perform_climbing("Eve", "MountEverest"))
# print(climbing_app.perform_climbing("Charlie", "MountEverest"))
# print(climbing_app.perform_climbing("Frank", "K2"))
# print(climbing_app.perform_climbing("Frank", "Denali"))
# print(climbing_app.perform_climbing("Frank", "MountEverest"))
#
# # Get statistics
# print(climbing_app.get_statistics())


"""
Alice is successfully registered as a ArcticClimber.
Bob is successfully registered as a SummitClimber.
ExtremeClimber doesn't exist in our register.
Charlie is successfully registered as a ArcticClimber.
Alice has been already registered.
Eve is successfully registered as a SummitClimber.
Frank is successfully registered as a SummitClimber.
MountEverest is successfully added to the wish list as a ArcticPeak.
K2 is successfully added to the wish list as a SummitPeak.
Denali is successfully added to the wish list as a ArcticPeak.
UnchartedPeak is an unknown type of peak.
Alice is prepared to climb MountEverest.
Bob is prepared to climb K2.
Charlie is not prepared to climb Denali. Missing gear: Helmet, Insulated clothing.
Alice conquered MountEverest whose difficulty level is Extreme.
Bob conquered K2 whose difficulty level is Extreme.
Climber Kelly is not registered yet.
Alice conquered K2 whose difficulty level is Extreme.
Peak MysteryMountain is not part of the wish list.
Eve conquered MountEverest whose difficulty level is Extreme.
Charlie will need to be better prepared next time.
Frank conquered K2 whose difficulty level is Extreme.
Frank conquered Denali whose difficulty level is Advanced.
Frank needs more strength to climb MountEverest and is therefore taking some rest.
Total climbed peaks: 3
**Climber's statistics:**
ArcticClimber: /// Climber name: Alice * Left strength: 120.0 * Conquered peaks: K2, MountEverest ///
SummitClimber: /// Climber name: Frank * Left strength: 51.0 * Conquered peaks: Denali, K2 ///
SummitClimber: /// Climber name: Bob * Left strength: 75.0 * Conquered peaks: K2 ///
SummitClimber: /// Climber name: Eve * Left strength: 75.0 * Conquered peaks: MountEverest ///
"""
