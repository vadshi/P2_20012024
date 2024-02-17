import random


def qsort_inplace(lst, start=0, end=None):
    """    Отсортировать список методом быстрой сортировки  """
    def subpart(lst, start, end, pivot_index):
        print('start ->', start, 'end ->', end, end=' ')
        lst[start], lst[pivot_index] = lst[pivot_index], lst[start]
        pivot = lst[start]
        x = start + 1
        y = start + 1

        while y <= end:
            if lst[y] <= pivot:
                lst[y], lst[x] = lst[x], lst[y]
                x += 1
            y += 1

        lst[start], lst[x - 1] = lst[x - 1], lst[start]
        print(f'\nlst after subpart: {lst}')
        return x - 1

    if end is None:
        end = len(lst) - 1
    if end - start < 1:
        return None

    pivot_index = random.randint(start, end)
    print(f'pivot_index = {pivot_index}, value = {lst[pivot_index]}')
    print('lst:', lst)
    x = subpart(lst, start, end, pivot_index)
    print(f' ... result as index of x  = {x} and value = {lst[x]}')
    print('*' * 75)
    qsort_inplace(lst, start, x - 1)
    qsort_inplace(lst, x + 1, end)


array = [54, 1, 2, 3, 52, 3, 1, 2, 3, 5, 3, 67, 3, 2, 543]
print(qsort_inplace(array))


