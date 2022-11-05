from game_round import PlayerChoice, ComputerChoice


# Class to simulate a full TopTrumps game - NEEDED FOR FRONT-END
class FullGame:
    def __init__(self):
        self.player_pick = PlayerChoice()
        self.comp_pick = ComputerChoice()
        self.player_score = 0
        self.computer_score = 0

    # Update to new cards - NEEDED FOR FRONT-END
    def new_instance(self):
        self.player_pick = PlayerChoice()
        self.comp_pick = ComputerChoice()

    # Function to run a full game - NEEDED FOR FRONT-END
    def run_game(self, category):
        result = self.player_pick.simulate_round(category)
        return result

    # Gets cards - NEEDED FOR FRONT-END
    def get_cards(self):
        return self.player_pick.get_cards()

    #  Returns computer score - NEEDED FOR FRONT-END
    def get_score_comp(self):
        return self.computer_score

    # Returns player score - NEEDED FOR FRONT END
    def get_score_player(self):
        return self.player_score

    # Code for future improvements where multiple rounds can be played and scores kept track of in class:

    # def update_score_comp(self): - NOT NEEDED FOR FRONT-END
    #     self.computer_score += 1

    # Available for database function integration - NOT NEEDED FOR FRONT END
    # def update_score_player(self):
    #     self.player_score += 1

