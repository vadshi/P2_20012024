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

    def equal_suit(self, other_card) -> bool:
        return self.suit == other_card.suit

    def more(self, other_card):
        if self.value == other_card.value:
            return SUITS.index(self.suit) > SUITS.index(other_card.suit)
        return VALUES.index(self.value) > VALUES.index(other_card.value)

    def less(self, other_card):
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
        return str(self)

    def show(self) -> None:
        # Принцип работы данного метода прописан в 00_task_deck.md
        print(self)

    def draw(self, x) -> list[Card]:
        # Принцип работы данного метода прописан в 00_task_deck.md
        out_cards = self.cards[:x]
        self.cards = self.cards[x:]
        return out_cards

    def shuffle(self) -> None:
        random.shuffle(self.cards)


# Создаем колоду
deck = Deck()

# Выводим колоду в формате указанном в основном задании
print(deck)

# Тасуем колоду
deck.shuffle()
deck.show()

# Возьмем 5 карт "в руку"
hand = deck.draw(5)

# Выводим колоду, чтобы убедиться что 5 верхних карт отсутствуют
deck.show()

# Выводим список карт "в руке"(список hand)
print(hand)
