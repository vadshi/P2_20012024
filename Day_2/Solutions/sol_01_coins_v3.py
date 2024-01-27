import random


class Coin:
    def __init__(self):
        # heads-орел/tails-решка
        self.side = None

    def flip(self):
        """  Подбрасывание монетки """
        self.side = random.choice(['head', 'tail'])
        # return side # Это ошибка, здесь return не нужен


# Задание: создайте список из n-монеток(экземпляров). Подбросьте(flip) все монетки.
# Выведите соотношение выпавших орлов и решек в процентах

# Пояснение: когда вы создаете монетку, то она находится в неопределенном состоянии self.side = None, т.е.
# не выпала ни орлом ни решкой. Монетка "определяется" со стороной(орел/решка),
# только после того, как вы ее подбрасываете(вызываете метод flip())


n = int(input('Введите количество монет: '))
# Плохое решение - логическое ошибка
# 1. Создаем список из n ссылок на одну и ту же монету!
coins = [Coin()] * n

# 2. Подбрасываем мне монетки
for coin in coins:
    coin.flip()

# 3. Считаем кол-во орлов и решек
heads = tails = 0
for coin in coins:
    if coin.side == 'head':
        heads += 1
    elif coin.side == 'tail':
        tails += 1

# 4. Выводим соотношение
print(f"Орлы: {heads / n:.2%}")  # % - умножает на 100 и добавляет знак %
print(f"Решки: {tails / n:.2%}")

print("Check after change one coin:")

coins[0].side = 'head' if coins[0].side == 'tail' else 'tail'
# 3. Считаем кол-во орлов и решек
heads = tails = 0
for coin in coins:
    if coin.side == 'head':
        heads += 1
    elif coin.side == 'tail':
        tails += 1

# 4. Выводим соотношение
print(f"Орлы: {heads / n:.2%}")  # % - умножает на 100 и добавляет знак %
print(f"Решки: {tails / n:.2%}")

