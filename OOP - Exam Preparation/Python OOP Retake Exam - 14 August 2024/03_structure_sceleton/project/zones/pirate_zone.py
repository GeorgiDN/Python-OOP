from project.zones.base_zone import BaseZone


class PirateZone(BaseZone):
    VOLUME = 8

    def __init__(self, code: str):
        super().__init__(code, self.VOLUME)

    def zone_info(self):
        result = ["@Pirate Zone Statistics@"]
        result.append(f"Code: {self.code}; Volume: {self.volume}")
        battleships_total_count = len(self.ships)
        royal_count = len([sh for sh in self.ships if sh.__class__.__name__ == "RoyalBattleship"])
        result.append(f"Battleships currently in the Pirate Zone: {battleships_total_count}, "
                      f"{royal_count} out of them are Royal Battleships.")
        all_ships = self.get_ships()
        ship_names = ', '.join([sh.name for sh in all_ships])
        if all_ships:
            result.append(f"#{ship_names}#")
        return "\n".join(result)
