from project.zones.base_zone import BaseZone

class RoyalZone(BaseZone):
    INITIAL_VOLUME = 10 # ships

    def __init__(self, code: str):
        super().__init__(code, self.INITIAL_VOLUME)

    def zone_info(self):
        result = ["@Royal Zone Statistics@"]
        result.append(f"Code: {self.code}; Volume: {self.volume}")
        battleships_total_count = len(self.ships)
        pirateships = [ship for ship in self.ships if ship.__class__.__name__ == 'PirateBattleship']
        pirateships_count = len(pirateships)
        result.append(f"Battleships currently in the Royal Zone: {battleships_total_count}, "
                      f"{pirateships_count} out of them are Pirate Battleships.")
        sorted_ships = self.get_ships()
        ship_names = ", ".join(ship.name for ship in sorted_ships) if self.ships else ""
        if ship_names:
            result.append(f"#{ship_names}#")
        return "\n".join(result)

