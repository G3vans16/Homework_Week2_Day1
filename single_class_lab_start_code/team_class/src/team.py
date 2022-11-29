class Team: 
    def __init__(self, input_name, input_players, input_coach):
        self.name = input_name
        self.players = input_players
        self.coach = input_coach

    points = 0

    def add_player(self, new_player_name):
        self.players.append(new_player_name)

    def has_player(self, player_name):
        if player_name in self.players:
            return True
        else: return False

    def play_game(self, result):
        if result == True:
            self.points += 3
        if result == False: return
