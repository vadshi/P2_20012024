"""
Напишите функцию декоратор, которая переводит значение декорируемой функции
в рублях, в доллары (курс: 1$ = 69 рубля) или в евро (курс: 1€ = 73 руб).
Для тех, кто хочет добавить знак валюты:
chr(36) -> '$'
chr(8364) -> '€'
chr(8381) -> '₽'
chr(165) -> '¥'

Добавить возможность указать значок валюты для декоратора, по которому мы получаем значение.
"""

def exchange(symbol: str):
    pass


@exchange('$')
def summa(count: float, price: float) -> str:
    """ Out: <float><CHAR>"""
    return f'{round(count * price, 2)}₽'


print(summa(305.5, 2.4))
print(summa(1000, price=10))

