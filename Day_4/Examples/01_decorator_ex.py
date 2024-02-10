# Функция полноправный объект в языке Python:
# • может быть создан во время выполнения;
# • может быть присвоен переменной или полю структуры данных;
# • может быть передан функции в качестве аргумента;
# • может быть возвращен функцией в качестве результата.


# ==========
# Декораторы
# ==========
def null_decorator(func):
    return func


def greet():
    return 'Привет!'


# Механизм работы декоратора
# print("Before:")
# print(greet())
# greet = null_decorator(greet)
# print("After:")
# print(greet())

# Функция декоратор
def uppercase(func):
    def wrapper():
        original_result = func()
        modified_result = "<<<< " + original_result.upper() + " >>>>"
        return modified_result
    return wrapper


# Декоратор
# @uppercase  # тоже самое, что и greet_eng = uppercase(greet_eng)
# def greet_eng() -> str:
#     return 'Hello!'
#
#
# print(greet_eng())  # out -> <<<<HELLO!>>>>
# print(greet_eng)
#
# # Если нужно сохранить и первоначальную функцию,
# # то создаем новую переменную
# greet_eng_new = uppercase(greet_eng)
# print(greet_eng_new())
# print(greet_eng())
# print(null_decorator(greet))
# print(uppercase(greet))

# Функция декоратор
def other(func):
    # Кладем все аргументы декорируемой функции
    # в функцию wrapper
    def wrapper(*args, **kwargs):
        print(f'{args = }')
        print(f'{kwargs = }')
        original_result = func(*args, **kwargs)
        modified_result = original_result - 100
        return modified_result
    return wrapper


# Переопределяем встроенную функцию sum
# sum = other(sum)
# print(sum((100, 100), start=1000))

# Применение нескольких декораторов
def strong(func):
    def wrapper():
        return '<strong>' + func() + '</strong>'
    return wrapper


def emphasis(func):
    def wrapper():
        return '<em>' + func() + '</em>'
    return wrapper


# Порядок применения снизу вверх
# @strong    # Второй по порядку
# @emphasis  # Первый по порядку
# def greet2():
#     return 'Привет!'
#
#
# print(greet2())
#
# # Без сахара
# greet2 = strong(emphasis(greet2))
# print(greet2())
# #
# Функция декоратор
# def trace(func):
#     def wrapper(*args, **kwargs):
#         print(f'ТРАССИРОВКА: вызвана {func.__name__}() '
#               f'с {args}, {kwargs}')
#         original_result = func(*args, **kwargs)
#         print(f'ТРАССИРОВКА: {func.__name__}() '
#               f'вернула {original_result!r}')
#         return '!!!! ' + original_result + ' !!!!'
#     return wrapper
#
#
# @trace
# def say(name, line):
#     return f'{name * 3}: {line} as is'
#
#
# print(say('hi', line='Hello'))
# print('*' * 30)
# print(say('hello', 5.2))
# print('*' * 30)
# print(say(line=10, name='user'))


