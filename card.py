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
    def view_card(self):
        print('Name:', self.name)
        print('Lifespan:', self.lifespan)
        print('Minimum length:', self.min_length)
        print('Maximum length:', self.max_length)
        print('Minimum weight:', self.min_weight)
        print('Maximum weight:', self.max_weight)

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

