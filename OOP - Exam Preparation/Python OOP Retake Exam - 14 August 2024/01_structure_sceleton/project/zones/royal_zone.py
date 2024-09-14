# from project.battleships.pirate_battleship import PirateBattleship
# from project.battleships.royal_battleship import RoyalBattleship
from project.zones.base_zone import BaseZone


class RoyalZone(BaseZone):
    VOLUME = 10

    def __init__(self, code: str):
        super().__init__(code, volume=self.VOLUME)

    def zone_info(self):
        result = ["@Royal Zone Statistics@"]
        result.append(f"Code: {self.code}; Volume: {self.volume}")
        pirate_ships = [sh.name for sh in self.ships if sh.__class__.__name__ == "PirateBattleship"]
        pirateships_count = len(pirate_ships)
        result.append(f"Battleships currently in the Royal Zone: {len(self.ships)}, {pirateships_count} out of them are Pirate Battleships.")
        ships_list_ordered = self.get_ships()
        ship_names = ", ".join(sh.name for sh in ships_list_ordered) if self.ships else ""
        if ship_names:
            result.append(f"#{ship_names}#")
        return "\n".join(result)



# p = PirateBattleship('PirateTwo', 100, 40)
# p2 = RoyalBattleship('RoyalTwo', 20, 20)
#
# zone = RoyalZone("123")
# zone.ships.append(p)
# zone.ships.append(p2)
# print(zone.zone_info())
