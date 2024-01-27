# from __future__ import annotations
from typing import Self  # с версии 3.11
import math


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self: Self, other_point: Self) -> float:
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5


class Triangle:
    def __init__(self, p1, p2, p3):
        self.a = p1.distance(p2)
        self.b = p2.distance(p3)
        self.c = p1.distance(p3)

    def perimeter(self):
        return self.a + self.b + self.c

    def area(self):
        # Для нахождения площади, используйте формулу Герона
        p = self.perimeter() / 2
        s = math.sqrt(p * (p - self.a) * (p - self.b) * (p - self.c))
        return s


# Треугольник задан координатами трех точек
triangle = Triangle(Point(2, 4), Point(6, 8), Point(8, 0))

# Задание:
# найдите площадь и периметр треугольника, реализовав методы area() и perimeter()

print(f"Периметр треугольника = {triangle.perimeter():.2f}")
print(f"Площадь треугольника = {triangle.area():.2f}")
