from project.artifacts.contemporary_artifact import ContemporaryArtifact
from project.artifacts.renaissance_artifact import RenaissanceArtifact
from project.collectors.museum import Museum
from project.collectors.private_collector import PrivateCollector


class AuctionHouseManagerApp:
    VALID_ARTIFACTS = {"RenaissanceArtifact": RenaissanceArtifact, "ContemporaryArtifact": ContemporaryArtifact}
    VALID_COLLECTORS = {"Museum": Museum, "PrivateCollector": PrivateCollector}

    def __init__(self):
        self.artifacts: list = []
        self.collectors: list = []

    def register_artifact(self, artifact_type: str, artifact_name: str, artifact_price: float, artifact_space: int):
        if artifact_type not in self.VALID_ARTIFACTS:
            raise ValueError(f"Unknown artifact type!")

        artifact = self._take_object_by_name(self.artifacts, artifact_name)
        if artifact:
            raise ValueError(f"{artifact_name} has been already registered!")

        new_artifact = self.VALID_ARTIFACTS[artifact_type](artifact_name, artifact_price, artifact_space)
        self.artifacts.append(new_artifact)
        return f"{artifact_name} is successfully added to the auction as {artifact_type}."

    def register_collector(self, collector_type: str, collector_name: str):
        if collector_type not in self.VALID_COLLECTORS:
            raise ValueError(f"Unknown collector type!")

        collector = self._take_object_by_name(self.collectors, collector_name)
        if collector:
            raise ValueError(f"{collector_name} has been already registered!")

        new_collector = self.VALID_COLLECTORS[collector_type](collector_name)
        self.collectors.append(new_collector)
        return f"{collector_name} is successfully registered as a {collector_type}."

    def perform_purchase(self, collector_name: str, artifact_name: str):
        collector = self._take_object_by_name(self.collectors, collector_name)
        if not collector:
            raise ValueError(f"Collector {collector_name} is not registered to the auction!")

        artifact = self._take_object_by_name(self.artifacts, artifact_name)
        if not artifact:
            raise ValueError(f"Artifact {artifact_name} is not registered to the auction!")

        if not collector.can_purchase(artifact.price, artifact.space_required):
            return "Purchase is impossible."

        self.artifacts.remove(artifact)
        collector.purchased_artifacts.append(artifact)
        collector.available_money -= artifact.price
        collector.available_space -= artifact.space_required

        return f"{collector_name} purchased {artifact_name} for a price of {artifact.price:.2f}."

    def remove_artifact(self, artifact_name: str):
        artifact = self._take_object_by_name(self.artifacts, artifact_name)
        if not artifact:
            return "No such artifact."

        self.artifacts.remove(artifact)
        return f"Removed {artifact.artifact_information()}"

    def fundraising_campaigns(self, max_money: float):
        count_collectors = 0
        for collector in self.collectors:
            if collector.available_money <= max_money:
                collector.increase_money()
                count_collectors += 1

        return f"{count_collectors} collector/s increased their available money."

    def get_auction_report(self):
        sorted_collectors = sorted(self.collectors, key=lambda c: (-len(c.purchased_artifacts), c.name))
        # count_of_sold_artifacts = 0
        # for collector in sorted_collectors:
        #     if collector.purchased_artifacts:
        #         count_of_sold_artifacts += len(collector.purchased_artifacts)

        count_of_sold_artifacts = sum(len(c.purchased_artifacts) for c in self.collectors)

        result = ["**Auction statistics**"]
        result.append(f"Total number of sold artifacts: {count_of_sold_artifacts}")
        result.append(f"Available artifacts for sale: {len(self.artifacts)}")
        result.append("***")
        for collector in sorted_collectors:
            result.append(collector.__str__())

        return "\n".join(result)

    @staticmethod
    def _take_object_by_name(object_list, name):
        found_object = next((obj for obj in object_list if obj.name == name), None)
        return found_object


manager = AuctionHouseManagerApp()
# Register artifacts
print(manager.register_artifact("RenaissanceArtifact", "Kohinoor", 5000.0, 10))
print(manager.register_artifact("RenaissanceArtifact", "Zelda", 5000.0, 10))
print(manager.register_artifact("RenaissanceArtifact", "Mona Lisa", 10000.0, 100))
print(manager.register_artifact("ContemporaryArtifact", "The Scream", 2000.0, 1000))
print(manager.register_artifact("ContemporaryArtifact", "Untitled", 32000.0, 90))
print()
# Register collectors
print(manager.register_collector("PrivateCollector", "Josh Smith"))
print(manager.register_collector("Museum", "Louvre"))
print(manager.register_collector("Museum", "Hermitage"))
print()
# Perform purchases
print(manager.perform_purchase("Josh Smith", "Mona Lisa"))
print(manager.perform_purchase("Louvre", "Kohinoor"))
print(manager.perform_purchase("Josh Smith", "Zelda"))
print(manager.perform_purchase("Josh Smith", "The Scream"))
print(manager.perform_purchase("Josh Smith", "Untitled"))
print()
# Remove artifact
print(manager.remove_artifact("The Scream"))
print(manager.remove_artifact("Nonexistent"))
print()
# Start fund-raising campaigns
print(manager.fundraising_campaigns(10000.0))
print()
# Get auction report
print(manager.get_auction_report())
print()

# Remove artifact
print(manager.remove_artifact("Untitled"))


"""
Kohinoor is successfully added to the auction as RenaissanceArtifact.
Zelda is successfully added to the auction as RenaissanceArtifact.
Mona Lisa is successfully added to the auction as RenaissanceArtifact.
The Scream is successfully added to the auction as ContemporaryArtifact.
Untitled is successfully added to the auction as ContemporaryArtifact.

Josh Smith is successfully registered as a PrivateCollector.
Louvre is successfully registered as a Museum.
Hermitage is successfully registered as a Museum.

Josh Smith purchased Mona Lisa for a price of 10000.00.
Louvre purchased Kohinoor for a price of 5000.00.
Josh Smith purchased Zelda for a price of 5000.00.
Josh Smith purchased The Scream for a price of 2000.00.
Purchase is impossible.

No such artifact.
No such artifact.

2 collector/s increased their available money.

**Auction statistics**
Total number of sold artifacts: 4
Available artifacts for sale: 1
***
Collector name: Josh Smith; Money available: 13000.00; Space available: 1890; Artifacts: Zelda, The Scream, Mona Lisa
Collector name: Louvre; Money available: 11000.00; Space available: 1990; Artifacts: Kohinoor
Collector name: Hermitage; Money available: 15000.00; Space available: 2000; Artifacts: none

Removed Contemporary Artifact: Untitled; Price: 32000.00; Required space: 90

"""
