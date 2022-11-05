from unittest import TestCase
from unittest.mock import Mock
from game_round import Round


class TestRound(TestCase):

    # Tests function player_won
    # in the occasion the person wins
    def test_player_won_person_wins(self):
        example_test = Round()
        example_test.player_card = Mock()
        example_test.computer_card = Mock()
        example_test.player_card.category_stat.return_value = 10
        example_test.computer_card.category_stat.return_value = 5

        expected = 1 # i.e. player wins
        actual = example_test.player_won('Lifespan')
        self.assertEqual(expected, actual)

    # in the occasion computer wins
    def test_player_won_computer_wins(self):
        example_test = Round()
        example_test.player_card = Mock()
        example_test.computer_card = Mock()
        example_test.player_card.category_stat.return_value = 5
        example_test.computer_card.category_stat.return_value = 10

        expected = 0  # i.e. computer wins
        actual = example_test.player_won('Lifespan')
        self.assertEqual(expected, actual)

    # in the occasion there's a draw
    def test_player_won_draw(self):
        example_test = Round()
        example_test.player_card = Mock()
        example_test.computer_card = Mock()
        example_test.player_card.category_stat.return_value = 5
        example_test.computer_card.category_stat.return_value = 5

        expected = -1  # i.e. draw
        actual = example_test.player_won('Lifespan')
        self.assertEqual(expected, actual)

    # testing return type of get_cards()
    def test_get_cards(self):
        example_test = Round()
        result = example_test.get_cards()
        self.assertIsInstance(result, tuple)
