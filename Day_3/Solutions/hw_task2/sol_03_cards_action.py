from sol_01_card import Card, VALUES, SUITS

cards = []
# TODO-1: в список cards добавьте ВСЕ карты всех мастей
for suit in SUITS:
    for value in VALUES:
        cards.append(Card(value, suit))

repeat_cards = [Card(value, suit) for suit in SUITS for value in VALUES]

# TODO-2: Выведите карты в формате: cards[кол-во] 2♦, 3♦ ... A♦, ....,2♥, 3♥, 4♥ ... A♥
print(f"cards[{len(cards)}]: {', '.join([str(card) for card in cards])}")
