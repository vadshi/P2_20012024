"""
## 2.1 Квадрат
сделать класс Square - квадрат, который наследуется от прямоугольника

Класс Point(x: int, y: int)

# прямоугольник создаем на основе двух точек (class Point)
Класс Rect(p1, p2)

rect = Rect(p1: Point, p2: Point)
p1 = left_bottom -> (1, 1)  # левая нижняя
p2 = right_top -> (4, 5)    # правая верхняя
methods: area, perimeter (можно через property)


class Square(Rect):
    def __init__(self, p1, size):
        # ...

    # добавить метод вычисления диагонали
    def diagonal():
        pass
    
sq = Square(p1, 5)  # Квадрат 5x5
print(sq.area())
print(sq.perimeter())
print(sq.diagonal())
print(sq)
"""
from typing import Self


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self: Self, other_point: Self) -> float:
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


# прямоугольник создаем на основе двух точек (class Point)
class Rect:
    def __init__(self, p1: Point, p2: Point) -> None:
        self.a = p2.x - p1.x
        self.b = p2.y - p1.y
        self.p1 = p1
        self.p2 = p2

    def area(self):
        return self.a * self.b

    def perimeter(self):
        return (self.a + self.b) * 2

    def __repr__(self) -> str:
        return f"{self.__class__.__name__}({self.a}, {self.b})"

    def __str__(self) -> str:
        return repr(self)


class Square(Rect):
    def __init__(self, p1, size):
        p2 = Point(p1.x + size, p1.y + size)
        Rect.__init__(self, p1, p2)
        self.size = size

    def diagonal(self):
        return self.size * 2 ** 0.5

    def diag(self):
        return self.p1.distance(self.p2)


if __name__ == "__main__":
    p1 = Point(0, 0)
    p2 = Point(3, 5)
    rect = Rect(p1, p2)
    print(f'{rect = }')
    print(rect.area())
    print(rect.perimeter())
    sq = Square(p1, 5)  # Квадрат 5x5
    print(f'{sq = }')
    print(sq.area())
    print(sq.perimeter())
    print(sq.diagonal())
    print(sq.diag())
