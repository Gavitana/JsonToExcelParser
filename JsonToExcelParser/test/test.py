from main import json_reader, get_cards, change_id_to_name, filter_cards
from config import LABELS, OTHER_LABELS

data = json_reader("test/wekan.json")


def test():
    '''Тест функции get_cards'''
    cards = get_cards(data)
    assert cards != []

    '''Тест функции change_id_to_name'''
    cards_change_id = change_id_to_name(data, cards)
    userlist = []
    for user in data["users"]:
        userlist.append(user["username"])
    for card in cards_change_id:
        assert card.creator in userlist

    '''Тест функции filter_cards'''
    cards_projects, other_projects = filter_cards(cards_change_id)
    for card in cards_projects:
        assert card.labels in LABELS
    for card in other_projects:
        assert card.labels in OTHER_LABELS
