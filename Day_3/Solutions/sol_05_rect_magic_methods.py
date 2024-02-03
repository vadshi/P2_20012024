"""
Используем класс Rect() с длиной и шириной в качестве атрибутов
Дополнительные задания на magic methods:
1) __repr__() - отобразить в виде текста

2) __str__() - отобразить в виде текста

3) r1 * 5 (__mul__()) - обе стороны станут в 5 раз больше
   добавить проверкy, что тип аргумента метода __mul__ это int или float
   # Variant 1, но python -O отключает все assert'ы
   assert type(arg) in (int, float), 'Bad type'

   # Variant 2
   if type(arg) in (int, float):
       pass
   else:
       raise TypeError

4) r1 < r2, r1 == r2, r1 <= r1 и т.п.

Шесть методов для сравнения:
__lt__() -> '<'
__gt__() -> '>'
__le__() -> '<='
__ge__() -> '>='
__eq__() -> '=='
__ne__() -> '!='
Сравнить по площади.

def __gt__(self, other):
	# ...
	# return True/False
"""
from typing import Self


class Rect:
    def __init__(self, length: int | float, width: int | float) -> None:
        self.length: int | float = length
        self.width: int | float = width

    def __repr__(self) -> str:
        return f"Rectangle({self.length}, {self.width})"

    def __str__(self) -> str:
        return repr(self)

    def area(self) -> int | float:
        return self.length * self.width

    def __mul__(self, number: int | float) -> None:
        if type(number) in (int, float):
            self.length *= number
            self.width *= number
        else:
            raise TypeError(f'Тип множителя должен быть int либо float. Передан тип {type(number)}.')

    def __lt__(self, other: Self) -> bool:
        return self.area() < other.area()

    def __gt__(self, other: Self) -> bool:
        return self.area() > other.area()

    def __le__(self, other: Self) -> bool:
        return self.area() <= other.area()

    def __ge__(self, other: Self) -> bool:
        return self.area() >= other.area()

    def __eq__(self, other: Self) -> bool:
        return self.area() == other.area()


if __name__ == "__main__":
    r1 = Rect(1, 2)
    print(r1)
    r1 * 5
    print("Умножили на 5")
    print(f"r1: {r1}")

    r2 = Rect(10, 5)
    r3 = Rect(10, 10)
    print(f"r2: {r2}")
    print(f"r3: {r3}")

    print(f"r1 < r2: {r1 < r2}")
    print(f"r1 == r2: {r1 == r2}")
    print(f"r1 <= r2: {r1 <= r2}")
    print(f"r3 > r2: {r3 > r2}")
    print(f"r3 >= r2: {r3 >= r2}")
    print(f"r2 != r1: {r2 != r1}")
