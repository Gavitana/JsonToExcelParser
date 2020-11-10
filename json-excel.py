import json
import argparse
import openpyxl
import pandas as pd
from pathlib import Path
from config import LABELS
from openpyxl import load_workbook
# def parse_args(input_args=None):
#     parser = argparse.ArgumentParser(description="Создает файл excel с необходимыми данными.")
#     parser.add_argument("--input_path", help='Входной путь к файлу', required=True)
#     parser.add_argument("--output_path", help='Результат', required=True)
#     args = parser.parse_known_args(input_args)[0]
#     return args

def json_reader(filename, read=None):
    '''Открывает json-файл и конвертирует его в объект python'''
    with open(filename, 'r') as file:
        read = json.load(file)
    return read


def get_cards(read):
    cards = {'Номер карточки':[],
             'Описание':[],
             'Кто выполняет':[],
             'Метки':[],
             'Время создания':[]}
    for card in read['cards']:
        cards['Номер карточки'].append(card['_id'])
        cards['Описание'].append(card['title'])
        cards['Кто выполняет'].append(card['userId'])
        cards['Метки'].append(" , ".join(card['labelIds']))
        cards['Время создания'].append(card['createdAt'])
    return cards


def get_users_and_labels(read, users={}, labels={}):
    for user in read['users']:
        users[user['_id']] = user['username']
    for label in read['labels']:
        labels[label['_id']] = label['name']
    return (users, labels)


def result_table(cards,users,labels):
    new_user_list = []
    new_labels_list = []
    listt= []
    for user in cards['Кто выполняет']:
        user = users[user]
        new_user_list.append(user)
    for word in cards['Метки']:
        new_labels_list.append(' '.join([labels.get(word,word) for word in word.split()]))
    cards['Кто выполняет'] = new_user_list
    cards['Метки'] = new_labels_list
    return cards


def new_table(g):
    for i in g['Метки']:
        for word in i:
            if word in LABELS.values():
                print(i)




if __name__ == "__main__":
    a = json_reader('wekan.json')
    cards = get_cards(a)
    users, labels = get_users_and_labels(a)
    result = result_table(cards=cards, users=users, labels=labels)
    new_table(result)
    # df = pd.DataFrame(result, index=result["Кто выполняет"], columns=["Номер карточки",
    #                                                      "Описание",
    #                                                      "Метки",
    #                                                      "Время создания"] )
    # df.reset_index(drop=False)
    # df.to_excel('sdf.xlsx')
    #
    # workbook = load_workbook(filename='sdf.xlsx')
    # sheet = workbook.active
    # sheet.freeze_panes = "B2"
    # sheet.auto_filter.ref = "A1:E1"
    # workbook.save("sample.xlsx")

# def main():
#     def main(input_args=None):
#     args = parse_args(input_args)
#     input_path = Path(args.input_path)
#     output_path = Path(args.output_path)
#     assert input_path != output_path
