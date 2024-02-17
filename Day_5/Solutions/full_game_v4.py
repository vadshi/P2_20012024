import random

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
        return f"{self.value}{SUITS_UNI.get(self.suit)}"

    def __repr__(self):
        return f"{self.value}{SUITS_UNI.get(self.suit)}"

    def eq_suit(self, other_card) -> bool:
        return self.suit == other_card.suit

    def eq_value(self, other_card) -> bool:
        return self.value == other_card.value

    def __gt__(self, other_card):
        if self.value == other_card.value:
            return SUITS.index(self.suit) > SUITS.index(other_card.suit)
        return VALUES.index(self.value) > VALUES.index(other_card.value)

    def __lt__(self, other_card):
        if self.value == other_card.value:
            return SUITS.index(self.suit) < SUITS.index(other_card.suit)
        return VALUES.index(self.value) < VALUES.index(other_card.value)


# Задание: Теперь создадим колоду из 52-ух карт и реализуем все методы
class Deck:
    def __init__(self):
        # Список карт в колоде. Каждым элементом списка будет объект класса Card
        self.cards = []
        for suit in SUITS:
            for value in VALUES:
                self.cards.append(Card(value, suit))

    def __str__(self):
        return f"deck[{len(self.cards)}]: {', '.join([str(card) for card in self.cards])}"

    def __repr__(self):
        return f'deck {self}'

    def show(self):
        # Принцип работы данного метода прописан в 00_task_deck.md
        print(self)

    def draw(self, x) -> list[Card]:
        # Принцип работы данного метода прописан в 00_task_deck.md
        out_cards = self.cards[:x]
        self.cards = self.cards[x:]
        return out_cards

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def __getitem__(self, item):
        return self.cards.__getitem__(item)


class Player:
    def __init__(self, name: str, hand=None):
        self.name: str = name
        self.hand = hand if hand is not None else []

    def __str__(self):
        return f"player[{self.name}, {len(self.hand)} cards]: {self.hand}"

    def __repr__(self):
        return str(self)

    # Игрок атакует
    def attak(self, table: list, cards_to_attak: list):
        if not table:
            table.append(self.hand[0])
            print(f'Ходит {self.name}: {self.hand[0]}')
            del self.hand[0]
        else:
            if cards_to_attak:
                print(f'Можно подкинуть: {cards_to_attak}')
                print(f'{self.name} подкинул: {cards_to_attak[0]}')
                table.append(cards_to_attak[0])
                self.hand.remove(cards_to_attak[0])

    # Игрок защищается
    def defend(self, table: list):

        cards_to_defend = list(filter(lambda x: x > table[-1], list(filter(lambda i: i.eq_suit(table[-1]), self.hand))))
        if not cards_to_defend:
            self.take(cards=table)
            return False
        else:
            print(f'{self.name} бьет: {cards_to_defend[0]}')
            table.append(cards_to_defend[0])
            self.hand.remove(cards_to_defend[0])
            return True

    # Забрать карты со стола в руку
    def take(self, cards: list[Card]) -> None:
        self.hand += cards
        print(f"{self.name} не смог отбиться и забирает карты")

    # Добрать карты
    def get_cards(self, deck: Deck) -> None:
        if len(self.hand) < 10:
            self.hand += deck.draw(10 - len(self.hand))


class Game:
    def __init__(self):
        self.player_1 = Player(input('Введите имя игрока: '))
        self.player_2 = Player(input('Введите имя игрока: '))
        self.first_player = None
        self.second_player = None
        self.cards_to_attak = []
        self.deck = Deck()
        self.table: list[Card] = []
        self.moves = 0
        self.winer = None

    # Запуск игры
    def start(self):
        print('Игра началась!')
        self.deck.shuffle()
        self.player_1.hand = sorted(self.deck.draw(10))
        self.player_2.hand = sorted(self.deck.draw(10))
        self.first_player = self.player_1
        self.second_player = self.player_2

        while self.winer == None:
            self.new_round()
            if self.deck or self.player_1.hand or self.player_2.hand == []:
                self.who_wines()

        print(f'Игра окончена. Победитель {self.winer}')

    # Новый ход
    def new_round(self):
        self.moves += 1
        self.cards_to_attak = []
        self.table = []
        self.player_1.hand.sort()
        self.player_2.hand.sort()
        print(f'{self.moves} Ход')
        print(f'{self.player_1.name}: {self.player_1.hand}')
        print(f'{self.player_2.name}: {self.player_2.hand}')

        while self.cards_to_attak != [] or self.table == []:
            self.first_player.attak(table=self.table, cards_to_attak=self.cards_to_attak)
            if self.second_player.defend(table=self.table):
                self.cards_to_attak = []
                for i in self.first_player.hand:
                    for x in self.table:
                        if i.eq_value(x):
                            self.cards_to_attak.append(i)
                if len(self.cards_to_attak) == 0:
                    print(f'{self.second_player.name} отбился')
                    self.first_player = self.player_2
                    self.second_player = self.player_1
                    break
            else:
                self.table = []
                break

            print(f'Стол: {self.table}')

        self.table = []
        self.player_1.get_cards(deck=self.deck)
        self.player_2.get_cards(deck=self.deck)
        print(f'Конец хода {self.moves}')
        print('*' * 40)

    # Определяем победителя
    def who_wines(self):
        if len(self.player_1.hand) == len(self.player_2.hand) == 0:
            self.winer = 'Ничья'

        elif len(self.player_1.hand) == 0:
            self.winer = self.player_1.name

        elif len(self.player_2.hand) == 0:
            self.winer = self.player_2.name


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
# Создаем игру
new_game = Game()
new_game.start()
