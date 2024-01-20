class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


def distance(p1: Point, p2: Point) -> float:
    """ Расстояние между двумя точками """
    return ((p1.x - p2.x) ** 2 + (p1.y - p2.y) ** 2) ** 0.5
    
    
# Дан список точек
points = [Point(2, 7), Point(12, 7), Point(5, -2), Point(10, -16), Point(-12, 0)]

# Задание: найдите точку наиболее удаленную от начала координат и выведите ее координаты
# Variant 1
p_zero = Point(0, 0)
max_len = 0
max_point = None
for point in points:
    curr_dist = distance(p_zero, point)
    if curr_dist > max_len:
        max_len = curr_dist
        max_point = point

print(f"Координаты наиболее удаленной точки = {max_point.x, max_point.y}")

# Variant 2
p_zero = Point(0, 0)
max_len = 0
max_point = None
for point in points:
    if (curr_dist := distance(p_zero, point)) > max_len:
        max_len = curr_dist
        max_point = point

print(f"Координаты наиболее удаленной точки = {max_point.x, max_point.y}")

# Variant 3
p_zero = Point(0, 0)
distances = []
for point in points:
    distances.append(distance(p_zero, point))

max_len = max(distances)
max_idx = distances.index(max_len)
print(f"Координаты наиболее удаленной точки = {points[max_idx].x, points[max_idx].y}")
