class Point:
    # Поля(fieds) == атрибуты класса
    x = 7
    y = 4


# Создадим несколько объектов-точек
# Экземпляр(instance)
point1 = Point()
point2 = Point()

# Считываем атрибуты
print(point1.x)  # 7
print(point2.x)  # 7

point1.x = 10
print(point1.x)  # 10
print(point2.x)  # 7

Point.x = -15
print(point1.x)  # 10
print(point2.x)  # -15

print(point1.y)  # 4
print(point2.y)  # 4

Point.z = 999
print(point1.z)  # 999
print(point2.z)  # 999

point2.z = -99
print(point1.z)  # 999
print(point2.z)  # -99

# Удаляем у экземпляра
del point2.z
print(point1.z)  # 999
print(point2.z)  # 999

# Удаляем у класса
del Point.z
# print(point1.z)   # Out: AttributeError:
# print(point2.z)   # Out: AttributeError:

# del point1
# print(point1.x)  # Out: NameError

# Мы можем создавать собственные атрибуты для экземпляров
point1.name = 'first instance'
print(point1.name)
print(point1)
print(f'{hex(id(point1)).upper(): >44}')

del point1.y     # Out: AttributeError:
