# =============================
#    Перегрузка операторов
# =============================
# https://docs.python.org/3/reference/datamodel.html
from __future__ import annotations
from pprint import pprint


class Point(object):
    def __init__(self, x=0.0, y=0.0):
        self.x: float | int = x
        self.y: float | int = y

    def __str__(self):
        return f'Point({self.x}, {self.y})'

    def __repr__(self):
        return str(self)

    # Перегрузка(Переопределение) оператора == (equal)
    def __eq__(self, other: Point):
        # мы будем выполнять оператор == только для точки
        if type(other) is Point:
            return self.x == other.x and self.y == other.y
        else:
            # мы самостоятельно вызываем ошибку TypeError
            raise TypeError('пришло что-то не то')

    # Определение оператора < (less than)
    def __lt__(self, other: Point) -> bool:
        """ Меньше та точка, у которой меньше <х>.
            При одинаковых <x>, та, у которой меньше <y>."""
        if self.x == other.x:
            return self.y < other.y
        return self.x < other.x

    # Определение оператора > (greater than)
    def __gt__(self, other: Point):
        # return not self < other  # можно и так, если экземпляры не могут быть равны
        # Пока лучше все явно прописывать
        if self.x == other.x:
            return self.y > other.y
        return self.x > other.x


class Begemot:
    x = 100
    y = 100


# Тестируем функции класса:
def main():
    p0 = Point(3, 5)
    p1 = Point(3, 5)
    p2 = Point(-1, 7)
    p3 = Point(3, 1.17)

    print('p0=', p0)  # 3 5
    print('p1=', p1)  # 3 5
    print('p2=', p2)  # -1 7
    print('p3=', p3)  # 3 1.17

    # print('p0 == p1:', p0 == p1)  # True
    # print('the same:', p0.__eq__(p1))
    # Если True -> выполнять код дальше
    # Если False -> ошибка AssertionError
    # Смысл assert
    # if p0 == p1:
    #     pass
    # else:
    #     raise AssertionError
    # assert p0 == p1, 'p0, на самом деле, равно p1'  # True, идем дальше по коду
    # print('p1 == p2:', p1 == p2)  # False
    # assert not p1 == p2
    # print('=' * 40)
    #
    # print('p0 != p1:', p0 != p1)  # False
    # # print('__ne__' in dir(p1))   # __ne__ -> !=
    # assert not p0 != p1
    # print('p1 != p2:', p1 != p2)  # True
    # assert p1 != p2
    # print('p0 != p3:', p0 != p3)
    # print('=' * 40)

    # Проверяем методы сравнения
    # print('p2 < p1', p2 < p1)   # True
    # assert p2 < p1
    # print('p1 < p2', p1 < p2)   # False
    # assert not p1 < p2
    # print('=' * 40)
    #
    # print('p3 < p1', p3 < p1)   # True
    # assert (p3 < p1)
    # print('p1 < p3', p1 < p3)   # False
    # assert not p1 < p3
    # print('=' * 40)
    # print('p1 > p2', p1 > p2)
    # print('p1 > p0', p1 > p0)

    # можно использовать min, max, sorted
    # a = (p0, p1, p2, p3)
    # print(a)
    # pmin = min(a)
    # pmax = max(a)
    # print('pmin =', pmin)
    # print('pmax =', pmax)
    # assert p2 is pmin
    # assert p0 is pmax

    # Функция sorted() принимает в качестве аргумента любую последовательность
    # и всегда возвращает список отсортированных элементов
    # b = sorted(a)
    # print(*b, sep=' -> ')  # print(b[0], b[1], b[2], b[3])
    # assert b == [p2, p3, p0, p1]
    #
    # # Проверил интроспекцию
    # pprint('__ne__' in dir(p1))
    # pprint(p1.__class__.__dict__)
    # pprint(Point.__dict__)
    #
    # ===========
    # error block
    # ===========
    beg = Begemot()
    print(f'{beg.x = }, {beg.y = }')
    # print(p0 == beg)   # p0.__eq__(beg) Out: TypeError
    # print(p0 != beg)   # Out: TypeError

    # Механизм работы: beg.__gt__(p0) -> p0.__lt__(beg)
    print(beg > p0)
    print(type(beg))
    print(type(p0))
    print(p0.__lt__(beg))  # True
    print(beg.__gt__(p0))  # NotImplemented

    beg1 = Begemot()
    # print(beg1 == p0)  # p0.__eq__(beg) Error

    # True if x is y else NotImplemented
    # Результат вызова метода __eq__() NotImplemented,
    # потому что мы его не переопределили и id(beg) != id(beg1)
    print(beg.__eq__(beg1))  # NotImplemented
    print(beg is beg)  # id(beg) == id(beg)


if __name__ == '__main__':
    main()
