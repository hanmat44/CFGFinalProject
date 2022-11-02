from unittest import TestCase
from unittest.mock import Mock
from game_round import Round



class test_round(TestCase):
    player_card = Mock()
    player_card.name = 'Cat'
    player_card.lifespan = '22'

    computer_card = Mock()
    computer_card.name = 'Dog'
    computer_card.lifespan = '14'

    test_round = Mock()
    test_round.player_card = player_card
    test_round.computer_card = computer_card

    def test_player_card_stat(self):
        expected = '22'
        result = test_round.player_card_stat('Lifespan')
        self.assertEqual(expected, result)
