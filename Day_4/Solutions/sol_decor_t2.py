"""
Напишите функцию декоратор, которая переводит значение декорируемой функции
в рублях, в доллары (курс: 1$ = 90 рублей) или в евро (курс: 1€ = 98 рублей).
Как добавить знак валюты:
chr(36) -> '$'
chr(8364) -> '€'
chr(8381) -> '₽'
chr(165) -> '¥'
"""
import random

RATES = {
    "$": 90,
    "€": 98
}


def exchange(func):
    def wrapper(*args, **kwargs):
        result = float(func(*args, **kwargs)[:-1])
        currency = random.choice(list(RATES.keys()))
        return f'{round(result / RATES.get(currency), 2)}{currency}'
    return wrapper


@exchange
def summa(count: float, price: float) -> str:
    """ Out: <float><CHAR>"""
    return f'{round(count * price, 2)}₽'


print(summa(305.5, 2.4))
print(summa(1000, price=10))

