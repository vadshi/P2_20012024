def selection_sort(a):
    length = len(a)
    for i in range(length - 1):
        idx_min = i
        for j in range(i + 1, length):
            if a[j] < a[idx_min]:
                idx_min = j
        a[idx_min], a[i] = a[i], a[idx_min]        


array = [30, 3, 5, 1, 2, 3, 5, 4, 2, 34, 43, 24]
selection_sort(array)
print(array)
array = [54, 1, 2, 3, 52, 3, 1, 2, 3, 5, 3, 67, 3, 2, 543]
selection_sort(array)
print(array)
