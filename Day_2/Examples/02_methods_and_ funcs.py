import pprint as pp


# # Создаем класс
# class MyClass:
#     def __init__(self, n):
#         self.name = n
#
#
# # Создаем экземпляры класса
# A = MyClass('A')
# B = MyClass('B')
#
#
# # Создаем функцию с параметром self
# def hello(self):
#     print("Этo экземпляр", self.name, ":hello")
#
#
# # Создаем функцию с параметром value
# def hi(value):
#     print(value.name, ":hi")
#
#
# # Ошибка, потому что у строки нет атрибута name
# # hello('value') # AttributeError: 'str' object has no attribute 'name'
#
# # Здесь ошибки не будет
# hello(A)
#
# # Определяем функцию класса
# MyClass.say = hello
# print(MyClass.say)
# pp.pprint(MyClass.__dict__)
#
# # Вызываем метод экземпляра
# A.say()  # 43
#
# # # Вызываем метод экземпляра
# B.say()  # 44
#
# # Вызываем функцию класса
# MyClass.say(A)  # A.say()
# MyClass.say(B)  # B.say()
#
# # Меняем ссылку на функцию
# MyClass.say = hi
#
# # Вызываем метод экземпляра
# A.say()
# print(type(A.say))
# print(A.say)
#
# # Вызываем метод экземпляра
# B.say()
#
# # Вызываем функцию класса
# MyClass.say(A)
# MyClass.say(B)
#
# print('Before:', vars(A))   # Out V1: {'name': 'A'}
#
# # Теперь мы создаем атрибут у экземпляра
# A.say = hello
# print('After:', vars(A))
# #
# # # Обязательно передаем аргумент, потому что
# # # работа идет не через класс МуClass
# A.say(A)
# # A.say()  # Error
# B.say()  # MyClass.say(B)
# pp.pprint(MyClass.__dict__)
# pp.pprint(A.__dict__)
# pp.pprint(B.__dict__)
#
# # Здесь класс MyClass не используем
# A.say(B)   # Out: B - hello
#
# # А здесь класс MyClass используем
# # B.say(A)   # Out: Error  MyClass.say(B, A)
#
# # Удаляем функцию класса
# del MyClass.say
# print("After del:")
# print(vars(A))
# print(vars(B))
# pp.pprint(vars(MyClass))
#
# # Вызываем функцию экземпляра
# A.say(A)
# # Здесь будет ошибка
# B.say()  # AttributeError

# Так можно, но не нужно
class Person:
    def __init__(some, name):
        some.name = name
        print(id(some))

    def add(self, s: str):
        self.name += s
        print(f'{self.name = }')
        print(id(self))
        result = self.third()
        print(f'{result = }')

    def second(abcd):
        abcd.name += ' work'
        print(f'{abcd.name = }')
        print(id(abcd))

    def third(work):
        print(id(work))
        return work.name[:3]


p = Person('Петр')
print(id(p))
print('Before:', p.name)
p.add('!!!')  # Person.add(self=p)  s = '!!!'
print('After:', p.name)
p.second()   # Person.second(abcd=p)

