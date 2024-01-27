import math


class Point:
    def __init__(self, x, y, color=None):
        self.x = x
        self.y = y
        self.color = color

    def distance(self, other_point) -> float:
        return math.sqrt((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2)


def triangle_square(p1: Point, p2: Point, p3: Point) -> float:
    # Посчитали стороны
    a = p1.distance(p2)
    b = p2.distance(p3)
    c = p3.distance(p1)

    # Полупериметр и площадь
    sp = (a + b + c) / 2
    square = math.sqrt(sp * (sp - a) * (sp - b) * (sp - c))
    return square


# пример работы метода
p1 = Point(4, 4)
p2 = Point(3, 3)

result = p1.distance(p2)
print(result)


# Дан список точек нарисованных красным(red) и зеленым(green) цветами
# Точно известно, что точек каждого цвета ровно три,
# но порядок точек в списке произвольный
points = [
    Point(2, 7, "red"),
    Point(12, 7, "green"),
    Point(5, -2, "red"),
    Point(4, 8, "green"),
    Point(10, -2, "green"),
    Point(-12, 0, "red")
]
# Все точки одного цвета соединены линиями и образуют треугольник

# Задание-1: доработайте конструктор class Point для хранения цвета точки
# Задание-2: реализуйте метод distance()
# Задание-3: вычислите площади треугольников образованных из точек одного цвета(зеленый и красный)
# для вычисления площади можно использовать формулу Герона:
# math.sqrt(p * (p-a) * (p-b) * (p-c)), где p - это полупериметр

reds = []
greens = []
for point in points:
    if point.color == "red":
        reds.append(point)
    elif point.color == "green":
        greens.append(point)


print("Площадь красного треугольника = ", triangle_square(*reds))
print("Площадь зеленого треугольника = ", triangle_square(*greens))
