# Красивый вывод словаря(вертикально)
from pprint import pprint


class People:
    """ class for learning """
    name = "Teachers"


# Встроенный(системный)
# print(People.__name__)
# People.__name__ = 'Some people'
# print(People.__name__)

# Сами создаем в классе
# print(People.name)
# print(id(People))
# p = People()       # создаю экземпляр на основе класса People
# print(p.name)
# P1 = People        # еще одна ссылка на класс People
# person1 = P1()     # создаю экземпляр на основе класса People
# print(p is person1)
# print(type(p), type(person1))
# print(id(P1))
# print(id(People) == id(P1))
# print(People is P1)
# print(p)  # repr(p)
# print(f'{hex(id(p)).upper(): >45}')

# ==========================================
#   Объект живет, пока есть ссылка на него
# ==========================================
# del People
# p3 = p()  # error
# doubt_p = P1()  # Вспомнить и проверить
# print(doubt_p)
# print(P1.__name__)
# p2 = People()  # Out: NameError: name 'People' is not defined
# del P1
# print(p.name)   # Вспомнить и проверить
#
#
# # Получаем словарь объекта
# print(vars(p))
# # Создаем снова имя(ссылку) People
# People = type(p)
#
# print(id(People))
# p9 = People()
# print(type(p9))
# pprint(vars(People))
# # ======================================
#
# # class People, создаю новый экземпляр
# print(type(p))
# print(id(p))
# new_p = type(p)()  # new_p = People()
# print(type(new_p))
# print(new_p)
# print(id(new_p))
#
# # # ## Получаю доступ к классу экземпляра
# print(p.__class__)  # type(p)
# print(new_p.__class__)  # type(new_p)
# print(id(p.__class__))
# print('=' * 40)
#
# # # ## Создаем экземпляр
# p2 = p.__class__()  # p2 = People()
# print(type(p2), p2)
# print('=' * 40)
# print(id(People))
# print(id(p.__class__))
# P3 = p2  # это ссылка на экземпляр
# print(P3 is p2)
# print(P3 is p2.__class__)

# Получаю доступ к классу экземпляра
# и затем к имени класса
# p = People()
# print(p.__class__.__name__)  # Out: People
# print(vars(p))
# # del p.name  # error
# # del p.__class__.name  # work
# print(p.name)  # Out: Teachers
# p.__class__.__name__ = "Person"
# print(p.__class__.__name__)
# print(People.__name__)
#
# # Но здесь ошибка!
# # print(p.__name__)  # AttributeError
# print(type(People))  # <class 'type'>
# print(People.__class__)
# p4 = People()
# print(p4.__class__.__name__)

# ===========================
# # Доступ к полям класса.
# # Получаем словарь объекта
# ===========================
# p = People()
# pprint(People.__dict__)  # vars(People)
# People.count = 20
# print(p.count)
# print(p.name)
# pprint(People.__dict__)
# pprint(p.__dict__)  # Out: {}
#
# # Создаем значение для атрибута экземпляра
# p.count = 30
# pprint(p.__dict__)
# pprint(p.__class__.__dict__)  # People.__dict__
# print(p.count)
# print(p.__class__.count)    # People.count
# print(vars(p).get('name'))  # None
# print(vars(p).get('count'))  # 30
#
# # Проверка наличия атрибута у экземпляра
# print(hasattr(p, 'name'))  # p.name
#
# del People.name
# pprint(People.__dict__)
# # print(p.name)  # AttributeError
# del People.count
# pprint(People.__dict__)
# print(p.count)  # Ошибки не будет
#
# p.name = 'Students'
# p.age = 22
# pprint(p.__dict__)
#
# # функция vars покажет словарь атрибутов объекта
# print(vars(p))
# pprint(vars(People))

# Меняем значение атрибута класса через экземпляр
p = People()
# p.__class__.name = 'SName'  # People.name = 'SName'
# pprint(People.__dict__)
# print(p.__dict__)

# ==========================================
# Функции getattr, setattr, delattr, hasattr
# ==========================================
# value = 'name'
# # # Шаблон вызова: имя объекта, имя атрибута
# print(getattr(People, value))  # Out: People.name -> SName
#
# # Вернет третий аргумент, если атрибута нет
# print(getattr(People, 'name2', 'Такого нет'))
# # # print(People.name2)   # AttributeError
# #
# # Шаблон вызова: имя объекта, имя атрибута, значение атрибута
# field_name = 'course'
# setattr(People, field_name, 'Python')  # People.course = 'Python'
# pprint(People.__dict__)
# print("before:")
# print(p.__dict__)
# setattr(p, field_name, 'Golang')
# print("after:")
# print(p.__dict__)

# # Пример использования функции setattr
# from string import ascii_letters as chars
# from random import choice
# # choice вернет случайный элемент из последовательности
# new_field = choice(chars)
# print(f'{new_field = }')
# setattr(People, new_field, 1)
# pprint(vars(People))
# print(getattr(p, new_field))
#
# # ## Удаляем атрибут
# # ## Шаблон вызова: имя объекта, имя атрибута
# delattr(People, 'course')
# pprint(People.__dict__)


# p.age = 22
# pprint(vars(p))
# # # проверка наличия атрибута у объекта(класс, экземпляр)
# print(hasattr(People, 'age'), hasattr(People, 'name'))
# print(hasattr(p, "name"), hasattr(p, 'age'))
# print(p.name)
#
#
# # Проверка понимания
# People.some = 567
# # Это не только проверка словаря экземпляра, но и класса
# print(hasattr(p, 'some'))  # Вспомнить и проверить
# print(p.some)
# print(vars(p).get("some"))
# print(getattr(p, 'some'))  #

# =============
# Методы класса
# =============
# class Student:
#     def __init__(self, name='Ivan'):
#         self.name = name
#         self.surname = 'Ivanov'
#
#     def hello1(self) -> None:   # list.append(), list.insert(), list.remove(), list.sort(), dict.update()
#         self.name += ' Ivanovich'
#
#     def hello3(self) -> None:
#         print(self.name, self.surname)
#
#     def hello2():
#         print('Hello, Student')
#
#
# print(f'{id(Student) = }')
# print(Student.hello1)
# print(id(Student.hello1))
# sb = Student()
# print(f'{id(sb) = }')
# print(sb.hello1)
# print(id(sb.hello1))
#
# # Работаем через класс
# sb.hello1()  # Student.hello1(sb)
# print(sb.name)
# # Student.hello1(sb)  # sb.hello1()
# # print(sb.name)
#
# # ## Два одинаковых вызова
# sb.hello3()
# Student.hello3(sb)  # sb.hello3()
#
# # # Важный момент с hello2()
# Student.hello2()      # Отработает
# # sb.hello2()         # TypeError
# # Student.hello2(sb)  # TypeError
#
# print(sb.__dict__)
# print(sb.hello1.__self__)
# print(f'{hex(id(sb)).upper(): >46}')
#
# # print(sb.__self__)  # AttributeError
# print(hex(id(sb)))
# print(sb.hello1.__func__)
# print(type(sb.hello1))
# print(type(sb.name))

