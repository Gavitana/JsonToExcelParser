import json
import argparse
import openpyxl

from db_classes import Card
from pathlib import Path
from config import LABELS
from openpyxl.utils import FORMULAE
from openpyxl import load_workbook, Workbook
from openpyxl.styles import Alignment

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
            if c in LABELS:
                card.labels = c
                cards_projects.append(card)


def create_xslx():
    workbook = Workbook()
    sheet = workbook.active
    sheet.append(['Метки', 'Создатель', 'Описание'])
    for card in cards_projects:
        data = [card.labels, card.creator, card.title]
        sheet.append(data)
    col = sheet.column_dimensions['C']
    col.alignment = Alignment(horizontal='fill')
    sheet.column_dimensions['A'].width = 18
    sheet.column_dimensions['B'].width = 18
    sheet.column_dimensions['C'].width = 18
    sheet.freeze_panes = "B2"
    sheet.auto_filter.ref = "A1:D1"
    sheet["G1"] = "=SUBTOTALS(109;D2:D700)"

    workbook.save(filename="Projects.xlsx")


if __name__ == "__main__":
    a = json_reader('wekan.json')
    get_cards(a)
    result_table(a)
    create_table()
    create_xslx()


# def main():
#     def main(input_args=None):
#     args = parse_args(input_args)
#     input_path = Path(args.input_path)
#     output_path = Path(args.output_path)
#     assert input_path != output_path
