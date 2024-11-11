from project.zones.base_zone import BaseZone

class PirateZone(BaseZone):
    INITIAL_VOLUME = 8 # ships

    def __init__(self, code: str):
        super().__init__(code, self.INITIAL_VOLUME)

    def zone_info(self):
        result = ["@Pirate Zone Statistics@"]
        result.append(f"Code: {self.code}; Volume: {self.volume}")
        battleships_total_count = len(self.ships)
        royalships_count = [ship for ship in self.ships if ship.__class__.__name__ == "RoyalBattleship"]
        royalships_count = len(royalships_count)
        result.append(f"Battleships currently in the Pirate Zone: {battleships_total_count}, "
                      f"{royalships_count} out of them are Royal Battleships.")
        sorted_ships = self.get_ships()
        ship_names = ", ".join(ship.name for ship in sorted_ships) if self.ships else ""
        if ship_names:
            result.append(f"#{ship_names}#")
        return "\n".join(result)
