from random import randint
from card import Card


# Parent class with all the functions to simulate 1 round of top trumps
class Round:
    def __init__(self):
        self.player_card = Card()
        self.computer_card = Card()
        self.winner = None

    # Method to return stat on player card
    def player_card_stat(self, category):
        return self.player_card.category_stat(category)

    # Method to return stat on computer card
    def computer_card_stat(self, category):
        return self.computer_card.category_stat(category)

    # Method to return who won the round. Returns either 'Player' or 'Computer'
    def who_won(self, category):
        if float(self.player_card_stat(category)) > float(self.computer_card_stat(category)):
            print("You won!")
            return 'Player'
        else:
            print("The computer won!")
            return 'Computer'

    def category_pick(self):
        pass
        # We will define this separately in the subclasses

    def simulate_round(self):
        cat = self.category_pick()
        print("Computer has:")
        print(self.computer_card_stat(cat))
        print("You have:")
        print(self.player_card_stat(cat))
        self.winner = self.who_won(cat)
        return


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
        print("The computer is picking the category. Let's see your card first:")
        self.player_card.view_card()
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







