import random
from rich import print

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
        return f'{self.value}{SUITS_UNI[self.suit]}'

    def __repr__(self) -> str:
        return f'{self.value}{SUITS_UNI[self.suit]}'

    def equal_suit(self, other_card):
        return self.suit == other_card.suit

    def __gr__(self, other_card):
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
        self.cards = [Card(value, suit) for suit in SUITS for value in VALUES]

    def __str__(self) -> str:
        return f'deck:{len(self.cards)}, Карты: {", ".join([str(i) for i in self.cards])}'

    def __repr__(self) -> str:
        return f'Deck {self}'

    def __len__(self):
        return len(self.cards)

    def show(self):
        # Принцип работы данного метода прописан в 00_task_deck.md
        print(self)
        # print(f'deck:[{len(self.cards)}]: {
        #    ", ".join([str(i) for i in self.cards])}')

    def draw(self, x) -> list[Card]:
        # Принцип работы данного метода прописан в 00_task_deck.md
        cars_in_hand = self.cards[:x]
        self.cards = self.cards[x:]
        return cars_in_hand

    # получение значения по индексу
    def __getitem__(self, item):
        return self.cards.__getitem__(item)

    def shuffle(self):
        random.shuffle(self.cards)


class Player:
    def __init__(self, cards, name='') -> None:
        # Список карт в руке
        self.cards = cards
        self.name = name

    def __str__(self) -> str:
        return f'У игрока {self.name} в руке карт осталось: {len(self.cards)}, карты: {self.cards}'

    def __repr__(self) -> str:
        return self.cards

    # получение значения по индексу
    def __getitem__(self, item):
        return self.cards.__getitem__(item)

    def __len__(self):
        return len(self.cards)

    def get_unbreakable_card(self, in_cards):
        # Так не надо, можно проще
        # [self.cards.append(i) for i in card]
        # self.cards = sorted([i for i in self.cards])
        self.cards.extend(in_cards)
        self.cards.sort()

    def rem_unbreakable_card(self, card):
        self.cards.remove(card)

    def rebound_stroke(self, card=None):
        if card:
            self.rem_unbreakable_card(card)
            return card
        cd = self.cards[0]
        self.rem_unbreakable_card(cd)
        return cd

    def defend(self, card_p2):
        cards_same_suit = sorted(
            [i for i in self.cards if i.equal_suit(card_p2) and i > card_p2])
        if cards_same_suit:
            self.rem_unbreakable_card(cards_same_suit[0])
            return cards_same_suit[0]
        return False


class Game:
    def __init__(self, deck):
        self.deck = deck
        self.player1 = Player(sorted(deck.draw(10)), 'Иван')
        self.player2 = Player(sorted(deck.draw(10)), 'Александр')
        self.current_player = self.player1
        self.resist_player = self.player2
        self.table = []
        self.hod = int()
        self.winner = None

    def check_table(self, player):
        print(f'Карт на столе {self.table}')
        ch = [card_pl for card_pl in player for card_tbl in self.table if card_pl.value == card_tbl.value]
        if ch:
            random_card = random.choice(ch)
            print(f'Игрок {player.name} подкидывает {random_card}')
            return random_card
        return False

    def move(self, player1, player2, card=None):
        pl1 = player1.rebound_stroke(card)
        self.table.append(pl1)
        if card is None:
            print(f'Игрок {player1.name} пошел картой {pl1}')
        pl2 = player2.defend(pl1)
        if pl2:
            print(f'Игрок {player2.name} побил картой {pl2}')
            self.table.append(pl2)
            if len(player1) > 0:
                podkid = self.check_table(player1)
                if podkid:
                    # print('Пора начинать сначало')
                    self.move(player1, player2, podkid)
                else:
                    print(f'Игрок {player1.name} больше ничего не может подкинуть')
                    self.current_player = player2
                    self.resist_player = player1
                    self.hod += 1
        else:
            print(f'Игрок 2 не может отбить и забирает карты')
            player2.get_unbreakable_card(self.table)
            self.hod += 1

    def start_game(self):
        print(self.player1)
        print(self.player2)
        while len(self.deck) or len(self.player1) or len(self.player2):
            self.move(self.current_player, self.resist_player)
            # print(result)
            print(f'Ход {self.hod} закончен')
            self.table = []
            if len(self.player1) < 10 and len(deck) != 0:
                nu_kard = deck.draw(10 - len(self.player1))
                self.player1.get_unbreakable_card(nu_kard)
            if len(self.player2) < 10 and len(deck) != 0:
                nu_kard = deck.draw(10 - len(self.player2))
                self.player2.get_unbreakable_card(nu_kard)
            if len(self.player1) == 0:
                self.winner = self.player1
                print(f'Победил {self.player1.name}')
                break
            elif len(self.player2) == 0:
                self.winner = self.player2
                print(f'Победил {self.player2.name}')
                break
            print(self.current_player)
            print(self.resist_player)
            print(self.deck)



# Создаем колоду
deck = Deck()
deck.shuffle()
# # Выводим колоду в формате указанном в основном задании
games = Game(deck)
games.start_game()