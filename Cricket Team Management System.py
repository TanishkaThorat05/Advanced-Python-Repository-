class Player:
    def __init__(self, player_name, jersey_number, runs):
        self.player_name = player_name
        self.jersey_number = jersey_number
        self.runs = runs

        # Categorize player based on runs
        if runs >= 1000:
            self.category = "Excellent"
        elif runs >= 500:
            self.category = "Good"
        else:
            self.category = "Average"

    def display(self):
        print(f"Player Name   : {self.player_name}")
        print(f"Jersey Number : {self.jersey_number}")
        print(f"Runs          : {self.runs}")
        print(f"Category      : {self.category}")
        print("-" * 30)


class Team:
    def __init__(self):
        self.players = []

    def add_player(self, player):
        self.players.append(player)

    def display_all_players(self):
        print("\n--- Cricket Team Players ---")
        for player in self.players:
            player.display()


# Create Team
team = Team()

# Create players
p1 = Player("Virat Kohli", 18, 2500)
p2 = Player("Rohit Sharma", 45, 1500)
p3 = Player("Shubman Gill", 77, 800)
p4 = Player("Rishabh Pant", 17, 400)

# Add players to team
team.add_player(p1)
team.add_player(p2)
team.add_player(p3)
team.add_player(p4)

# Display all player details
team.display_all_players()
