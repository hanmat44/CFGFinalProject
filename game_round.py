from card import Card
from random import randint


# method for choosing the category when the player picks the category
def player_pick(card):
    print("Your turn to pick the category. Let's see the card:")
    card.view_card()
    decision = input('Which category do you want to pick?')
    print('Category chosen: {}'.format(decision))
    return decision


# method for choosing the category when the computer picks the category
def computer_pick(card):
    print("The computer is picking the category")
    choices_array = ['Minimum length', 'Maximum length', 'Minimum weight', 'Maximum weight', 'Lifespan']
    choice_num = randint(0, 4)
    choice = choices_array[choice_num]
    print('Category chosen: {}'.format(choice))
    return choice



computer_card = Card()
player_card = Card()
computer_pick(computer_card)

