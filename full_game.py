from game_round import Round, PlayerChoice, ComputerChoice


# Class to simulate a full TopTrumps game
class FullGame:
    def __init__(self):
        self.player_pick = PlayerChoice()
        self.comp_pick = ComputerChoice()
        self.player_score = 0
        self.computer_score = 0

     # Update to new cards
    def new_instance(self):
        self.player_pick = PlayerChoice()
        self.comp_pick = ComputerChoice()
        return


    # Function to run a full game
    def run_game(self):
        turn_to_pick = 0
        while self.player_score < 5 and self.computer_score < 5:
            if turn_to_pick % 2 == 0:
                self.comp_pick.simulate_round()
                self.update_score_comp()
            else:
                self.player_pick.simulate_round()
                self.update_score_player()
            self.new_instance()
            turn_to_pick += 1
        if self.player_score == 5:
            print("Congratulations you won!")
            return
        else:
            print("The computer won :(")
            return

    # Function to update score- link to database??
    def update_score_comp(self):
        if self.comp_pick.who_won(self.comp_pick.category_pick()) == 'Player':
            self.player_score += 1
        else:
            self.computer_score += 1
        print('Current scores:')
        print('Computer: {}'.format(self.computer_score))
        print('Player: {}'.format(self.player_score))
        return


    def update_score_player(self):
        if self.player_pick.who_won(self.player_pick.category_pick()) == 'Player':
            self.player_score += 1
        else:
            self.computer_score += 1
        print('Current scores:')
        print('Computer: {}'.format(self.computer_score))
        print('Player: {}'.format(self.player_score))
        return



new_game = FullGame()
new_game.run_game()