from project.zones.base_zone import BaseZone


class RoyalZone(BaseZone):
    VOLUME = 10

    def __init__(self, code: str):
        super().__init__(code, self.VOLUME)

    def zone_info(self):
        result = ["@Royal Zone Statistics@"]
        result.append(f"Code: {self.code}; Volume: {self.volume}")
        battleships_total_count = len(self.ships)
        pirateships_count = len([sh for sh in self.ships if sh.__class__.__name__ == "PirateBattleship"])
        result.append(f"Battleships currently in the Royal Zone: {battleships_total_count}, "
                      f"{pirateships_count} out of them are Pirate Battleships.")
        all_ships = self.get_ships()
        ship_names = ', '.join([sh.name for sh in all_ships])
        if all_ships:
            result.append(f"#{ship_names}#")
        return "\n".join(result)
