from unittest import TestCase
from card import Card


class TestCard(TestCase):

    def test_max_length(self):
        test_card = Card()
        expected = test_card.max_length
        result = test_card.category_stat('Maximum length')
        self.assertEqual(expected, result)

    def test_error(self):
        test_card = Card()
        with self.assertRaises(ValueError):
            test_card.category_stat('Fur length')

    def test_min_length(self):
        test_card = Card()
        expected = test_card.min_length
        result = test_card.category_stat('Minimum length')
        self.assertEqual(expected, result)

    def test_min_weight(self):
        test_card = Card()
        expected = test_card.min_weight
        result = test_card.category_stat('Minimum weight')
        self.assertEqual(expected, result)

    def test_max_weight(self):
        test_card = Card()
        expected = test_card.max_weight
        result = test_card.category_stat('Maximum weight')
        self.assertEqual(expected, result)

    def test_lifespan(self):
        test_card = Card()
        expected = test_card.lifespan
        result = test_card.category_stat('Lifespan')
        self.assertEqual(expected, result)