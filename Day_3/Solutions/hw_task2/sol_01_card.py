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


if __name__ == '__main__':
    # # Создадим несколько карт
    card1 = Card("10", "Hearts")
    card2 = Card("10", "Diamonds")

    # Выведем карты на экран в виде: 10♥ и A♦
    print(card1)
    print(card2)

    # Проверим, одинаковые ли масти у карт
    if card1.equal_suit(card2):
        print(f"У карт: {card1} и {card2} одинаковые масти")
    else:
        print(f"У карт: {card1} и {card2} разные масти")

    # Проверим методы more() и less()
    print(card1.more(card2))
    print(card1.less(card2))

