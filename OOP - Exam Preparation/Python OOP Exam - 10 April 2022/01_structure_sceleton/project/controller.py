
from project.supply.drink import Drink
from project.supply.food import Food


class Controller:
    VALID_SUPPLIES = {"Food": Food, "Drink": Drink}

    def __init__(self):
        self.players: list = []
        self.supplies: list = []

    def add_player(self, *players):
        added_players = []
        for player in players:
            if player not in self.players:
                self.players.append(player)
                added_players.append(player)
        player_names = ", ".join(p.name for p in added_players)
        return f"Successfully added: {player_names}"

    def add_supply(self, *supplies):
        for supply in supplies:
            self.supplies.append(supply)

    def sustain(self, player_name: str, sustenance_type: str):
        player = self._get_object_by_name(self.players, player_name)

        if player and sustenance_type in self.VALID_SUPPLIES:
            if player.stamina == 100:
                return f"{player_name} have enough stamina."

            supply = self._get_last_added_object_by_type(self.supplies, sustenance_type)
            if not supply:
                raise Exception(f"There are no {sustenance_type.lower()} supplies left!")

            player.stamina = min(player.stamina + supply.energy, 100)
            self.supplies.remove(supply)
            return f"{player_name} sustained successfully with {supply.name}."

    def duel(self, first_player_name: str, second_player_name: str):
        player1 = self._get_object_by_name(self.players, first_player_name)
        player2 = self._get_object_by_name(self.players, second_player_name)

        if player1.stamina == 0 and player2.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina.\n" \
                   f"Player {second_player_name} does not have enough stamina."
        elif player1.stamina == 0:
            return f"Player {first_player_name} does not have enough stamina."
        elif player2.stamina == 0:
            return f"Player {second_player_name} does not have enough stamina."

        weaker_player, stronger_player = self._order_players_by_stamina(player1, player2)

        stronger_player.stamina = max(stronger_player.stamina - weaker_player.stamina / 2, 0)
        if stronger_player.stamina == 0:
            return f"Winner: {weaker_player.name}"

        weaker_player.stamina = max(weaker_player.stamina - stronger_player.stamina / 2, 0)
        if weaker_player.stamina == 0:
            return f"Winner: {stronger_player.name}"

        winner = stronger_player if stronger_player.stamina > weaker_player.stamina else weaker_player
        return f"Winner: {winner.name}"

    def next_day(self):
        for player in self.players:
            player.stamina = max(player.stamina - player.age * 2, 0)
            self.sustain(player.name, "Food")
            self.sustain(player.name, "Drink")

    def __str__(self):
        result = []
        for player in self.players:
            result.append(player.__str__())

        for supply in self.supplies:
            result.append(supply.details())

        return "\n".join(result)

    @staticmethod
    def _get_object_by_name(object_list, name):
        found_object = next((obj for obj in object_list if obj.name == name), None)
        return found_object

    @staticmethod
    def _get_last_added_object_by_type(object_list, object_type):
        found_object = [obj for obj in object_list if obj.__class__.__name__ == object_type]
        return found_object[-1] if found_object else None

    @staticmethod
    def _get_object_by_type(object_list, object_type):
        found_object = next((obj for obj in object_list if obj.__class__.__name__ == object_type), None)
        return found_object

    @staticmethod
    def _order_players_by_stamina(p1, p2):
        duel_list = [p1, p2]
        duel_list.sort(key=lambda x: x.stamina)
        weaker_player = duel_list[0]
        stronger_player = duel_list[1]
        return weaker_player, stronger_player


# controller = Controller()
# apple = Food("apple", 22)
# cheese = Food("cheese")
# juice = Drink("orange juice")
# water = Drink("water")
# first_player = Player('Peter', 15)
# second_player = Player('Lilly', 12, 94)
# print(controller.add_supply(cheese, apple, cheese, apple, juice, water, water))
# print(controller.add_player(first_player, second_player))
# print(controller.duel("Peter", "Lilly"))
# print(controller.add_player(first_player))
# print(controller.sustain("Lilly", "Drink"))
# first_player.stamina = 0
# print(controller.duel("Peter", "Lilly"))
# print(first_player)
# print(second_player)
# controller.next_day()
# print(controller)


"""
None
Successfully added: Peter, Lilly
Winner: Lilly
Successfully added: 
Lilly sustained successfully with water.
Player Peter does not have enough stamina.
Player: Peter, 15, 0, True
Player: Lilly, 12, 82.5, True
Player: Peter, 15, 37, True
Player: Lilly, 12, 98.5, True
Food: cheese, 25
Food: apple, 22
"""
