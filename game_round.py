from card import Card
from random import randint
from card import Card


# Class with all the functions to simulate 1 round of top trumps
class Round:
    def __init__(self):
        self.player_card = Card()
        self.computer_card = Card()
        self.winner = None

    def player_card_stat(self, category):
        return self.player_card.category_stat(category)

    def computer_card_stat(self, category):
        return self.computer_card.category_stat(category)


# Subclass for a round where the player picks the category.
class PlayerChoice(Round):
    def __init__(self):
        super().__init__()

    # method for the player choosing a category. Returns category to be compared as a string
    def category_pick(self):
        print("Your turn to pick the category. Let's see the card:")
        self.player_card.view_card()
        decision = input('Which category do you want to pick?')
        print('Category chosen: {}'.format(decision))
        return decision


# Subclass for when the computer picks the category
class ComputerChoice(Round):
    def __init__(self):
        super().__init__()

        # Method for the computer to choose a category. Returns category to be compared as a string
    def category_pick(self):
        print("The computer is picking the category")
        choices_array = ['Minimum length', 'Maximum length', 'Minimum weight', 'Maximum weight', 'Lifespan']
        choice_num = randint(0, 4)
        choice = choices_array[choice_num]
        print('Category chosen: {}'.format(choice))
        return choice


new_round = PlayerChoice()
cat = new_round.category_pick()
new_round.player_card_stat(cat)







