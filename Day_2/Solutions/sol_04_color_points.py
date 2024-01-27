import math


class Point:
    def __init__(self, x, y, color=None):
        self.x = x
        self.y = y
        self.color = color

    def distance(self, other_point) -> float:
        return math.sqrt((other_point.x - self.x) ** 2 + (other_point.y - self.y) ** 2)

    def triangle_perimeter(self, p1, p2)  -> float:
        return self.distance(p1)+self.distance(p2)+p1.distance(p2)





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

# TODO: your code here...


def triangle_square(color):
    three_points = []
    for point in points:
        if point.color == color:
            three_points.append(point)
        if len(three_points) == 3:
            semi_perimeter = (three_points[0].triangle_perimeter(three_points[1], three_points[2])) / 2
            triangle_square = math.sqrt(semi_perimeter * (semi_perimeter - three_points[0].distance(three_points[1]))
                                * (semi_perimeter - three_points[1].distance(three_points[2]))
                                * (semi_perimeter - three_points[2].distance(three_points[0])))
            return triangle_square


print("Площадь красного треугольника = ", triangle_square("red"))
print("Площадь зеленого треугольника = ", triangle_square("green"))
