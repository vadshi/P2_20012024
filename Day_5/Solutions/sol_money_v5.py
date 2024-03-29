from functools import total_ordering

import requests


@total_ordering
class Money:

    def __init__(self, rub, kop):
        self.rub: int = rub + kop // 100
        self.kop: int = kop % 100
        self.total: int = self.rub * 100 + self.kop

    def __str__(self):
        if self.kop < 10:
            return f'{self.rub}руб. 0{self.kop}коп.'
        else:
            return f'{self.rub}руб. {self.kop}коп.'

    def __eq__(self, other):
        return self.total == other.total

    def __lt__(self, other):
        return self.total < other.total

    def __add__(self, other):
        x = (self.total + other.total)
        return Money(0, x)

    def __sub__(self, other):
        x = (self.total - other.total) // 100
        y = (self.total - other.total) % 100
        return Money(x, y)

    def __mul__(self, mult: int):
        x = self.total * mult
        return Money(0, x)

    def __mod__(self, percent: float | int):
        result = round(self.total / 100 * percent)
        return Money(0, result)


# __mod__()
# Пояснение: % (процент от суммы) - должна являться новая денежная сумма.
# После вычисления процента, используем округление (функция round())


# Напишите класс для работы с денежными суммами.
#
# Реализовать:
# *   сложение
# *   вычитание
# *   умножение на целое число
# *   сравнение (больше, меньше, равно, не равно)

# ==========================================================================================
from functools import total_ordering

# Описываемый декоратор, позволяет для классов, в которых определён __eq__(), а также один из
# __lt__(), __gt__(), __le__(), __ge__(), сгенерировать остальные методы автоматически.

# @total_ordering
# class Student:
#
#     def __eq__(self, other):
#         return self.last_name == other.last_name
#
#     def __lt__(self, other):
#         return self.last_name < other.last_name

# =========================================================================================

# Примеры:
# Создаем сумму из 20 рублей и 120 копеек
money1 = Money(20, 120)  # в конструктор можно передать два любых натуральных числа

# Выводим сумму, с учетом максимального кол-ва копеек <= 99 коп
print(money1)  # 21руб 20коп

# Создаем две денежные суммы
money1 = Money(20, 60)
money2 = Money(10, 45)

# Складываем суммы
money3 = money1 + money2
print(money3)  # 31руб 05коп

# Примечание: список всех методов для перегрузки операций: (https://pythonworld.ru/osnovy/peregruzka-operatorov.html).


#### Дополнительные задания **

# Добавьте операцию - вычисление процента от суммы. %

# Пример:

# Создаем две денежные суммы
money1 = Money(20, 60)

# Находим 20% от суммы
percent_money = money1 % 20

print(percent_money)  # 4руб 12коп

# __mod__()
# Пояснение: % (процент от суммы) - должна являться новая денежная сумма.
# После вычисления процента, используем округление (функция round())
#
#
# ### Конвертация валют
#
# Доработайте класс Money, добавив ему метод .convert("EUR"), для конвертации суммы в рублях в евро и доллары(*любую валюту).
# Актуальные значения можно взять, сделав запрос на: https://www.cbr-xml-daily.ru/daily_json.js
#
# #### Отправка запроса на url-адрес
#
# pip install requests
# py -m pip install requests
# import requests
#
url = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(url)
#
# , где url - адрес сайта, на который отправляете запрос.
#
# В переменную response получите ответ сайта.
#
# Для преобразования ответа из json-формата используйте функцию:
#
# import json
# data_dict = json.loads(response.text)
#
# Модуля json
#
# print(data_dict['Valute']['EUR']['Value'])
