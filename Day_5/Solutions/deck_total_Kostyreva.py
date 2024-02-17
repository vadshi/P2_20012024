''' Last Edition '''

import random
from rich import print

# Начнем с создания карты
# ♥ ♦ ♣ ♠
VALUES = ('2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A')
SUITS = ('Spades', 'Clubs', 'Diamonds', 'Hearts')
SUITS_UNI = {
    'Spades': '♠',
    'Clubs': '♣',
    'Diamonds': '♦',
    'Hearts': '♥'
}


class Card:
    def __init__(self, value, suit):
        self.value = value  # Значение карты(2, 3... 10, J, Q, K, A)
        self.suit = suit  # Масть карты

    def __str__(self):
        c_value = self.value
        c_suit = SUITS_UNI.get(self.suit)
        return f"{c_value}{c_suit}"

    def __repr__(self):
        c_value = self.value
        c_suit = SUITS_UNI.get(self.suit)
        return f"{c_value}{c_suit}"  # f"Card {c_value}{c_suit}"

    def equal_suit(self, other_card):
        if self.suit == other_card.suit:
            return True
        else:
            return False

    def __gt__(self, other_card):
        '''
        Если у карты больше(старше) значение, то она больше(старше). При равенстве значений, сравниваем масти.
        Старшинство мастей определяем следующее: ♠<♣<♦<♥
        '''
        if VALUES.index(self.value) > VALUES.index(other_card.value):
            return True
        elif VALUES.index(self.value) == VALUES.index(other_card.value):
            return True if SUITS.index(self.suit) > SUITS.index(other_card.suit) else False
        else:
            return False

    def __lt__(self, other_card):
        if VALUES.index(self.value) > VALUES.index(other_card.value):
            return False
        elif VALUES.index(self.value) == VALUES.index(other_card.value):
            return False if SUITS.index(self.suit) > SUITS.index(other_card.suit) else True
        else:
            return True


# Задание: Теперь создадим колоду из 52-ух карт и реализуем все методы
class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = []
        for s in SUITS:
            for v in VALUES:
                c = Card(v, s)
                self.cards.append(c)

    def __str__(self):
        return f"cards[{len(self.cards)}]: {','.join([str(card) for card in self.cards])}"

    def __getitem__(self, item):
        return self.cards.__getitem__(item)

    def show(self) -> None:
        # Принцип работы данного метода прописан в 00_task_deck.md
        print(f"cards[{len(self.cards)}]: {','.join([str(card) for card in self.cards])}")

    def draw(self, x):
        # Принцип работы данного метода прописан в 00_task_deck.md
        ''' метод .**draw**(x) - возвращает x первых карт из колоды в виде списка, эти карты **убираются** из колоды.
        Уточнение: первую карту в списке считаем верхней картой колоды'''
        x_cards = self.cards[:x]
        self.cards = self.cards[x:]
        return x_cards

    def shuffle(self) -> None:
        random.shuffle(self.cards)


"""
Cоздадим имитацию ходов в “Дурака без козырей”:

1. Создайте колоду из 52 карт. Перемешайте ее.
2. Первый игрок берет сверху 10 карт
3. Второй игрок берет сверху 10 карт.
4. Игрок-1 ходит:
    4.1. игрок-1 выкладывает самую маленькую карту по "старшенству"
    4.2. игрок-2 пытается бить карту, если у него есть такая же масть, но значением больше.
    4.3. Если игрок-2 не может побить карту, то он проигрывает/забирает себе(см. пункт 7)
    4.4. Если игрок-2 бьет карту, то игрок-1 может подкинуть карту любого значения, которое есть на столе.
5. Если Игрок-2 отбился, то Игрок-1 и Игрок-2 меняются местами. Игрок-2 ходит, Игрок-1 отбивается.
6. Выведите в консоль максимально наглядную визуализацию данных ходов (библиотека rich)
7* Реализовать возможность добрать карты из колоды после того, как один из игроков отбился/взял в руку
"""


class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []

    def take(self, cards_in):
        self.cards.extend(cards_in)

    def __str__(self):
        return f"cards[{len(self.cards)}]: {','.join([str(card) for card in self.cards])}"

    def cards_min(self):
        return min(self.cards)

    def find_beating_card(self, the_round_card):
        greater_cards_same_suit = []
        for card in self.cards:
            if card.suit == the_round_card.suit and the_round_card < card:
                greater_cards_same_suit.append(card)
        if len(greater_cards_same_suit) == 0:
            print('[u]No beating card, take from the table[/u]')
            return False
        else:
            greater_cards_same_suit_st = sorted(greater_cards_same_suit)
            return greater_cards_same_suit_st[0]

    def one_more_card(self, table):
        # Если игрок-2 бьет карту, то игрок-1 может подкинуть карту любого значения, которое есть на столе.
        table_card_values = []
        for card in table:
            table_card_values.append(card.value)
        table_card_values = list(set(table_card_values))

        cards_to_choose = []
        for card in self.cards:
            if card.value in table_card_values:
                cards_to_choose.append(card)

        print(f"cards_to_choose {cards_to_choose}")

        if len(cards_to_choose):
            return random.choice(cards_to_choose)
        print(f"[u]No card for the next step, clean the table[/u]")
        return False


class Game:
    def __init__(self):
        self.deck = Deck()
        self.deck.shuffle()
        self.attacker = Player('Петя')
        self.attacker.take(self.deck.draw(10))
        self.defender = Player('Коля')
        self.defender.take(self.deck.draw(10))

    def switch_players(self):
        print(f"{self.attacker.name}, {self.defender.name}")
        a = self.attacker
        d = self.defender
        self.defender = a
        self.attacker = d
        print(f"игроки поменялись местами")
        print(f"{self.attacker.name}, {self.defender.name}")

    def round(self):
        table = []
        while len(self.attacker.cards) > 0 and len(self.defender.cards) > 0:
            print(f"начало карты аттакера {self.attacker.cards}")
            print(f"начало карты дефендера {self.defender.cards}")
            table.append(self.attacker.cards_min())  # игрок-1 выкладывает самую маленькую карту по "старшенству"
            print(f"стол после смены хода, аттакер пошел {table}")
            self.attacker.cards.remove(self.attacker.cards_min())
            print(f"карту которую бить [bold red]{table[-1]}[/bold red]")

            while len(table) != 0:
                # игрок-2 пытается бить карту, если у него есть такая же масть, но значением больше.
                # Если игрок-2 не может побить карту, то он проигрывает/забирает себе(см. пункт 7)

                turn_card = self.defender.find_beating_card(table[-1])
                if turn_card is False:
                    print(f"карты аттакера {self.attacker.cards}")
                    print(f"карты дефендера до забора карт {self.defender.cards}")
                    self.defender.take(table)  # не отбился и забирает карты со стола
                    print(f"карты дефендера после забора карт {self.defender.cards}")
                    table = []
                    print(f"дефендер не отбился и забирает карты со стола")
                    # print('по ветке no defeat')

                else:
                    # Если игрок-2 бьет карту, то игрок-1 может подкинуть карту любого значения, которое есть на столе.
                    print(f"дефендер бьется и добаляет карту на стол {turn_card}")
                    table.append(turn_card)  # бьется и добаляет карту на стол
                    print(f"дефендер побил теперь стол [bold green]{table}[/bold green]")
                    self.defender.cards.remove(turn_card)  # исключает свою карту так как побился
                    print(f"карты аттакера {self.attacker.cards}")
                    print(f"карты дефендера {self.defender.cards}")
                    additional_card = self.attacker.one_more_card(table)
                    if additional_card is False:
                        print(f"аттакер не подкидывает")
                        table = []  # очищается стол
                        # print('по ветке no additional card')
                        self.switch_players()
                    else:
                        table.append(additional_card)  # игрок-1 подкидывает карту
                        print(f"После подкидывания стол {table}")
                        self.attacker.cards.remove(additional_card)  # исключает свою карту так как подбросил
                        print(f"карты аттакера {self.attacker.cards}")
                        print(f"карты дефендера {self.defender.cards}")

                if len(self.attacker.cards) == 0:
                    print('[bold magenta]У аттакера нет карт, игра окончена[/bold magenta]')
                elif len(self.defender.cards) == 0:
                    print('[bold magenta]У дефендера нет карт, игра окончена[/bold magenta]')


if __name__ == '__main__':
    firstGame = Game()
    firstGame.round()
