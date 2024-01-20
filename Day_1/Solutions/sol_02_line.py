class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1: Point, p2: Point) -> float:
    """ Расстояние между двумя точками """
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5


# Ломаная линия задана произвольным количеством последовательных точек
points = [Point(2, 4), Point(7, 5), Point(5, -2), Point(0, 6), Point(-12, 0)]

# Задание: Найдите длину ломаной линии
# Variant 1, через индексы
length = 0
for idx in range(len(points) - 1):
    length += distance(points[idx], points[idx + 1])

print("Длина ломаной линии = ", length)

# Variant 2, без индексов
length = 0
prev = None
for point in points:
    if prev is not None:
        length += distance(prev, point)
    prev = point

print("Длина ломаной линии = ", length)


# Variant 3, без индексов
length = 0
previous = points[0]
for point in points:
    length += distance(previous, point)
    previous = point

print("Длина ломаной линии = ", length)
