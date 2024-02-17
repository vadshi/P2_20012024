RATES = {
    "$": 90,
    "€": 98
         }


def exchange(arg):
    def real_func(func):
        def wrapper(*args, **kwargs):
            rub = float(func(*args, ** kwargs)[:-1])
            currency = RATES.get(arg)
            return f'{round(rub/currency, 2)}{arg}'
        return wrapper
    return real_func


@exchange("€")
def summa(count: float, price: float) -> str:
    return f'{round(count * price, 2)} р'


print(summa(100, 10))


