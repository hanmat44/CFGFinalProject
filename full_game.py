from game_round import PlayerChoice, ComputerChoice

# Class to simulate a full TopTrumps game
class FullGame:
    def __init__(self):
        self.player_pick = PlayerChoice()
        self.comp_pick = ComputerChoice()
        self.player_score = 0 # set this to be a database call
        self.computer_score = 0 # set this to be a database call

    # Update to new cards
    def new_instance(self):
        self.player_pick = PlayerChoice()
        self.comp_pick = ComputerChoice()

    # Function to run a full game
    def run_game(self, category):
        result = self.player_pick.simulate_round(category)
        if result:
            self.update_score_player()
        else:
            self.update_score_comp()
        return result


    # Function to update score- link to database??
    # Available for database function integration
    def update_score_comp(self):
        self.computer_score += 1
        print('Current scores:')
        print('Computer: {}'.format(self.computer_score))
        print('Player: {}'.format(self.player_score))

    # returns computer score
    def get_score_comp(self):
        return self.computer_score

    # Available for database function integration
    def update_score_player(self):
        self.player_score += 1 # alter this for database
        print('Current scores:')
        print('Computer: {}'.format(self.computer_score))
        print('Player: {}'.format(self.player_score))

    # Returns player score
    def get_score_player(self):
        return self.player_score


# Quick test
if __name__ == '__main__':
    new_game = FullGame()
    new_game.run_game()