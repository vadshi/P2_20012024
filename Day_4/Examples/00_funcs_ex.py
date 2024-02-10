# Функция полноправный объект в языке Python:
# • может быть создан во время выполнения;
# • может быть присвоен переменной или полю структуры данных;
# • может быть передан функции в качестве аргумента;
# • может быть возвращен функцией в качестве результата.

# Создаем для примера функцию
from collections.abc import Callable


# функция для примеров
def func(text: str) -> str:
    return text.upper() + '!'


# print(id(func))
# print(func('привет'))
bar = func  # Ссылка на func
# print(type(bar), id(bar))
# print(bar('пока'))

# Можно удалить func, но bar будет вызываться
del func
# print(func('textest'))  # Out -> Error

# print(bar('Я работаю'))
# print(bar.__name__)
# print(id(bar))
#
# # ## Можно хранить функции в структурах данных
# funcs = [bar, str.lower, str.capitalize]
# print(funcs)
#
# # ## Доступ к функциям, хранящимся внутри списка
# for function in funcs:
#     print(function.__name__, '->', function('проверка Работы'))
#
# # ## Вызов функции как элемента списка по индексу
# print(funcs[0]('первая функция'))
#
# # ## Словарь функций
# d = {'first': str.upper
#      ,'second': bar
#      ,'third': str.capitalize
#      }
#
# print(d['first']('hello'))
# print(d['second']('arg'))
# print(d['third']('foo'))


# ## Передача функции в качестве аргумента в другую функцию
# def greet(fun: Callable) -> None:
#     greeting = fun('Программа на Python')
#     print(greeting)
#
#
# # # ## Вызов функции greet с аргументом - функцией bar
# greet(bar)
# # greet('hello')  # Error
# print(callable(bar))  # есть реализация __call__()
# print(callable('hello'))
# print(bar.__call__("hello"))  # bar('hello')
# print(callable(int))
#
#
# # Вторая функция для примера
# def imp_func(text: str) -> str:
#     return text.lower() + '. Done!'
#
#
# # Вызов функции greet с аргументом - функцией imp_func
# greet(imp_func)

# Полезные модули. Ссылка на документацию
# https://docs.python.org/3/library/itertools.html
# https://docs.python.org/3/library/functools.html
# https://more-itertools.readthedocs.io/en/stable/api.html

# Функции более высокого порядка(higher-order functions)
# map, filter, reduce
# ===
# map
# ===
# print(map(bar, ['hello', 'hi', 'привет']))
# print(set(map(bar, ['hello', 'hi', 'привет'])))
# # numbers = list(map(int, input("Enter: ").split()))
# # print(numbers)
# # strings = tuple(map(bar, input("Enter: ").split(maxsplit=2)))
# # print(strings)
#
# # ## Здесь действует распаковка
# a = map(float, input("Enter: ").split())
# print(f'{a = }')
# print(next(a))  # a.__next__()
# print(next(a))  # a.__next__()
# print(next(a, "I'm empty."))
#
# a, b = map(float, input("Enter: ").split())
# print(f'{a = }, {b = }')

# Здесь отработает
# print(*map(int, '4 8'.split()))

# print(list(map(len, ['hello', 'hi', 'привет'])))

# ======
# filter
# ======
# def condition(text):
#     return len(text) > 3
#
#
# # Включаем элемент в итоговый список, если результат работы
# # функции condition True
# print(list(filter(condition, ['hello', 'hi', 'привет'])))
# # Если первый аргумент None, то в итоговую выдачу попадут только truthy values
# print(tuple(filter(None, [True, 5, 0, '', 8.2, 'hello', False])))


# ======
# reduce
# ======
# def add_two(a, b):
#     print('Привет из функции add_two')
#     print(f'{a = }')
#     print(f'{b = }')
#     print('Функция отработала')
#     print('=' * 40)
#     return a + b
#
#
# from functools import reduce
# print(reduce(add_two, ['hello', 'hi', 'привет'], 'START:'))


# ## Пример функции zip
# ## Объединяет элементы с одинаковым индексом
# a = tuple(range(10))
# b = list(range(11, 17))
# c = list(range(101, 120))
# d = 'hello python'
# print(list(zip(a, b, c, d)))

# Пример на понимание работы словаря
# d = dict(zip('pythonpy', range(8)))
# print(len(d))  # 8(3+) vs 6(2)
# print(d)

# =========
# Замыкания
# =========
# Замыкание (англ. closure) в программировании — функция первого класса,
# в теле которой присутствуют ссылки на переменные, объявленные вне тела
# этой функции в окружающем коде и не являющиеся её параметрами.
# Говоря другим языком, замыкание — функция, которая ссылается на
# свободные переменные в своей области видимости.
# def multiply(num1):
#     # локальная переменная функция,
#     # которая удалится, после вызова функции multiply
#     var = 10
#     var += num1
#     # Вложенная функция
#     def inner(num2):
#         return num1 * num2
#     return inner


# mult_by_9 = multiply(9)   # Это ссылка на inner
# mult_by_10 = multiply(10)  # Это другая ссылка на inner
#
# # Это разные объекты
# print(id(mult_by_9), id(mult_by_10))
# print(mult_by_9)  # Out: <function __main__.multiply.<locals>.inner(num2)>
#
# print(mult_by_9.__closure__)  # Out: (<cell at 0xb0bd5f2c: int object at 0x836bf60>,)
#
# print(mult_by_9.__closure__[0].cell_contents)   # Out: 9
# print(mult_by_10.__closure__[0].cell_contents)  # Out: 10
#
# print([c.cell_contents for c in mult_by_9.__closure__])  # Out: 9
#
# # Вызываем функцию inner с аргументом num2
# print(mult_by_9(10))  # Out: 90
# print(mult_by_9(2))   # Out: 18
# print(mult_by_10(4))  # Out: 40
# print(mult_by_10(5))  # Out: 50
#
# print(mult_by_9.__code__.co_argcount)  # Количество аргументов inner
# print(mult_by_9.__code__.co_freevars)
# print(mult_by_9.__code__.co_name)
#
# # Исходный код функции
# import inspect as ins
# print(ins.getsource(mult_by_9.__code__))

# =================
# Области видимости
# =================
# Local -> Enclosed -> Global -> Builtins (LEGB)
# Вложенные функции
# a = 10
# def main(text: str):
#     # print(a)
#     # a = 5
#     def inner_func(text_1: str) -> str:
#         # Доступ к переменной a в функции main
#         # nonlocal a
#         # Доступ к глобальной переменной a
#         # global a
#         print(a)
#         print(locals())  # Словарь локальных переменных
#         # a += 1  # a = a + 1
#         return text_1.lower() + '...' + f'{a}'
#     # Словарь локальных переменных
#     # print(locals())
#     return inner_func(text)
#
#
# print(main('Привет, Всем '))
# print(f'{a = }')

# print(inner_func('Может работает?')) # Error
# print(main.inner_func) # Error


# Результат работы функции main_imp это идентификатор на функцию,
# которая выбирается в зависимости от значения аргумента
# def main_imp(size: int):
#     def foo(text):
#         return text.lower() + '.' * size
#
#     def bar(text):
#         return text.upper() + '!' * size
#
#     if size > 5:
#         return foo
#     return bar
#
#
# print(main_imp(3))  # out-> function main_imp.<locals>.bar
# print(main_imp(7))  # out-> function main_imp.<locals>.foo
# some_name = main_imp(1)
# print(some_name, type(some_name))
# print(some_name('привет'))
#
# # Вызываем сразу две функции подряд
# print(main_imp(10)('Test'))
# print(main_imp(3)('Student'))

# ## Используем область видимости Enclosed
# def main_imp_2(size: int, text='default'):
#     # Вложенным функциям доступны локальные
#     # переменные родительской функции из
#     # области видимости Enclosed
#     def foo():
#         return text.lower() + '.' * size
#
#     def bar():
#         return text.upper() + '!' * size
#
#     if size > 5:
#         return foo
#     return bar
#
#
# # Вызываем подряд две функции
# print(main_imp_2(10, 'TEST'))  # foo()
# print(main_imp_2(3)())  # Вызвали bar()


# Лямбды(Анонимные функции).
# Нельзя делать связывание в теле функции
# Лямбды возвращает только одно значение
# add = lambda x, y: 3 * x ** 2 + 5 * y + 100
# print(add(2, 3), type(add))
# print(add)
#
# # # ### Вызов лямбды с аргументами
# print((lambda x, y: x + y)(10, 16))
#
# # Можно, но не нужно
# print((lambda *args, **kwargs: (args, kwargs))(4, 5, b='hello', c='hi'))
# print((lambda *args, **kwargs: (args, kwargs))(41, 51))
#
#
# # # Пример функции с любым количеством аргументов
# # # args - это кортеж позиционных аргументов
# # # kwargs - это словарь именованные аргументов
# def func_1(*args, **kwargs):
#     print(args, kwargs)
#
#
# # # Одна и та же функция, но с использованием lambda
# def multiply(num1):
#     return lambda num2: num1 * num2
#
#
# mul_5 = multiply(5)
# print(mul_5(10), type(mul_5), mul_5)
# mul_10 = multiply(10)
# print(mul_10(20))

# lambda в качестве значения аргумента key
# def new_order(x):
#     return x[1]
#
#
# list_of_tuples = [(1, 'd'), (2, 'b'), (4, 'a'), (3, 'c')]
#
# # sorted принимает как аргумент последовательность и всегда возвращает список
# print(sorted(list_of_tuples))
#
# # ## Сортировка по второму значению кортежей
# print(sorted(list_of_tuples, key=lambda x: x[1]))
# print(sorted(list_of_tuples, key=new_order))
# # Out: [(4, 'a'), (2, 'b'), (3, 'c'), (1, 'd')]
#
# # # 0 1 1 4 4 9 9 16 16 25 25 - результат сортировки работы ключа(критерия)
# print(sorted(range(-5, 6), key=lambda x: x * x))
# # Вспомнить всё и проверить
#
# print(sorted(range(5, -6, -1), key=lambda x: x * x))
# # Это пример с lambda
# print(sorted('hello', key=lambda x: ord(x) % 10))


# In: hel545 py5n st495 hel55 hel54 py5n
# result = set(map(lambda x: x.replace('5', '*').replace('4', '*'), input('Enter: ').split()))
# print(len(result))  # Кол-во элементов?
# print(result)

# Примеры с min и max
# s = 'hello python java go golang'
# print(min(s.split(), key=len))  # Out: go
# print(min(s.split(), key=lambda x: x.count('o')))  # java
# #
# print(max(s.split(), key=lambda x: x.count('g')))  # golang
# print(max(s.split(), key=lambda x: x.count('h')))  # hello
# #
# print(min(s.split(), key=lambda x: x.count('n') + len(x)))  # go
#
# print(min(range(13, 20), key=lambda x: x % 3))  # 15
# print(max(range(6, 20), key=lambda x: x % 3))  # 8




