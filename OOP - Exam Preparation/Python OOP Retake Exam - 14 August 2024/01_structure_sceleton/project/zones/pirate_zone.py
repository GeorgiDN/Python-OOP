from project.zones.base_zone import BaseZone


class PirateZone(BaseZone):
    VOLUME = 8

    def __init__(self, code: str):
        super().__init__(code, volume=self.VOLUME)

    def zone_info(self):
        result = ["@Pirate Zone Statistics@"]
        result.append(f"Code: {self.code}; Volume: {self.volume}")
        royal_ships = [sh.name for sh in self.ships if sh.__class__.__name__ == "RoyalBattleship"]
        result.append(f"Battleships currently in the Pirate Zone: {len(self.ships)}, {len(royal_ships)} out of them are Royal Battleships.")
        ships_list_ordered = self.get_ships()
        ship_names = ", ".join(sh.name for sh in ships_list_ordered) if self.ships else ""
        if ship_names:
            result.append(f"#{ship_names}#")
        return "\n".join(result)
