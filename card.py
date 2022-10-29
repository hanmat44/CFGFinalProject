from zoo_api import get


# Class for a top-trumps card
class Card:
    def __init__(self):
        card = get()
        self.name = card['name']
        self.lifespan = card['lifespan']
        self.min_length = card['length_min']
        self.max_length = card['length_max']
        self.min_weight = card['weight_min']
        self.max_weight = card['weight_max']

    # Method to display 1 top trumps card
    def get_card(self):
        card_dict = {}
        card_dict.update({'Name': self.name})
        card_dict.update({'Lifespan': self.lifespan})
        card_dict.update({'Minimum length': self.min_length})
        card_dict.update({'Maximum length': self.max_length})
        card_dict.update({'Minimum weight': self.min_weight})
        card_dict.update({'Maximum weight': self.max_weight})

        return card_dict

    # Returns value of a specified category
    def category_stat(self, category):
        # There must be a better way of writing this
        try:
            if category == 'Lifespan':
                return self.lifespan
            elif category == 'Minimum length':
                return self.min_length
            elif category == 'Maximum length':
                return self.max_length
            elif category == 'Maximum weight':
                return self.max_weight
            elif category == 'Minimum weight':
                return self.min_weight
            else:
                raise ValueError
        except ValueError:
            print('Invalid category')
            return ValueError

