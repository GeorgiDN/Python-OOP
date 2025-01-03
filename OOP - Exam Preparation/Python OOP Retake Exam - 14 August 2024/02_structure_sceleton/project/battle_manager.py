from project.battleships.pirate_battleship import PirateBattleship
from project.battleships.royal_battleship import RoyalBattleship
from project.zones.pirate_zone import PirateZone
from project.zones.royal_zone import RoyalZone


class BattleManager:
    VALID_ZONES = {"RoyalZone": RoyalZone, "PirateZone": PirateZone}
    VALID_SHIPS = {"RoyalBattleship": RoyalBattleship, "PirateBattleship": PirateBattleship}

    def __init__(self):
        self.zones: list = []
        self.ships: list = []

    def add_zone(self, zone_type: str, zone_code: str):
        if zone_type not in self.VALID_ZONES:
            raise Exception("Invalid zone type!")

        found_zone = next((zone.code for zone in self.zones if zone.code == zone_code), None)
        if found_zone:
            raise Exception("Zone already exists!")

        new_zone = self.VALID_ZONES[zone_type](zone_code)
        self.zones.append(new_zone)
        return f"A zone of type {zone_type} was successfully added."

    def add_battleship(self, ship_type: str, name: str, health: int, hit_strength: int):
        if ship_type not in self.VALID_SHIPS:
            raise Exception(f"{ship_type} is an invalid type of ship!")

        new_ship = self.VALID_SHIPS[ship_type](name, health, hit_strength)
        self.ships.append(new_ship)
        return f"A new {ship_type} was successfully added."

    def add_ship_to_zone(self, zone: "BaseZone", ship: "BaseBattleship"):
        if zone.volume == 0:
            return f"Zone {zone.code} does not allow more participants!"

        if ship.health == 0:
            return f"Ship {ship.name} is considered sunk! Participation not allowed!"

        if not ship.is_available:
            return f"Ship {ship.name} is not available and could not participate!"

        if (ship.__class__.__name__ == "PirateBattleship" and zone.__class__.__name__ == "PirateZone") or \
                (ship.__class__.__name__ == "RoyalBattleship" and zone.__class__.__name__ == "RoyalZone"):
            ship.is_attacking = True

        zone.ships.append(ship)
        ship.is_available = False
        zone.volume -= 1

        return f"Ship {ship.name} successfully participated in zone {zone.code}."

    def remove_battleship(self, ship_name: str):
        found_ship = next((ship for ship in self.ships if ship.name == ship_name), None)
        if not found_ship:
            return "No ship with this name!"

        if not found_ship.is_available:
            return "The ship participates in zone battles! Removal is impossible!"

        self.ships.remove(found_ship)
        return f"Successfully removed ship {ship_name}."

    def start_battle(self, zone):
        attackers = [s for s in zone.ships if s.is_attacking]
        targets = [s for s in zone.ships if not s.is_attacking]
        if not attackers or not targets:
            return "Not enough participants. The battle is canceled."

        attacker = max(attackers, key=lambda s: s.hit_strength)
        target = max(targets, key=lambda s: s.health)

        attacker.attack()
        target.take_damage(attacker)

        if target.health == 0:
            zone.ships.remove(target)
            self.ships.remove(target)
            return f"{target.name} lost the battle and was sunk."
        if attacker.ammunition == 0:
            zone.ships.remove(attacker)
            self.ships.remove(attacker)
            return f"{attacker.name} ran out of ammunition and leaves."

        return "Both ships survived the battle."

    def get_statistics(self):
        available_ships_names = [sh.name for sh in self.ships if sh.is_available]
        result = [f"Available Battleships: {len(available_ships_names)}"]
        available_ships = ", ".join(available_ships_names)
        result.append(f"#{available_ships}#") if available_ships else ""
        result.append(f"***Zones Statistics:***")
        result.append(f"Total Zones: {len(self.zones)}")
        sorted_zones = sorted(self.zones, key=lambda z: z.code)
        for z in sorted_zones:
            result.append(z.zone_info())
        return "\n".join(result)

































# battle_manager = BattleManager()
#
# # Add zones
# print(battle_manager.add_zone("RoyalZone", "001"))
# print(battle_manager.add_zone("PirateZone", "002"))
# print()
#
# # Add battleships
# print(battle_manager.add_battleship("RoyalBattleship", "RoyalOne", 50, 50))
# print(battle_manager.add_battleship("RoyalBattleship", "RoyalTwo", 80, 45))
# print(battle_manager.add_battleship("PirateBattleship", "PirateOne", 50, 50))
# print(battle_manager.add_battleship("PirateBattleship", "PirateTwo", 70, 60))
# print(battle_manager.add_battleship("RoyalBattleship", "RoyalThree", 100, 100))
# print(battle_manager.add_battleship("PirateBattleship", "PirateThree", 90, 90))
# print()
#
# # Retrieve battleships and zones
# royal_zone = battle_manager.zones[0]
# pirate_zone = battle_manager.zones[1]
#
# royal_one = battle_manager.ships[0]
# royal_two = battle_manager.ships[1]
# pirate_one = battle_manager.ships[2]
# pirate_two = battle_manager.ships[3]
#
# # Add ships to zones
# print(battle_manager.add_ship_to_zone(royal_zone, royal_one))
# print(battle_manager.add_ship_to_zone(royal_zone, pirate_one))
# print(battle_manager.add_ship_to_zone(pirate_zone, royal_two))
# print(battle_manager.add_ship_to_zone(pirate_zone, pirate_two))
# print()
#
# # Remove a battleship
# print(battle_manager.remove_battleship("RoyalTwo"))
# print(battle_manager.remove_battleship("Nonexistent"))
# print()
#
# # Start battle in RoyalZone
# print(battle_manager.start_battle(royal_zone))
# print()
#
# # Start battle in PirateZone
# print(battle_manager.start_battle(pirate_zone))
# print()
#
# # Start another battle in RoyalZone
# print(battle_manager.start_battle(royal_zone))
# print()
#
# # Retrieve updated statistics
# print(battle_manager.get_statistics())
# print()
#
# # Remove a battleship
# print(battle_manager.remove_battleship("RoyalThree"))

"""
A zone of type RoyalZone was successfully added.
A zone of type PirateZone was successfully added.

A new RoyalBattleship was successfully added.
A new RoyalBattleship was successfully added.
A new PirateBattleship was successfully added.
A new PirateBattleship was successfully added.
A new RoyalBattleship was successfully added.
A new PirateBattleship was successfully added.

Ship RoyalOne successfully participated in zone 001.
Ship PirateOne successfully participated in zone 001.
Ship RoyalTwo successfully participated in zone 002.
Ship PirateTwo successfully participated in zone 002.

The ship participates in zone battles! Removal is impossible!
No ship with this name!

PirateOne lost the battle and was sunk.

Both ships survived the battle.

Not enough participants. The battle is canceled.

Available Battleships: 2
#RoyalThree, PirateThree#
***Zones Statistics:***
Total Zones: 2
@Royal Zone Statistics@
Code: 001; Volume: 8
Battleships currently in the Royal Zone: 1, 0 out of them are Pirate Battleships.
#RoyalOne#
@Pirate Zone Statistics@
Code: 002; Volume: 6
Battleships currently in the Pirate Zone: 2, 1 out of them are Royal Battleships.
#PirateTwo, RoyalTwo#

Successfully removed ship RoyalThree.
"""
