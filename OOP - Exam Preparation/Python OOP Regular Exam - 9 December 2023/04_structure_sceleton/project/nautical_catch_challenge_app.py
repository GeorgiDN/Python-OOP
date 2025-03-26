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

        diver = self.get_object_by_name(self.divers, diver_name)
        if diver:
            return f"{diver_name} is already a participant."

        new_diver = self.VALID_DIVERS[diver_type](diver_name)
        self.divers.append(new_diver)
        return f"{diver_name} is successfully registered for the competition as a {diver_type}."

    def swim_into_competition(self, fish_type: str, fish_name: str, points: float):
        if fish_type not in self.VALID_FISHES:
            return f"{fish_type} is forbidden for chasing in our competition."

        fish = self.get_object_by_name(self.fish_list, fish_name)
        if fish:
            return f"{fish_name} is already permitted."

        new_fish = self.VALID_FISHES[fish_type](fish_name, points)
        self.fish_list.append(new_fish)
        return f"{fish_name} is allowed for chasing as a {fish_type}."

    def chase_fish(self, diver_name: str, fish_name: str, is_lucky: bool):
        diver = self.get_object_by_name(self.divers, diver_name)
        if not diver:
            return f"{diver_name} is not registered for the competition."

        fish = self.get_object_by_name(self.fish_list, fish_name)
        if not fish:
            return f"The {fish_name} is not allowed to be caught in this competition."

        if diver.has_health_issue:
            return f"{diver_name} will not be allowed to dive, due to health issues."

        if diver.oxygen_level < fish.time_to_catch:
            diver.miss(fish.time_to_catch)
            return f"{diver_name} missed a good {fish_name}."

        if diver.oxygen_level == fish.time_to_catch:
            if is_lucky:
                diver.hit(fish)
                return f"{diver_name} hits a {fish.points}pt. {fish_name}."
            else:
                diver.miss(fish.time_to_catch)
                return f"{diver_name} missed a good {fish_name}."

        if diver.oxygen_level > fish.time_to_catch:
            diver.hit(fish)
            return f"{diver_name} hits a {fish.points}pt. {fish_name}."

    def health_recovery(self):
        divers_for_recovery = [d for d in self.divers if d.has_health_issue]
        for diver in divers_for_recovery:
            diver.has_health_issue = False
            diver.renew_oxy()
        return f"Divers recovered: {len(divers_for_recovery)}"

    def diver_catch_report(self, diver_name: str):
        diver = self.get_object_by_name(self.divers, diver_name)
        result = [f"**{diver_name} Catch Report**"]
        for fish in diver.catch:
            result.append(fish.fish_details())

        return "\n".join(result)

    def competition_statistics(self):
        result = ["**Nautical Catch Challenge Statistics**"]
        sorted_divers = sorted(self.divers, key=lambda d: (-d.competition_points, -len(d.catch), d.name))

        for diver in sorted_divers:
            if not diver.has_health_issue:
                result.append(diver.__str__())

        return "\n".join(result)

    @staticmethod
    def get_object_by_name(object_list, name):
        found_object = next((obj for obj in object_list if obj.name == name), None)
        return found_object



# nautical_catch_challenge = NauticalCatchChallengeApp()
#
# # Dive into competition
# print(nautical_catch_challenge.dive_into_competition("ScubaDiver", "MaxineHarper"))
# print(nautical_catch_challenge.dive_into_competition("FreeDiver", "JamalCarter"))
# print(nautical_catch_challenge.dive_into_competition("SkyDiver", "FionaBennett"))
# print(nautical_catch_challenge.dive_into_competition("FreeDiver", "OscarWallace"))
# print(nautical_catch_challenge.dive_into_competition("ScubaDiver", "LilaMoreno"))
# print(nautical_catch_challenge.dive_into_competition("FreeDiver", "LilaMoreno"))
#
# # Swim into competition
# print(nautical_catch_challenge.swim_into_competition("ReefFish", "AzureDamselfish", 8.7))
# print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "BluestripeSnapper", 6.3))
# print(nautical_catch_challenge.swim_into_competition("PredatoryFish", "YellowtailSurgeonfish", 5.0))
# print(nautical_catch_challenge.swim_into_competition("PredatoryFish", "Barracuda", 9.2))
# print(nautical_catch_challenge.swim_into_competition("PredatoryFish", "Coryphaena", 9.7))
# print(nautical_catch_challenge.swim_into_competition("PredatoryFish", "Bluefish", 4.4))
# print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "SwordFish", 10.0))
# print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "Mahi-Mahi", 9.1))
# print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "Tuna", 8.5))
# print(nautical_catch_challenge.swim_into_competition("AquariumFish", "SilverArowana", 3.3))
# print(nautical_catch_challenge.swim_into_competition("DeepSeaFish", "Barracuda", 8.6))
#
# # Conduct fishing competitions
# print(nautical_catch_challenge.chase_fish("FionaBennett", "AzureDamselfish", False))
# print(nautical_catch_challenge.chase_fish("JamalCarter", "SilverArowana", True))
# print(nautical_catch_challenge.chase_fish("MaxineHarper", "YellowtailSurgeonfish", False))
# print(nautical_catch_challenge.chase_fish("MaxineHarper", "Mahi-Mahi", False))
# print(nautical_catch_challenge.chase_fish("MaxineHarper", "Tuna", False))
# print(nautical_catch_challenge.chase_fish("MaxineHarper", "Coryphaena", True))
# print(nautical_catch_challenge.chase_fish("MaxineHarper", "BluestripeSnapper", True))
# print(nautical_catch_challenge.chase_fish("OscarWallace", "Barracuda", False))
# print(nautical_catch_challenge.chase_fish("OscarWallace", "YellowtailSurgeonfish", False))
# print(nautical_catch_challenge.chase_fish("OscarWallace", "Tuna", True))
# print(nautical_catch_challenge.chase_fish("JamalCarter", "Barracuda", True))
# print(nautical_catch_challenge.chase_fish("JamalCarter", "YellowtailSurgeonfish", True))
# print(nautical_catch_challenge.chase_fish("LilaMoreno", "Tuna", False))
# print(nautical_catch_challenge.chase_fish("LilaMoreno", "Mahi-Mahi", False))
# print(nautical_catch_challenge.chase_fish("LilaMoreno", "SwordFish", True))
#
# # Check health recovery
# print(nautical_catch_challenge.health_recovery())
#
# # Conduct fishing competitions
# print(nautical_catch_challenge.chase_fish("LilaMoreno", "Tuna", False))
# print(nautical_catch_challenge.chase_fish("LilaMoreno", "Mahi-Mahi", False))
# print(nautical_catch_challenge.chase_fish("LilaMoreno", "SwordFish", True))
#
# # View catch reports
# print(nautical_catch_challenge.diver_catch_report("LilaMoreno"))
#
# # View competition statistics
# print(nautical_catch_challenge.competition_statistics())



"""
MaxineHarper is successfully registered for the competition as a ScubaDiver.
JamalCarter is successfully registered for the competition as a FreeDiver.
SkyDiver is not allowed in our competition.
OscarWallace is successfully registered for the competition as a FreeDiver.
LilaMoreno is successfully registered for the competition as a ScubaDiver.
LilaMoreno is already a participant.
ReefFish is forbidden for chasing in our competition.
BluestripeSnapper is allowed for chasing as a DeepSeaFish.
YellowtailSurgeonfish is allowed for chasing as a PredatoryFish.
Barracuda is allowed for chasing as a PredatoryFish.
Coryphaena is allowed for chasing as a PredatoryFish.
Bluefish is allowed for chasing as a PredatoryFish.
SwordFish is allowed for chasing as a DeepSeaFish.
Mahi-Mahi is allowed for chasing as a DeepSeaFish.
Tuna is allowed for chasing as a DeepSeaFish.
AquariumFish is forbidden for chasing in our competition.
Barracuda is already permitted.
FionaBennett is not registered for the competition.
The SilverArowana is not allowed to be caught in this competition.
MaxineHarper hits a 5.0pt. YellowtailSurgeonfish.
MaxineHarper hits a 9.1pt. Mahi-Mahi.
MaxineHarper hits a 8.5pt. Tuna.
MaxineHarper hits a 9.7pt. Coryphaena.
MaxineHarper will not be allowed to dive, due to health issues.
OscarWallace hits a 9.2pt. Barracuda.
OscarWallace missed a good YellowtailSurgeonfish.
OscarWallace will not be allowed to dive, due to health issues.
JamalCarter hits a 9.2pt. Barracuda.
JamalCarter missed a good YellowtailSurgeonfish.
LilaMoreno hits a 8.5pt. Tuna.
LilaMoreno hits a 9.1pt. Mahi-Mahi.
LilaMoreno hits a 10.0pt. SwordFish.
Divers recovered: 4
LilaMoreno hits a 8.5pt. Tuna.
LilaMoreno hits a 9.1pt. Mahi-Mahi.
LilaMoreno hits a 10.0pt. SwordFish.
**LilaMoreno Catch Report**
DeepSeaFish: Tuna [Points: 8.5, Time to Catch: 180 seconds]
DeepSeaFish: Mahi-Mahi [Points: 9.1, Time to Catch: 180 seconds]
DeepSeaFish: SwordFish [Points: 10.0, Time to Catch: 180 seconds]
DeepSeaFish: Tuna [Points: 8.5, Time to Catch: 180 seconds]
DeepSeaFish: Mahi-Mahi [Points: 9.1, Time to Catch: 180 seconds]
DeepSeaFish: SwordFish [Points: 10.0, Time to Catch: 180 seconds]
**Nautical Catch Challenge Statistics**
ScubaDiver: [Name: MaxineHarper, Oxygen level left: 540, Fish caught: 4, Points earned: 32.3]
FreeDiver: [Name: JamalCarter, Oxygen level left: 120, Fish caught: 1, Points earned: 9.2]
FreeDiver: [Name: OscarWallace, Oxygen level left: 120, Fish caught: 1, Points earned: 9.2]

"""
