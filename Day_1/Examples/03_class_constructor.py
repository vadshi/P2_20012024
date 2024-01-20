class Point:
    version = 1

    # Конструктор класса
    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y


# Создаем объекты класса с помощью конструктора
point1 = Point(10, -8)
point2 = Point(12, 5)

print("point1.x =", point1.x)
print("point1.y =", point1.y)
print("point1.version =", point1.version)

print("point2.x = ", point2.x)
print("point2.y = ", point2.y)
print("point2.version =", point2.version)

point3 = Point(y=5)  # point3 = Point(0, 5)
print(point3.x)      # Out: 0
print(point3.y)      # Out: 5

# ERROR
# AttributeError: type object 'Point' has no attribute 'x'
# print(Point.x)
# print(Point.y)
# Шаблон вызова: объект, имя_атрибута(str)
print(hasattr(Point, 'x'))   # Out: False
print(hasattr(point1, 'x'))  # Out: True
print(hasattr(point1, 'version'))  # Out: True

Point.x = 12
print(Point.x)  # Out: 12
print(point3.x)  # Out: 0
print(f'{point3.version = }')

# Используем значения по умолчанию
point4 = Point()  # point4 = Point(0, 0)
print(point4.x)  # Out: 0
print(point4.y)  # Out: 0

point5 = Point(x=10)
print(point5.x)  # Out: 10
print(point5.y)  # Out: 0

point4.x = 999
print(point4.x)  # Out: 999

# Экземпляр динамически обновляет информацию из класса
Point.z = 12
# Значения из класса
print(point1.z)  # Out: 12
print(point2.z)  # Out: 12
print(point3.z)  # Out: 12
print(point4.z)  # Out: 12
print(point5.z)  # Out: 12

# Создаем значение атрибута только для point1.z
point1.z = 78

print(point1.z)  # Out: 78
print(point2.z)  # Out: 12
print(point3.z)  # Out: 12
print(point4.z)  # Out: 12
print(point5.z)  # Out: 12

# Удаляем атрибут только для point1.z
del point1.z
print("after del point1.z:")
# Значения из класса
print(point1.z)  # Out: 12
print(point2.z)  # Out: 12
print(point3.z)  # Out: 12
print(point4.z)  # Out: 12
print(point5.z)  # Out: 12

print(point1.y)
del point1.y
# print(point1.y)  # Error
# del point1.w     # Error

Point.version = 2.0
print(point1.version)