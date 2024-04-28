from project.peaks.arctic_peak import ArcticPeak
from project.peaks.summit_peak import SummitPeak
from project.climbers.arctic_climber import ArcticClimber
from project.climbers.summit_climber import SummitClimber
from typing import List


class SummitQuestManagerApp:
    VALID_CLIMBERS = {"ArcticClimber": ArcticClimber, "SummitClimber": SummitClimber}
    VALID_PEAKS = {"ArcticPeak": ArcticPeak, "SummitPeak": SummitPeak}

    def __init__(self):
        self.climbers: list = []
        self.peaks: list = []

    def register_climber(self, climber_type: str, climber_name: str):
        if climber_type not in self.VALID_CLIMBERS:
            return f"{climber_type} doesn't exist in our register."

        climber = self._get_climber(self.climbers, climber_name)
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
        climber = self._get_climber(self.climbers, climber_name)
        peak = self._get_peak(self.peaks, peak_name)

        if gear == peak.get_gear():
            return f"{climber_name} is prepared to climb {peak_name}."

        climber.is_prepared = False
        missing_gear = [g for g in peak.get_gear() if g not in gear]
        sorted_missing_gear = sorted(missing_gear)
        return f"{climber_name} is not prepared to climb {peak_name}. Missing gear: {', '.join(sorted_missing_gear)}."

    def perform_climbing(self, climber_name: str, peak_name: str):
        climber = self._get_climber(self.climbers, climber_name)
        peak = self._get_peak(self.peaks, peak_name)

        if not climber:
            return f"Climber {climber_name} is not registered yet."

        if not peak:
            return f"Peak {peak_name} is not part of the wish list."

        if climber.can_climb() and climber.is_prepared:
            climber.climb(peak)
            return f"{climber_name} conquered {peak_name} whose difficulty level is {peak.difficulty_level}."

        if not climber.is_prepared:
            return f"{climber_name} will need to be better prepared next time."

        climber.rest()
        return f"{climber_name} needs more strength to climb {peak_name} and is therefore taking some rest."

    def get_statistics(self):
        result = f"Total climbed peaks: {len(self.peaks)}\n"
        result += "**Climber's statistics:**\n"
        climbers_with_conquered_peaks = [c for c in self.climbers if len(c.conquered_peaks) > 0]

        sorted_climbers_with_conquered_peaks = sorted(climbers_with_conquered_peaks,
                                                      key=lambda c: (-len(c.conquered_peaks), c.name))

        for current_climber in sorted_climbers_with_conquered_peaks:
            result += current_climber.__str__() + "\n"
        return result.strip()

    # Helper methods
    @staticmethod
    def _get_climber(lst, cl_name):
        found_climber = next((c for c in lst if c.name == cl_name), None)
        return found_climber

    @staticmethod
    def _get_peak(lst, p_name):
        found_peak = next((p for p in lst if p.name == p_name), None)
        return found_peak
