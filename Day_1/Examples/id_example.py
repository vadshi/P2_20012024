# Check 1
a = 5
b = 5
print(a == b)  # Out: True
print(a is b)  # Out: True

# Check 2
c = 300
d = 300
print(c == d)  # Out: True
print(c is d)  # Out: True

# Check 3
s1 = 'hello$%^'
s2 = 'hello$%^'
print(s1 == s2)  # Out: True
print(s1 is s2)  # Out: True

# Check 4
lst1 = [45, 3]
lst2 = lst1[:]  # lst1.copy()
print(lst1 == lst2)  # True
print(lst1 is lst2)  # Out: Вспомнить всё и проверить

# # Check 5
lst1 = [45, 3]
lst2 = lst1  # еще одна ссылка
lst2.append(100)
print(lst1 == lst2)  # Out: Вспомнить всё и проверить
print(lst1 is lst2)  # Out: Вспомнить всё и проверить
lst1.pop()
print(lst1, lst2)

# Кортеж - unmutable type
tup1 = ([45], 3)
tup1[0].append(100)
print(f'{tup1 = }')
# tup1[0] = 1  # Error
tup2 = tup1[:]  # tup2 = tup1
print(tup1 == tup2)  # Out: Вспомнить всё и проверить
print(tup1 is tup2)  # Out: Вспомнить всё и проверить

# Контрольный вопрос
s3 = 'hello!@Ж'
s4 = s3[:]  # s4 = s3
print(s3 == s4)   # True
print(s3 is s4)   # Out: Вспомнить и проверить


