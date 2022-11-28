class Team: 
    def __init__(self, input_name, input_players, input_coach):
        self.name = input_name
        self.players = input_players
        self.coach = input_coach

    def add_player(self, new_player_name):
        self.players.append(new_player_name)

    def has_player(self, player_name):
        if player_name in self.players:
            return True
        else: return False