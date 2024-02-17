from collections import Counter, deque


from pprint import pprint

# Обычный словарь(dict)
# d_usual = dict()
# print(type(d_usual))
# for word in ['spam', 'egg', 'egg', 'spam',
#              'counter', 'counter', 'counter']:
#     # Вернет значение ключа, если есть. Создать пару, если такого ключа нет.
#     d_usual.setdefault(word, 0)
#     d_usual[word] += 1
#
# print(d_usual.get("col", 0))
# # print(d_usual['col'])   # Error: KeyError
# print(d_usual)

# =============
# класс Counter
# =============
# counter = Counter()
# print(type(counter))
# for word in ['spam', 'egg', 'egg', 'spam',
#              'counter', 'counter', 'counter']:
#     counter[word] += 1    # Нет ошибки(в обычном dict будет)
#
# print(counter)
# print(counter['counter'])
# print(counter['collections'])  # Нет ошибки

# # Пример создания на лету.
# print(Counter('count_symbols_in_string'))
#
# # Вернуть 3 самых часто встречающихся элемента
# print(Counter('count_symbols_in_string').most_common(3))
# print(Counter('hello students, language python').most_common(3))
# print(Counter('hello students, language python'))
#
# # Вернуть 2 самых редко встречающихся элемента
# print(Counter('hello students, language python').most_common()[:-3:-1])
# print(Counter('hello students, language python').most_common()[-2:])

# counter = Counter(a=4, b=2, c=0, d=-2)
# counter2 = Counter(a=1, b=2, c=3, d=4)

# Ключи только с положительными значениями
# print('Сложение:\n', counter + counter2)
# print('Вычитание:\n', counter - counter2)  # Counter({'a': 3})
#
# # Ключи с минимальными значениями, строго > 0
# print('Минимальные значения:', counter & counter2)
#
# # Ключи с максимальными значениями, строго > 0
# print('Максимальные значения:', counter | counter2)
#
# # Ключи со всеми значениями (положительные, нулевые и отрицательные)
# counter.subtract(counter2)
# print(counter)
#
# print(f'{+counter = }')  # пары с положительными значениями
# print(f'{-counter = }')  # пары с неположительными значениями
# print(list(counter))  # list(counter.keys())
#
# # вернет все элементы
# print(list(counter.elements()))  # Counter({'a': 3}) -> 'a', 'a', 'a'
# res = Counter('count_symbols_in_string')
# print(f'{res = }')
# print(''.join(res.elements()))
#
# # ========================================================
# print(sum(counter.values()))  # общее сумма по значениям.
# # Можно явный метод total()
# print(counter.total())
# print(counter.__class__.__mro__)
#
# # удалить элементы, встречающиеся менее одного раза.
# counter += Counter()
# print(counter)


"""
Как создать файл
cmd.exe
chcp 65001
py -c "import this" > zen.txt
powershell:
py -c "import this" | out-file zen.txt -encoding utf8
"""
# import re
#
# # https://regex101.com/  [а-яА-ЯёЁ]
# # \w+ - буквы, цифры и _, длина от 1 и более
# words = re.findall(r'[\w\']+', open('zen.txt', encoding="utf8").read().lower())
# print(type(words))
# zen_dict = Counter(words)
# pprint(zen_dict)
# print(zen_dict.total())


# =================================
# Deque FIFO -> First In, First Out
# =================================

# ex = list("python")
# deque_ex = deque(ex)
# print(deque_ex)
# print(deque_ex.__class__.__mro__)

# deque_ex.append('e')      # добавление в конец
# deque_ex.appendleft('a')  # добавление в начало (левый конец)
# print(deque_ex)

# right_elem = deque_ex.pop()
# left_elem = deque_ex.popleft()
# print(deque_ex)
# print(f'{right_elem =}, {left_elem = }')

# deque_ex.extend([10, 11])
# deque_ex.extendleft([98, 99])
# print(deque_ex)

# print(deque_ex.count('p'))
# print(deque_ex[3])
# print(len(deque_ex))

# Перенос n элементов из конца очереди в начало
# deque_ex.rotate(5)
# print(deque_ex)
#
# Перенос n элементов из начала очереди в конец
# deque_ex.rotate(-5)
# print(deque_ex)
# lst = list(deque_ex)
# print(lst, type(lst))

# Параметр maxlen определяет количество элементов в очереди.
# def tail(filename, n=10):
#     """ Возвращает n последних строк файла """
#     with open(filename) as f:
#         return deque(f, maxlen=n)


# print(*tail('zen.txt'), sep='')











