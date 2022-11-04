from unittest import TestCase
from card import Card


class TestCard(TestCase):

    # Tests for the category_stat method:
    # Testing that each category returns the correct stat
    def test_max_length(self):
        test_card = Card()
        expected = test_card.max_length
        result = test_card.category_stat('Maximum length')
        self.assertEqual(expected, result)

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

    # Testing an error is thrown correctly
    def test_error(self):
        test_card = Card()
        with self.assertRaises(ValueError):
            test_card.category_stat('Fur length')

    # Testing the get_card method
    # Testing that each entry in the dictionary has the correct info
    def test_correct_dict_name(self):
        test_card = Card()
        expected = test_card.name
        actual = test_card.get_card()['Name']
        self.assertEqual(expected, actual)

    def test_correct_dict_image(self):
        test_card = Card()
        expected = test_card.image_link
        actual = test_card.get_card()['Image']
        self.assertEqual(expected, actual)

    def test_correct_dict_lifespan(self):
        test_card = Card()
        expected = test_card.lifespan
        actual = test_card.get_card()['Lifespan']
        self.assertEqual(expected, actual)

    def test_correct_dict_min_length(self):
        test_card = Card()
        expected = test_card.min_length
        actual = test_card.get_card()['Minimum length']
        self.assertEqual(expected, actual)

    def test_correct_dict_max_length(self):
        test_card = Card()
        expected = test_card.max_length
        actual = test_card.get_card()['Maximum length']
        self.assertEqual(expected, actual)

    def test_correct_dict_min_weight(self):
        test_card = Card()
        expected = test_card.min_weight
        actual = test_card.get_card()['Minimum weight']
        self.assertEqual(expected, actual)

    def test_correct_dict_max_weight(self):
        test_card = Card()
        expected = test_card.max_weight
        actual = test_card.get_card()['Maximum weight']
        self.assertEqual(expected, actual)



