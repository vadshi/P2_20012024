# Класс Предок
class Super(object):
    # Стандартное поведение
    def method(self):
        print('in Super.method')

    def delegate(self):
        print('START delegate method')
        self.action()
        print('FINISH delegate method')

    # Ожидается перегрузка(переопределение) метода
    def first(self):
        assert False, 'first must be defined'


# Буквальное наследование всех методов из Super
class Inheritor(Super):
    pass


# Заполнение обязательного метода в Provider.action
class Provider(Super):
    def action(self):
        print('in Provider.action')


# Полное замещение метода в Replacer.method (добавить Provider)
class Replacer(Provider, Super):
    def method(self):
        print('in Replacer.method')

    def first(self):
        print('method <first> in Replace defined')


# Расширение поведения метода
class Extender(Super):
    def method(self):
        # начало Extender.method
        print('starting Extender.method')
        Super.method(self)
        print('ending Extender.method')
        # конец Extender.method


if __name__ == '__main__':
    # for klass in (Inheritor, Replacer, Extender):
    #     print(klass)  # class or instance? Классы vs Экземпляры
    #     print('\n' + klass.__name__ + '...')
    #     # Inheritor().method(), Replacer().method(), Extender().method()
    #     klass().method()
    #     print('=' * 40)

    print('Provider...')
    p = Provider()
    p.delegate()  # двойная пробежка
    # i = Inheritor()
    # i.first()  # AssertionError:
    # # print('done')
    r = Replacer()
    r.first()
    # r.delegate()
    # e = Extender()
    # e.first()  # AssertionError:
    #
    # MRO - method resolution order
    print(r.__class__.__mro__)
