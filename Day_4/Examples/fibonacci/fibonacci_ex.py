import functools

from clockdecorator import clock

# используется механизм: memoization

@functools.lru_cache()
@clock
def fibonacci(n):
    if n < 2:
        return n
    return fibonacci(n - 2) + fibonacci(n - 1)


if __name__ == '__main__':
    import sys
    print(sys.getrecursionlimit())
    sys.setrecursionlimit(3000)
    print(fibonacci(1500))


# Пример рекурсии
# def add(n):
#     # Базовый случай
#     if n == 1:
#         print('Базовый случай')
#         return 1
#     else:
#         print(n)
#         return n + add(n - 1)
#
#
# print(add(5))