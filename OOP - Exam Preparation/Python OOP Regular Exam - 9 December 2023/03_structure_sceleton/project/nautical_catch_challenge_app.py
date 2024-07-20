from project.divers.free_diver import FreeDiver
from project.divers.scuba_diver import ScubaDiver
from project.fish.predatory_fish import PredatoryFish
from project.fish.deep_sea_fish import DeepSeaFish


class NauticalCatchChallengeApp:
    VALID_DIVERS = {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}
    VALID_FISHES = {"PredatoryFish": PredatoryFish, "DeepSeaFish": DeepSeaFish}

    def __init__(self):
        self.divers: list = []
        self.fish_list: list = []

    def dive_into_competition(self, diver_type: str, diver_name: str):
        if diver_type not in self.VALID_DIVERS:
            return f"{diver_type} is not allowed in our competition."

        diver = self._get_diver_by_name(self.divers, diver_name)
        if diver in self.divers:
            return f"{diver_name} is already a participant."

        new_diver = self.VALID_DIVERS[diver_type](diver_name)
        self.divers.append(new_diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.VALID_FISHES:
            return f"{fish_type} is forbidden for chasing in our competition."

        fish = self._get_fish_by_name(self.fish_list, fish_name)
        if fish in self.fish_list:
            return f"{fish_name} is already permitted."

        new_fish = self.VALID_FISHES[fish_type](fish_name, points)
        self.fish_list.append(new_fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver = self._get_diver_by_name(self.divers, diver_name)
        if not diver:
            return f"{diver_name} is not registered for the competition."

        fish = self._get_fish_by_name(self.fish_list, fish_name)
        if not fish:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            self._check_oxy_level_and_update_health_status(diver.oxygen_level, diver.has_health_issue)
            return f"{diver_name} missed a good {fish_name}."

        elif diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                self._check_oxy_level_and_update_health_status(diver.oxygen_level, diver.has_health_issue)
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."

            elif not is_lucky:
                diver.miss(fish.time_to_catch)
                self._check_oxy_level_and_update_health_status(diver.oxygen_level, diver.has_health_issue)
                return f"{diver_name} missed a good {fish_name}."

        else:
            diver.hit(fish)
            self._check_oxy_level_and_update_health_status(diver.oxygen_level, diver.has_health_issue)
            return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):
        count_recovered = 0
        for diver in self.divers:
            if diver.has_health_issue:
                diver.has_health_issue = False
                diver.renew_oxy()
                count_recovered += 1

        return f"Divers recovered: {count_recovered}"

    def diver_catch_report(self, diver_name: str):
        diver = self._get_diver_by_name(self.divers, diver_name)
        result = f"**{diver_name} Catch Report**\n"
        for fish in diver.catch:
            result += fish.show_fish_details() + "\n"

        return result.strip()

    def competition_statistics(self):
        sorted_divers = sorted(self.divers, key=lambda d: (-d.competition_points, -len(d.catch), d.name))
        result = "**Nautical Catch Challenge Statistics**\n"
        for diver in sorted_divers:
            if not diver.has_health_issue:
                result += f"{diver}" + "\n"

        return result.strip()

    # #  Helper methods
    @staticmethod
    def _check_oxy_level_and_update_health_status(oxy_level, health_issue):
        if oxy_level == 0:
            health_issue = True
            return health_issue

    @staticmethod
    def _get_diver_by_name(divers_list, d_name):
        found_diver = next((d for d in divers_list if d.name == d_name), None)
        return found_diver

    @staticmethod
    def _get_fish_by_name(f_list, f_name):
        found_fish = next((f for f in f_list if f.name == f_name), None)
        return found_fish







# from project.divers.free_diver import FreeDiver
# from project.divers.scuba_diver import ScubaDiver
# from project.fish.predatory_fish import PredatoryFish
# from project.fish.deep_sea_fish import DeepSeaFish
#
#
# class NauticalCatchChallengeApp:
#     VALID_DIVERS = {"FreeDiver": FreeDiver, "ScubaDiver": ScubaDiver}
#     VALID_FISHES = {"PredatoryFish": PredatoryFish, "DeepSeaFish": DeepSeaFish}
#
#     def __init__(self):
#         self.divers: list = []
#         self.fish_list: list = []
#
#     def dive_into_competition(self, diver_type: str, diver_name: str):
#         if diver_type not in self.VALID_DIVERS:
#             return f"{diver_type} is not allowed in our competition."
#
#         diver = self._get_diver_by_name(self.divers, diver_name)
#         if diver in self.divers:
#             return f"{diver_name} is already a participant."
#
#         new_diver = self.VALID_DIVERS[diver_type](diver_name)
#         self.divers.append(new_diver)
#         return f"{diver_name} is successfully registered for the competition as a {diver_type}."
#
#     def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
#         if fish_type not in self.VALID_FISHES:
#             return f"{fish_type} is forbidden for chasing in our competition."
#
#         fish = self._get_fish_by_name(self.fish_list, fish_name)
#         if fish in self.fish_list:
#             return f"{fish_name} is already permitted."
#
#         new_fish = self.VALID_FISHES[fish_type](fish_name, points)
#         self.fish_list.append(new_fish)
#         return f"{fish_name} is allowed for chasing as a {fish_type}."
#
#     def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
#         diver = self._get_diver_by_name(self.divers, diver_name)
#         if not diver:
#             return f"{diver_name} is not registered for the competition."
#
#         fish = self._get_fish_by_name(self.fish_list, fish_name)
#         if not fish:
#             return f"The {fish_name} is not allowed to be caught in this competition."
#
#         if diver.has_health_issue:
#             return f"{diver_name} will not be allowed to dive, due to health issues."
#
#         if diver.oxygen_level < fish.time_to_catch:
#             diver.miss(fish.time_to_catch)
#             if diver.oxygen_level == 0.0:
#                 diver.has_health_issue = True
#             return f"{diver_name} missed a good {fish_name}."
#
#         elif diver.oxygen_level == fish.time_to_catch:
#             if is_lucky:
#                 diver.hit(fish)
#                 if diver.oxygen_level == 0.0:
#                     diver.has_health_issue = True
#                 return f"{diver_name} hits a {fish.points}pt. {fish_name}."
#
#             elif not is_lucky:
#                 diver.miss(fish.time_to_catch)
#                 if diver.oxygen_level == 0.0:
#                     diver.has_health_issue = True
#                 return f"{diver_name} missed a good {fish_name}."
#
#         elif diver.oxygen_level > fish.time_to_catch:
#             diver.hit(fish)
#             if diver.oxygen_level == 0.0:
#                 diver.has_health_issue = True
#             return f"{diver_name} hits a {fish.points}pt. {fish_name}."
#
#     def health_recovery(self):
#         count_recovered = 0
#         for diver in self.divers:
#             if diver.has_health_issue:
#                 diver.has_health_issue = False
#                 diver.renew_oxy()
#                 count_recovered += 1
#
#         return f"Divers recovered: {count_recovered}"
#
#     def diver_catch_report(self, diver_name: str):
#         diver = self._get_diver_by_name(self.divers, diver_name)
#         result = f"**{diver_name} Catch Report**\n"
#         for fish in diver.catch:
#             result += fish.show_fish_details() + "\n"
#
#         return result.strip()
#
#     def competition_statistics(self):
#         sorted_divers = sorted(self.divers, key=lambda d: (-d.competition_points, -len(d.catch), d.name))
#         result = "**Nautical Catch Challenge Statistics**\n"
#         for diver in sorted_divers:
#             if not diver.has_health_issue:
#                 result += f"{diver}" + "\n"
#
#         return result.strip()
#
#     # #  Helper methods
#     @staticmethod
#     def _get_diver_by_name(divers_list, d_name):
#         found_diver = next((d for d in divers_list if d.name == d_name), None)
#         return found_diver
#
#     @staticmethod
#     def _get_fish_by_name(f_list, f_name):
#         found_fish = next((f for f in f_list if f.name == f_name), None)
#         return found_fish
