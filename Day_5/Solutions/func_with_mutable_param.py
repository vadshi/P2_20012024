def bad_func(a: int, lst=[]) -> list:
    lst.append(a)
    return lst


scores = [3, 8, 1]
print(bad_func(100, scores))

print(bad_func(99))   # Out: [99]

print(bad_func(999))  # Out: [999]

print(bad_func(9999))  # Out: [9999]


def good_func(a: int, lst=None) -> list:
    if lst is None:
        lst = []
    lst.append(a)
    return lst


scores = [3, 8, 1]
print(good_func(100, scores))

print(good_func(99))   # Out: [99]

print(good_func(999))  # Out: [999]

print(good_func(9999))  # Out: [9999]
