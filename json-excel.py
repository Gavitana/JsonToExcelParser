import json
import argparse
import openpyxl

from db_classes import Card
from pathlib import Path
from config import LABELS
from openpyxl import load_workbook, Workbook


# def parse_args(input_args=None):
#     parser = argparse.ArgumentParser(description="Создает файл excel с необходимыми данными.")
#     parser.add_argument("--input_path", help='Входной путь к файлу', required=True)
#     parser.add_argument("--output_path", help='Результат', required=True)
#     args = parser.parse_known_args(input_args)[0]
#     return args


cards = []
cards_projects = []
def json_reader(filename, data=None):
    '''Открывает json-файл и конвертирует его в объект python'''
    with open(filename, 'r') as file:
        data = json.load(file)
    return data


def get_cards(data):
    for card in data['cards']:
        card = Card(id=card['_id'],
                    title=card['title'],
                    creator=card['userId'],
                    labels=(" ".join(card['labelIds'])))
        cards.append(card)


def result_table(read, users={}, labels={}):
    for user in read['users']:
        users[user['_id']] = user['username']
    for label in read['labels']:
        labels[label['_id']] = label['name']
    for card in cards:
        lab = card.labels
        card.creator = users[card.creator]
        card.labels = ' '.join([labels.get(lab, lab) for lab in lab.split()])


def create_table():
    for card in cards:
        for c in card.labels.split():
            if c in LABELS.values():
                card.labels = c
                cards_projects.append(card)


if __name__ == "__main__":
    a = json_reader('wekan.json')
    get_cards(a)
    result_table(a)
    create_table()
    workbook = Workbook()
    sheet = workbook.active
    sheet.append(['Метки', 'Описание', 'Создатель'])
    for card in cards_projects:
        data = [card.labels, card.title, card.creator]
        sheet.append(data)
    sheet.freeze_panes = "B2"
    sheet.auto_filter.ref = "A1:D1"
    workbook.save(filename="oop_sample.xlsx")


# def main():
#     def main(input_args=None):
#     args = parse_args(input_args)
#     input_path = Path(args.input_path)
#     output_path = Path(args.output_path)
#     assert input_path != output_path
