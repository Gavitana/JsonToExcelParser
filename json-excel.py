import json
import argparse
from pathlib import Path

from config import LABELS, TIME_LABELS
from classes import Card, Result
from styles import set_style

from openpyxl.utils import FORMULAE
from openpyxl.styles import Alignment
from openpyxl import load_workbook, Workbook
from openpyxl.worksheet.table import Table, TableStyleInfo


def parse_args(input_args=None):
    parser = argparse.ArgumentParser(description="Создает файл excel с необходимыми данными.")
    parser.add_argument("--input_path", help='Входной путь к файлу', required=True)
    parser.add_argument("--output_path", help='Результат', required=True)
    args = parser.parse_known_args(input_args)[0]
    return args


cards = []
results = []
cards_projects = []


def json_reader(filename, data=None):
    '''Открывает json-файл и конвертирует его в объект python'''
    with open(filename, 'r') as file:
        data = json.load(file)
    return data


def get_cards(data):
    '''Создает объект список объектов из json-файла Card'''
    for card in data['cards']:
        card = Card(id=card['_id'],
                    title=card['title'],
                    creator=card['userId'],
                    labels=(" ,".join(card['labelIds'])))
        cards.append(card)


def change_id_to_name(read, users={}, labels={}):
    '''Изменяет все id объектов на имена'''
    for user in read['users']:
        users[user['_id']] = user['username']
    for label in read['labels']:
        labels[label['_id']] = label['name']
    for card in cards:
        lab = card.labels
        card.creator = users[card.creator]
        card.labels = ', '.join([labels.get(lab, lab) for lab in lab.split(' ,')])


def filter_cards():
    '''Фильтрует карточки по названиям проектов'''
    for card in cards:
        for label in card.labels.split(', '):
            if label in TIME_LABELS:
                card.hours += TIME_LABELS[label]
            if label in LABELS:
                card.labels = label
                cards_projects.append(card)
results=[]
def result_table():
    sum_list=[]
    for card in cards_projects:
        result = Result(name=card.labels,
                        hours=card.hours)
        if result.name not in sum_list:
            results.append(result)
            sum_list.append(result.name)
        elif result.name in sum_list:
            for result in results:
                if result.name==card.labels:
                    result.hours += card.hours

def create_xslx():
    '''Создает таблицу эксель'''
    workbook = Workbook()
    sheet = workbook.active
    sheet.append(['Проект', 'Создатель', 'Описание', 'Затраченное время','rr','ss'])
    for card in cards_projects:
        data = [card.labels, card.creator, card.title, card.hours]
        sheet.append(data)
    for result in results:
        data = ['','','','',result.name,result.hours]
        sheet.append(data)
    set_style(sheet)
    sheet.insert_cols(idx=5, amount=2)


    workbook.save(filename="Projects.xlsx")


if __name__ == "__main__":
    data = json_reader('wekan.json')
    get_cards(data)
    change_id_to_name(data)
    filter_cards()
    result_table()
    create_xslx()


# def main():
#     def main(input_args=None):
#     args = parse_args(input_args)
#     input_path = Path(args.input_path)
#     output_path = Path(args.output_path)
#     assert input_path != output_path
