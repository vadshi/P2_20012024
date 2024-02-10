"""
Напишите функцию-декоратор, оборачивающую результат другой функции в прямоугольник звездочек.
Пояснение: если декорируемая функция возвращает “Привет”, то декоратор должен изменить вывод на:
Пример 1:
********
*Привет*
********
Пример 2:
****
*23*
****
Пример 3:
**************
*[34, 45, 12]*
**************
"""


def stars(function):
    def wrapper(*args, **kwargs):
        result = str(function(*args, **kwargs))
        line = (len(result) + 2) * '*'
        return f'{line}\n*{result}*\n{line}'
    return wrapper


@stars
def func(arg):
    return arg


@stars
def func_two(arg1, arg2):
    return f'{arg1} {arg2}'


# Тестовая часть
print(func('Привет'))
print(func(23))
print(func([34, 45, 12]))
print(func(arg=100))
print(func_two('hello ', 'python'))
