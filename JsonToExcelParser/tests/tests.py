import unittest

from config import LABELS, OTHER_LABELS
from main import json_reader, get_cards, change_id_to_name, filter_cards


class TestMain(unittest.TestCase):
    data = json_reader("tests/wekan.json")

    def test_main(self):
        '''Тест функции get_cards'''
        cards = get_cards(self.data)
        self.assertNotEqual(cards, [])

    def test_main_type_err(self):
        '''Тест функции get_cards, если на входе пустой список'''
        self.assertRaises(TypeError, get_cards, [])

    def test_change_id_to_name(self):
        '''Тест функции change_id_to_name'''
        userlist = []
        cards = get_cards(self.data)
        cards_change_id = change_id_to_name(self.data, cards)

        for user in self.data["users"]:
            userlist.append(user["username"])
            userlist.append("Никто не назначен")
        for card in cards_change_id:
            self.assertIn(card.creator, userlist)

    def test_change_id_to_name_err(self):
        '''Тест функции change_id_to_name, если на входе пустые списки'''
        self.assertRaises(TypeError, change_id_to_name, [], [])

    def test_filter_cards(self):
        '''Тест функции filter_cards'''
        cards = get_cards(self.data)
        cards_change_id = change_id_to_name(self.data, cards)
        cards_projects, other_projects = filter_cards(cards_change_id)

        for card in cards_projects:
            self.assertIn(card.labels, LABELS)
        for card in other_projects:
            self.assertIn(card.labels, OTHER_LABELS)

    def test_filter_cards_err(self):
        '''Тест функции filter_cards, если на входе пустые списки'''
        self.assertRaises(TypeError, filter_cards, [], [])


if __name__ == "__main__":
    unittest.main()
