import requests
import json
from pprint import pprint
from functools import total_ordering


@total_ordering
class Money:
    def __init__(self, full, pennies) -> None:
        if pennies >= 99:
            full += pennies // 100
            pennies %= 100
        self.full = full
        self.pennies = pennies

    def __str__(self) -> str:
        return f'{self.full}руб {self.pennies:02}коп'

    def __repr__(self) -> str:
        return f'{vars(self)}'

    # сложение

    def __add__(self, other):
        self.full += other.full
        self.pennies += other.pennies
        return Money(self.full, self.pennies)

    # вычитание
    def __sub__(self, other):
        self.full -= other.full
        self.pennies -= other.pennies
        return Money(self.full, self.pennies)

    # остаток от деления
    def __mod__(self, other):
        total_kopecks = self.full * 100 + self.pennies
        percent_kopecks = total_kopecks * other / 100
        percent_rubles = round(percent_kopecks // 100)
        percent_kopecks = round(percent_kopecks % 100)
        return Money(percent_rubles, percent_kopecks)

    # x < y
    def __lt__(self, other):
        total_kopecks = self.full * 100 + self.pennies
        total_other_kopecks = other.full * 100 + other.pennies
        return total_kopecks < total_other_kopecks

    # x == y
    def __eq__(self, other):
        total_kopecks = self.full * 100 + self.pennies
        total_other_kopecks = other.full * 100 + other.pennies
        return total_kopecks == total_other_kopecks

    def convert(self, valuta):
        total_kopecks = self.full * 100 + self.pennies
        dt = data_dict['Valute'][valuta]['Value']
        nominal = data_dict['Valute'][valuta]['Nominal']
        cel = int(dt) * 100
        kop = (int((round(dt - int(dt), 2)) * 100))
        total_kopecks_valuta = (cel + kop) / nominal
        return f'{round(total_kopecks / total_kopecks_valuta, 4)} {valuta}'


# Создаем сумму из 20 рублей и 120 копеек
# в конструктор можно передать два любых натуральных числа
money1 = Money(20, 120)

# Выводим сумму, с учетом максимального кол-ва копеек <= 99 коп
print(money1)  # 21руб 20коп


# Создаем две денежные суммы
money1 = Money(20, 60)
money2 = Money(20, 60)

# Складываем суммы
money3 = money1 + money2
print(money3)  # 31руб 05коп


# Создаем две денежные суммы
money1 = Money(20, 60)

# Находим 20% от суммы
percent_money = money1 % 20

print(percent_money)  # 4руб 12коп


url = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(url)
# Variant 1
# data_dict = json.loads(response.text)
# print(type(data_dict))

# Variant 2
data_dict = response.json()
# print(type(data_dict))
money1 = Money(100, 0)
print(money1.convert('JPY'))
# pprint(data_dict)
# print(data_dict['Valute']['EUR']['Value'])
# print(data_dict['Valute']['USD']['Value'])