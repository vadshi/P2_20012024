class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y


points = [Point(10, -8), Point(12, 5)]

# Выведем координату x первой точки
print(points[0].x)

# Выведем координату y второй точки
print(points[1].y)

# Механизм работы списка не меняется
lst = [str(456), float('890.23'), int('6'), set('890')]
print(lst[0], lst[1], lst[2].denominator)
print(lst[2].as_integer_ratio())  # Out: (6, 1)

print(lst[0][1:])
