from __future__ import annotations
import random

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

    def to_str(self):
        return f'{self.value}{SUITS_UNI[self.suit]}'

    # def equal_suit(self, other_card):
    #     return self.suit == other_card.suit

    def __eq__(self, other_card: Card) -> bool:
        return self.value == other_card.value

    def __gt__(self, other_card: Card) -> bool:
        if self.suit == other_card.suit:
            return VALUES.index(self.value) > VALUES.index(other_card.value)

    def __lt__(self, other_card):
        if self.suit == other_card.suit:
            return VALUES.index(self.value) < VALUES.index(other_card.value)

    def __repr__(self):
        return f'{self.value}{SUITS_UNI.get(self.suit)}'


class Deck:
    def __init__(self):
        self.cards = []

        for suit in SUITS:
            for value in VALUES:
                self.cards.append(Card(value, suit))

    def show(self) -> str:
        return f"Deck[{len(self.cards)}]: {', '.join([str(card) for card in self.cards])}"

    def shuffle(self) -> None:
        random.shuffle(self.cards)

    def draw(self, num_cards: int) -> list[Card]:
        out_cards = []
        out_cards += self.cards[:num_cards]
        del self.cards[:num_cards]
        return out_cards

    def __str__(self):
        return f"Deck[{len(self.cards)}]: {', '.join([str(card) for card in self.cards])}"

    def __repr__(self):
        return str(self)


class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def attack(self):
        card_for_attack = min(vars(self).get('hand'))
        self.hand.remove(card_for_attack)
        return card_for_attack


class Game:
    def __init__(self, max_cards_on_hand=10):
        self.table = []
        self.player1 = Player("Вадим Викторович")
        self.player2 = Player("Стас")
        self.deck = Deck()
        self.deck.shuffle()
        self.max_cards_on_hand = max_cards_on_hand
        self.player1.hand = self.deck.draw(max_cards_on_hand)
        self.player2.hand = self.deck.draw(max_cards_on_hand)
        self.first_move = 1
        self.num_of_match = 1
        self.round()

    def round(self):
        while len(self.player1.hand) > 0 and len(self.player2.hand) > 0:
            print(f'Партия № {self.num_of_match}\n-----------')
            self.num_of_match += 1

            print(f'{self.player1.name} держит в руке: {self.player1.hand} - {[len(self.player1.hand)]} шт.\n'
                  f'{self.player2.name} держит в руке: {self.player2.hand} - {[len(self.player2.hand)]} шт.\n\n')

            self.fight()

            if len(self.player1.hand) == 0:
                print(f"Конец Игры !\n{len(self.player1.hand)} : {len(self.player2.hand)}")
                print(f'{self.player1.name} победил !!!')
            elif len(self.player2.hand) == 0:
                print(f"Конец Игры !\n{len(self.player1.hand)} : {len(self.player2.hand)}")
                print(f'{self.player2.name} победил !!!')

    def fight(self):
        if self.first_move == 1:
            start_player = self.player1
            defender = self.player2
        elif self.first_move == 2:
            start_player = self.player2
            defender = self.player1

        # Первый игрок атакует:
        move1 = start_player.attack()
        print(f'Ходит {start_player.name}: {move1}')
        self.table.append(move1)
        out_str = f'На столе лежат: {self.table}'
        print(f'{out_str: >40}')

        go = 6  # Максимальное кол-во карт для подкидывания
        while go > 0:
            # Второй игрок отбивается
            suitable = []
            for card in defender.hand:
                if card > self.table[-1]:
                    suitable.append(card)

            if len(suitable) == 0:
                print(f'{defender.name} забирает карты со стола')
                defender.hand += self.table
                self.table.clear()
                print(f'                    На столе лежат карты: {self.table}')
                break

            print(f'                    Подходящие карты для защиты: {suitable}')
            defend_card = min(suitable)
            print(f'{defender.name} защищается: {defend_card}')
            self.table.append(defend_card)
            print(f'                    На столе лежат карты: {self.table}')
            defender.hand.remove(defend_card)
            suitable.clear()

            # Первый игрок атакует снова:
            suitable = []
            for card in self.table:
                for card_2 in start_player.hand:
                    if card == card_2:
                        suitable.append(card_2)

            if len(suitable) == 0:
                print(f'{start_player.name} не может больше атаковать')
                print(f'Бито: {self.table}\n')
                self.table.clear()
                self.first_move = 2
                break

            print(f'                    Какие карты можно подкинуть: {suitable}')
            defend_card = min(suitable)
            print(f'{start_player.name} подбрасывает: {defend_card}')
            self.table.append(defend_card)
            print(f'                    На столе лежат карты: {self.table}')
            start_player.hand.remove(defend_card)
            suitable.clear()
            go -= 1

        # Добираем недостающие карты из колоды
        if len(start_player.hand) < self.max_cards_on_hand and len(self.deck.cards):
            need_num = self.max_cards_on_hand - len(start_player.hand)
            print(f'{start_player.name} забирает из колоды карт: {need_num} шт.')
            start_player.hand += self.deck.draw(need_num)

        if len(defender.hand) < self.max_cards_on_hand and len(self.deck.cards):
            need = self.max_cards_on_hand - len(defender.hand)
            print(f'{defender.name} забирает из колоды карт {need} шт.')
            defender.hand += self.deck.draw(need)

        print(f'\nОставшиеся карты в колоде: {self.deck}\n\n\n\n')


game1 = Game()
