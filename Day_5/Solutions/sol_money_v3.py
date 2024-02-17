from functools import total_ordering


@total_ordering
class Money:
    def __init__(self, ruble, penny):
        self.ruble = ruble + penny // 100
        self.penny = penny % 100
        self.sumrp = self.ruble * 100 + self.penny

    def __str__(self):
        str_0 = ''
        if len(str(self.penny)) < 2:
            str_0 = '0'
        return f'{self.ruble}руб' + ' ' + str_0 + f'{self.penny}коп'

    def __repr__(self):
        return self.__str__()

    def __add__(self, other):
        new_ruble = self.ruble + other.ruble
        new_penny = self.penny + other.penny
        return Money(new_ruble, new_penny)

    def __sub__(self, other):
        if self.penny < other.penny:
            new_penny = (100 + self.penny) - other.penny
            new_ruble = self.ruble - other.ruble - 1
        else:
            new_ruble = self.ruble - other.ruble
            new_penny = self.penny - other.penny
        return Money(new_ruble, new_penny)

    def __mul__(self, n):
        new_penny = self.penny * n
        new_ruble = self.ruble * n
        return Money(new_ruble, new_penny)

    def __eq__(self, other):
        return self.sumrp == other.sumrp

    def __lt__(self, other):
        return self.sumrp < other.sumrp

    def __mod__(self, p):
        percent = round(self.sumrp * p / 100)
        return Money(0, percent)


#  Создаем сумму из 20 рублей и 120 копеек
money1 = Money(20, 120)  # в конструктор можно передать два любых натуральных числа

# Выводим сумму, с учетом максимального кол-ва копеек <= 99 коп
print(money1)  # 21руб 20коп
print(repr(money1))

# Создаем две денежные суммы
money1 = Money(20, 60)
money2 = Money(10, 45)

# Складываем суммы
money3 = money1 + money2
print(money3)  # 31руб 05коп

money3 = money1 < money2
print(money3)  # 31руб 05коп

money3 = money1 * 5
print(money3)  # 31руб 05коп


print(money1.__add__(money2))
print(money1.__sub__(money2))
print(money1.__mul__(2))
print(money1.__eq__(money2))
print(money1.__lt__(money2))
print(money1.__gt__(money2))
print(money1.__ne__(money2))
print(money1.__mod__(20))
