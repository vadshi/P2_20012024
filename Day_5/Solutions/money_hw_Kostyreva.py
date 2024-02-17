from functools import total_ordering
import math
import requests
import json

url = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(url)
RATES = json.loads(response.text)


@total_ordering
class Money:
    def __init__(self, rubl: int, kop: int):
        if kop <= 99:
            self.rubl = rubl
            self.kop = kop
        else:
            self.rubl = rubl + kop // 100
            self.kop = kop % 100

    def __str__(self):
        return f"{self.rubl}руб {self.kop:02}коп"

    def __repr__(self):
        return f"Money({self.rubl},{self.kop:02})"

    def __eq__(self, other):
        return self.rubl == other.rubl and self.kop == other.kop

    def __lt__(self, other):
        if self.rubl == other.rubl:
            return self.kop < other.kop
        else:
            return self.rubl < other.rubl

    def __add__(self, other):
        added_rubl = self.rubl + other.rubl
        added_kop = self.kop + other.kop
        if added_kop <= 99:
            added_total = Money(added_rubl, added_kop)
        else:
            added_rubl = added_rubl + added_kop // 100
            added_kop = added_kop % 100
            added_total = Money(added_rubl, added_kop)
        return added_total

    def __sub__(self, other):
        sub_rubl = self.rubl - other.rubl
        sub_kop = self.kop - other.kop
        if sub_rubl <= 0 and sub_kop < 0:
            print(f"Вторая сумма больше, чем первая")
            return None
        if sub_kop < 0:
            sub_rubl = self.rubl - (other.rubl + 1)
            sub_kop = 100 + sub_kop
            sub_total = Money(sub_rubl, sub_kop)
        else:
            sub_total = Money(sub_rubl, sub_kop)
        return sub_total

    def __mul__(self, mn: int):
        mul_rubl = self.rubl * mn
        mul_kop = self.kop * mn
        if mul_kop <= 99:
            mul_total = Money(mul_rubl, mul_kop)
        else:
            mul_rubl = mul_rubl + mul_kop // 100
            mul_kop = mul_kop % 100
            mul_total = Money(mul_rubl, mul_kop)
        return mul_total

    def __mod__(self, perc: int):
        mod_rubl = self.rubl / 100 * perc

        d, c = math.modf(mod_rubl)

        mod_kop = round((self.kop / 100 * perc) + d * 100)

        if mod_kop <= 99:
            mod_total = Money(round(c), mod_kop)
        else:
            mod_rubl = c + mod_kop // 100
            mod_kop = mod_kop % 100
            mod_total = Money(mod_rubl, mod_kop)
        return mod_total

    def convert(self, cur: str):
        conv_rubl = round(self.rubl / RATES['Valute'][cur]['Value'])
        conv_kop = round(self.kop / RATES['Valute'][cur]['Value'])
        print(f"{RATES['Valute'][cur]['Name']}: {conv_rubl + conv_kop} {cur}")
        return conv_rubl + conv_kop


money1 = Money(20, 60)
money2 = Money(20, 325)
money3 = Money(23000, 25000)
money4 = Money(0, 16)
money5 = Money(0, 10)


print(money1 < money2)
print(money2 > money1)
print(money2 == money3)
print(money2 <= money3)
print(money1 + money3)
print(money2 + money3)
print(money3 - money1)
print(money4 - money5)
print(money5 - money4)
print(money5 * 6)
print(f'{money2 = }')
print(money2 * 10)
print(f'{money3 = }')
print(money3 % 20)
print(money5 % 300)
print(money1 * 10)

print('*' * 15)
print(money3)
print(money3 % 1)

print(money5)
print(money5 % 1000)


print(f'{money3 = }')
money3.convert('EUR')
money3.convert('USD')
money3.convert('GBP')
money3.convert('BYN')
money3.convert('BGN')
money3.convert('AED')
money3.convert('CAD')
money3.convert('CNY')

"""
class Money

Напишите класс для работы с денежными суммами.

Реализовать:
*   сложение
*   вычитание
*   умножение на целое число
*   сравнение (больше, меньше, равно, не равно)

==========================================================================================
from functools import total_ordering
Описываемый декоратор, позволяет для классов, в которых определён __eq__(), а также один из
__lt__(), __gt__(), __le__(), __ge__(), сгенерировать остальные методы автоматически.

    @total_ordering
    class Student:

        def __eq__(self, other):
            return self.last_name == other.last_name

        def __lt__(self, other):
            return self.last_name < other.last_name

=========================================================================================

Примеры:
# Создаем сумму из 20 рублей и 120 копеек
money1 = Money(20, 120)  # в конструктор можно передать два любых натуральных числа

# Выводим сумму, с учетом максимального кол-ва копеек <= 99 коп
print(money1) # 21руб 20коп


# Создаем две денежные суммы
money1 = Money(20, 60)
money2 = Money(10, 45)

# Складываем суммы
money3 = money1 + money2
print(money3)  # 31руб 05коп



Примечание: список всех методов для перегрузки операций: (https://pythonworld.ru/osnovy/peregruzka-operatorov.html).


#### Дополнительные задания **

Добавьте операцию - вычисление процента от суммы. %

Пример:

# Создаем две денежные суммы
money1 = Money(20, 60)

# Находим 20% от суммы
percent_money = money1 % 20

print(percent_money)  # 4руб 12коп

__mod__()
Пояснение: % (процент от суммы) - должна являться новая денежная сумма.
После вычисления процента, используем округление (функция round())


### Конвертация валют

Доработайте класс Money, добавив ему метод .convert("EUR"), для конвертации суммы в рублях в евро и доллары(*любую валюту).
Актуальные значения можно взять, сделав запрос на: https://www.cbr-xml-daily.ru/daily_json.js

#### Отправка запроса на url-адрес

pip install requests
py -m pip install requests
import requests

url = 'https://www.cbr-xml-daily.ru/daily_json.js'
response = requests.get(url)

, где url - адрес сайта, на который отправляете запрос.

В переменную response получите ответ сайта.

Для преобразования ответа из json-формата используйте функцию:

import json
data_dict = json.loads(response.text)

Модуля json

print(data_dict['Valute']['EUR']['Value'])
"""
