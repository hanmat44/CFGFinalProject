from unittest import TestCase
from unittest.mock import Mock
from game_round import Round

class test_round(TestCase):

    # Tests function player_won in the occasion the person wins
    def test_player_won_person_wins(self):
        example_test = Round()
        example_test.player_card = Mock()
        example_test.computer_card = Mock()
        example_test.player_card.category_stat.return_value = 10
        example_test.computer_card.category_stat.return_value = 5

        expected = 1 # i.e. player wins
        actual = example_test.player_won('Lifespan')
        self.assertEqual(expected, actual)
