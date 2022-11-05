from random import randint
from card import Card


# Parent class with all the functions to simulate 1 round of top trumps
class Round:
    def __init__(self):
        self.player_card = Card()
        self.computer_card = Card()

    # Method to return stat on player card - - NEEDED FRONT-END
    def player_card_stat(self, category):
        return self.player_card.category_stat(category)

    # Method to return stat on computer card - - NEEDED FRONT-END
    def computer_card_stat(self, category):
        return self.computer_card.category_stat(category)

    # Method to return who won the round. Returns either 'Player', 'Computer' or 'Draw' - NEEDED FRONT-END
    def player_won(self, category):
        if float(self.player_card_stat(category)) > float(self.computer_card_stat(category)):
            return 1
        elif float(self.player_card_stat(category)) == float(self.computer_card_stat(category)):
            return -1
        else:
            return 0

    # NEEDED FOR FRONT-END
    def simulate_round(self, category):
        return self.player_won(category)

    # Implement name tuple - NEEDED FOR FRONT-END
    def get_cards(self):
        return self.player_card.get_card(), self.computer_card.get_card()


# Subclass for a round where the player picks the category - - NEEDED FRONT-END
class PlayerChoice(Round):
    def __init__(self):
        super().__init__()


# Subclass for when the computer picks the category
class ComputerChoice(Round):
    def __init__(self):
        super().__init__()

        # Method for the computer to choose a category. Returns category to be compared as a string
    # def category_pick(self):
    #     print("The computer is picking the category. Let's see your card first:")
    #     self.player_card.get_card()
    #     choices_array = ['Minimum length', 'Maximum length', 'Minimum weight', 'Maximum weight', 'Lifespan']
    #     choice_num = randint(0, 4)
    #     choice = choices_array[choice_num]
    #     print('Category chosen: {}'.format(choice))
    #     return choice

