import json
import requests


class APIExeption(Exception):
    pass


class FuuuExeption(APIExeption):
    def __str__(self):
        return "Ты пишешь боту гадости? Тебе, что 5 лет?"


class NotEnoughExeption(APIExeption):
    def __str__(self):
        return "Не хватает исходных данных. Воспользуйся /help"


class MoreThenEnoughExeption(APIExeption):
    def __str__(self):
        return "Слишком много исходных данных. Воспользуйся /help"


class SyntaxExeption(APIExeption):
    def __str__(self):
        return "Исходные данные не верны. Воспользуйся /help"


thrals_dict = {"Доллар": "USD",
               "Евро": "EUR",
               "Злотый": "PLN",
               "Фунт": "GBP"}


class RequesterCore:
    @staticmethod
    def exchange_it_my_thral(parent, child, vol):
        work = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        worked_work = json.loads(work.content)
        all_valutes = worked_work.get("Valute")
        parent = thrals_dict.get(parent)
        child = thrals_dict.get(child)
        for row in all_valutes.keys():
            if parent == row:
                d = all_valutes.get(row)
                parent = round(d.get('Value'), 2)
            if child == row:
                d = all_valutes.get(row)
                child = round(d.get('Value'), 2)
        return round(((parent * vol) / child), 2)

    @staticmethod
    def convert_it_my_thral(parent, vol):
        work = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        worked_work = json.loads(work.content)
        all_valutes = worked_work.get("Valute")
        parent = thrals_dict.get(parent)
        for row in all_valutes.keys():
            if parent == row:
                d = all_valutes.get(row)
                parent = round(d.get('Value'), 2)
        return round((parent * vol), 2)

    @staticmethod
    def get_me_price_my_thral():
        work = requests.get('https://www.cbr-xml-daily.ru/daily_json.js')
        worked_work = json.loads(work.content)
        all_valutes = worked_work.get("Valute")
        interest_valute = {}
        for row in all_valutes.keys():
            for row2 in thrals_dict.values():
                if row == row2:
                    d = all_valutes.get(row)
                    f = d.get('Value')
                    interest_valute.update({row: round(f, 2)})
        return interest_valute


fuuu_list = ["хуй", "жоп", "пизд", "говн", "ебат", "Хуй", "Жоп", "Пизд", "Говн", "Ебат"]