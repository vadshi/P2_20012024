from functools import total_ordering
from typing import Self
import requests


def get_exchange_rates():
    """Получение курсов валют"""
    url = 'https://www.cbr-xml-daily.ru/daily_json.js'
    response = requests.get(url).json()
    return response['Valute']


@total_ordering
class Money:
    exchange_rates = {}

    def __init__(self, whole_part: int = 0, frac_part: int = 0, currency: str = "RUR") -> None:
        self.amount: int = whole_part * 100 + frac_part
        self.currency: str = currency

    def __eq__(self, other: Self) -> bool:
        if self.currency == other.currency:
            return self.amount == other.amount
        return self.amount == other.convert(self.currency).amount

    def __lt__(self, other: Self) -> bool:
        if self.currency == other.currency:
            return self.amount < other.amount
        return self.amount < other.convert(self.currency).amount

    def __repr__(self) -> str:
        whole_part, frac_part = self.rub_kop(self.amount)
        return f"{whole_part}.{frac_part:02} {self.currency}"

    def __str__(self) -> str:
        whole_part, frac_part = self.rub_kop(self.amount)
        if self.currency == "RUR":
            return f"{whole_part} руб. {frac_part:02} коп."
        return f"{whole_part}.{frac_part:02} {self.currency}"

    @staticmethod
    def rub_kop(amount: int) -> tuple:
        return divmod(amount, 100)

    def __add__(self, other: Self) -> Self:
        if self.currency == other.currency:
            new_amount = self.amount + other.amount
        else:
            new_amount = self.amount + other.convert(self.currency).amount
        return Money(0, new_amount, currency=self.currency)

    def __sub__(self, other: Self) -> Self:
        if self < other:
            raise ValueError("Нельзя из меньшего вычесть большее")
        if self.currency == other.currency:
            new_amount = self.amount - other.amount
        else:
            new_amount = self.amount - other.convert(self.currency).amount
        return Money(0, new_amount, currency=self.currency)

    def __mul__(self, multiplier: int) -> Self:
        new_amount = self.amount * multiplier
        return Money(0, new_amount, currency=self.currency)

    def __mod__(self, percent: float) -> Self:
        new_amount = int(round(self.amount * percent / 100, 0))
        return Money(0, new_amount, currency=self.currency)

    def convert(self, new_currency: str) -> Self:
        """Конвертация валют"""
        if not Money.exchange_rates:
            Money.exchange_rates = get_exchange_rates()
        rates_dict = Money.exchange_rates
        if new_currency != "RUR" and new_currency not in rates_dict.keys():
            raise KeyError(f"Валюта с кодом {new_currency} не найдена!")
        old_rate = 1
        if self.currency != "RUR":
            if self.currency not in rates_dict.keys():
                raise KeyError(f"Исходная валюта с кодом {self.currency} не найдена!")
            old_rate = rates_dict[self.currency]["Value"] / rates_dict[self.currency]["Nominal"]
        new_rate = 1
        if new_currency != "RUR":
            new_rate = rates_dict[new_currency]["Value"] / rates_dict[new_currency]["Nominal"]
        new_amount = int(round(self.amount * old_rate / new_rate, 0))
        return Money(0, new_amount, currency=new_currency)


if __name__ == "__main__":
    m1 = Money(100, 0)
    m2 = m1.convert("USD")
    m3 = m1.convert("INR")
    m4 = m2.convert("INR")
    m5 = m4.convert("RUR")
    print("*"*40)
    print("Перевод валют")
    print(f"RUR: \n\t{m1 = }")
    print(f"RUR -> USD: \n\t{m2 = }")
    print(f"RUR -> INR: \n\t{m3 = }")
    print(f"RUR -> USD -> INR: \n\t{m4 = }")
    print(f"RUR -> USD -> INR -> RUR: \n\t{m5 = }")
    print("*"*40)
    print("Сложение, вычитание и умножение")

    print(f"{m1} + {m2} = {m1+m2}")
    print(f"{m1} - {m2} = {m1-m2}")
    print(f"{m1} * 20 = {m1*20}")
    print("*"*40)
    print("Сортировка")
    a = [Money(1, 0, "RUR"),
         Money(1, 0, "USD"),
         Money(1, 0, "EUR"),
         Money(1, 0, "CNY"),
         Money(1, 0, "INR"),
         Money(1, 0, "JPY"),
         Money(1, 0, "KGS"),
         Money(1, 0, "RSD")]
    print(a)
    print(sorted(a))
    print("*"*40)

    m2 = Money(20, 90, "RUR")
    money1 = Money(20, 60)
    money2 = Money(10, 45)

    print(m1 + m2)
    print(m1 - m2)
    # Складываем суммы
    money3 = money1 + money2
    print(money3)  # 31руб 05коп

    # Создаем две денежные суммы
    print("Процент")
    money1 = Money(20, 60)

    # Находим 20% от суммы
    percent_money = money1 % 20

    print(f"{money1} % 20 = {money1 % 20}")  # 4руб 12коп
