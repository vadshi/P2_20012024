class Point:
    # Конструктор
    def __init__(self, x, y, color='white'):
        self.x = x
        self.y = y
        self.color = color

    # Метод distance возвращает свой результат
    def distance(self, other_point) -> float:
        return ((self.x - other_point.x) ** 2 + (self.y - other_point.y) ** 2) ** 0.5

    # Метод change_color, который меняет состояние экземпляра
    def change_color(self, color) -> None:
        self.color = color

    def info(self) -> None:
        print(f'Point coordinates: {self.x, self.y}')


point1 = Point(10, -8)
point2 = Point(12, 5)
dist = point1.distance(point2)  # Point.distance(point1, point2)
print("Расстояние между точками:")
print(dist)
print(Point.distance(point1, point2))
print(point2.distance(point1))

print(f'Before calling <change_color> method: {point1.color = }')
point1.change_color('red')
print(f'After calling <change_color> method: {point1.color = }')

point1.info()


