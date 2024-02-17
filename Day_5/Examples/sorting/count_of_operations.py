#  Сложность алгоритмов сортировки и типы данных
#  https://www.bigocheatsheet.com/


lst = [3, 9, 9, 23, 1]

lst.append(100)  # 1
print(lst.pop())  # 1
print(max(lst))  # n
print(min(lst))  # n

for item in lst:  # 3n -> O(n)
    foo = item + 2
    print(foo)

lst = [[23, 23, 8, 3],
       [45, 9, 6, 4],
       [7, 78, 3, 9],
       'hell']

for item in lst:  # n^2 + 4n + 4 -> O(n^2)
    for inner_item in item:
        bar = str(inner_item) * 2
    print(bar)
