from project.player import Player


class Guild:
    def __init__(self, name: str):
        self.name = name
        self.players = []

    def assign_player(self, player: Player):
        if player.guild != self.name and player.guild != "Unaffiliated":
            return f"Player {player.name} is in another guild."
        if player.guild == self.name:
            return f"Player {player.name} is already in the guild."
        player.guild = self.name
        self.players.append(player)
        return f"Welcome player {player.name} to the guild {self.name}"

    def kick_player(self, player_name: str):
        player_in_guild = [p for p in self.players if p.name == player_name]
        if not player_in_guild:
            return f"Player {player_name} is not in the guild."
        curr_player = player_in_guild[0]
        self.players.remove(curr_player)
        curr_player.guild = "Unaffiliated"
        return f"Player {player_name} has been removed from the guild."

    def guild_info(self):
        players_info = [p.player_info() for p in self.players]
        return f'Guild: {self.name}\n' + '\n'.join(players_info)


        # result = f'Guild: {self.name}\n'
        # for p in self.players:
        #     result += p.player_info()
        # return result


player = Player("George", 50, 100)
print(player.add_skill("Shield Break", 20))
print(player.player_info())
guild = Guild("UGT")
print(guild.assign_player(player))
print(guild.guild_info())
