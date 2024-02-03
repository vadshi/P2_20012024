from sol_01_card import Card, VALUES


hearts_cards = []
# TODO-1: добавьте в список hearts_cards все червовые карты(от 2-ки до туза)
for value in VALUES:
    hearts_cards.append(Card(value, 'Hearts'))

diamonds_cards = []
# TODO-2: добавьте в список diamonds_cards все бубновые карты(от туза до 2-ки)
for value in VALUES[::-1]:
    diamonds_cards.append(Card(value, 'Diamonds'))

# TODO-3: выведите все карты из списка hearts_cards в терминал через запятую в одну строку:
# Пример вывода: 2♥, 3♥, 4♥ ... A♥
print(*hearts_cards, sep=', ')


