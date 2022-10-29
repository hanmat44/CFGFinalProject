from random import randint
from card import Card


# Parent class with all the functions to simulate 1 round of top trumps
class Round:
    def __init__(self):
        self.player_card = Card()
        self.computer_card = Card()

    # Method to return stat on player card
    def player_card_stat(self, category):
        return self.player_card.category_stat(category)

    # Method to return stat on computer card
    def computer_card_stat(self, category):
        return self.computer_card.category_stat(category)

    # Method to return who won the round. Returns either 'Player' or 'Computer'
    def player_won(self, category):
        if float(self.player_card_stat(category)) > float(self.computer_card_stat(category)):
            return True
        else:
            return False

    def category_pick(self):
        pass
        # We will define this seperately in the subclasses

    def simulate_round(self, category):
        return self.player_won(category)


# Subclass for a round where the player picks the category.
class PlayerChoice(Round):
    def __init__(self):
        super().__init__()

    # method for the player choosing a category. Returns category to be compared as a string

# Subclass for when the computer picks the category
class ComputerChoice(Round):
    def __init__(self):
        super().__init__()

        # Method for the computer to choose a category. Returns category to be compared as a string
    def category_pick(self):
        print("The computer is picking the category. Let's see your card first:")
        self.player_card.get_card()
        choices_array = ['Minimum length', 'Maximum length', 'Minimum weight', 'Maximum weight', 'Lifespan']
        choice_num = randint(0, 4)
        choice = choices_array[choice_num]
        print('Category chosen: {}'.format(choice))
        return choice


if __name__ == '__main__':
    # new_round = PlayerChoice()
    # new_round.simulate_round()
    new_round = ComputerChoice()
    new_round.simulate_round()







