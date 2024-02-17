from deck_total import Card, Deck
from rich.console import Console
from rich.highlighter import RegexHighlighter
from rich.theme import Theme


class CardHighlighter(RegexHighlighter):
    """Apply style to anything that looks like an email."""

    base_style = "example."
    highlights = [r"(?P<black_card>[0-9JQKA]+[♠♣])",
                  r"(?P<red_card>[0-9JQKA]+[♦♥])"]


theme = Theme({
    "example.black_card": " white",
    "example.red_card": " red"
})
console = Console(highlighter=CardHighlighter(), theme=theme)

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

    def __init__(self, name: str):
        self.name = name
        self.cards: list[Card] = []

    def __str__(self):
        return f"Player {self.name}: cards[{len(self.cards)}]: {', '.join([str(card) for card in self.cards])}"

    def __repr__(self):
        return str(self)

    def has_cards(self) -> bool:
        """Возвращает признак наличия карт на руке"""
        return bool(len(self.cards))

    def number_cards(self) -> int:
        """Возвращает количество карт на руке"""
        return len(self.cards)

    def choose_card(self, cards: list[Card]) -> Card | None:
        """Выбрать карту с руки"""
        choice = min(cards)
        # Done: переписал вместо поиска и удаления элемента по индексу делаем remove
        self.cards.remove(choice)
        return choice

    def make_turn(self, table: list[Card]) -> Card | None:
        """Сделать первый ход / попытаться подбросить карту"""
        if not self.has_cards():
            return None
        if table:
            variants: list[Card] = []
            for card in table:
                # variants += list(filter(card.equal_value, self.cards)) # Убрал использование метода equal_value
                variants += list(filter(lambda x: card.value == x.value, self.cards))
            if not variants:
                return None
            return self.choose_card(variants)
        return self.choose_card(self.cards)

    def beat(self, table: list[Card]) -> Card | None:
        """Попытаться отбиться"""
        card = table[-1]
        # Done: Отбиваемся той же мастью
        variants: list[Card] = list(filter(lambda x: (card.equal_suit(x) and card < x), self.cards))
        if variants:
            return self.choose_card(variants)
        return None

    def take(self, cards: list[Card]) -> None:
        """Взять карты со стола на руку"""
        self.cards += cards
        self.cards = sorted(self.cards)


class Game:

    def __init__(self, _player_1: Player, _player_2: Player, max_cards_on_hand: int = 10):
        self.deck = Deck()
        self.deck.shuffle()
        self.current_player: Player = _player_1
        self.opposite_player: Player = _player_2
        self.max_cards_on_hand: int = max_cards_on_hand
        self.current_player.take(self.deck.draw(max_cards_on_hand))
        self.opposite_player.take(self.deck.draw(max_cards_on_hand))
        self.table: list[Card] = []
        self.turn_number = 0
        self.winner: Player | None = None
        self.game_over: bool = False
        self.swap: bool = True

    def new_turn(self) -> None:
        """Сделать ход"""
        self.turn_number += 1
        console.rule(f"[bold green]Ход {self.turn_number}:")
        console.print(f"Колода: {self.deck.cards}")
        console.print(f"{self.current_player.name}: {self.current_player.cards}")
        console.print(f"{self.opposite_player.name}: {self.opposite_player.cards}")
        console.print(f"\tХодит  {self.current_player.name:>10}", end="")
        console.print(f" ← {self.opposite_player.name} бьётся.")

        while self.opposite_player.has_cards():
            turn = self.current_player.make_turn(self.table)
            if turn:
                self.table.append(turn)
                console.print(f"\t\t{str(turn):>9}", end="")
            else:
                console.print(f"\tБито: {self.table}")
                self.table = []
                break

            beat = self.opposite_player.beat(self.table)
            if beat:
                self.table.append(beat)
                console.print(f" ← {beat}")
                if not self.opposite_player.has_cards():
                    console.print(f"\tБито: {self.table}")
                    self.table = []
                    break
            else:
                self.opposite_player.take(self.table)
                console.print(f" → [bold magenta]Беру...[/bold magenta]")
                console.print(f"\t{self.opposite_player.name} взял {self.table}")
                self.table = []
                self.swap = False  # Done: Если игрок берёт, то смены игроков не происходит
                break

    def take_cards(self) -> None:
        """Добрать карты из колоды. Сначала берёт текущий игрок"""
        for player in [self.current_player, self.opposite_player]:
            if self.deck and (player.number_cards() < self.max_cards_on_hand):
                new_cards = self.deck.draw(self.max_cards_on_hand - player.number_cards())
                if new_cards:
                    player.take(new_cards)
                    console.print(f"\t{player.name} добрал из колоды: {new_cards}")

    def check_winner(self) -> None:
        """Проверить условие победы"""
        if not self.current_player.has_cards() and not self.opposite_player.has_cards():
            self.game_over = True
            console.rule(f"[bold magenta]Ничья.[/bold magenta]")
            return
        for player in [self.current_player, self.opposite_player]:
            if not player.has_cards():
                self.winner = player
                self.game_over = True
                console.rule(f"[green]Игрок [bold cyan]{self.winner.name}[/bold cyan] выиграл.[/green]")
                console.print(f"[bold cyan]{self.current_player.name}[/bold cyan]: {self.current_player.cards}")
                console.print(f"[bold magenta]{self.opposite_player.name}[/bold magenta]: {self.opposite_player.cards}")

    def swap_players(self) -> None:
        """Поменять местами игроков"""
        self.opposite_player, self.current_player = self.current_player, self.opposite_player

    def go(self):
        """Играть до конца"""
        while not self.game_over:
            self.swap = True
            self.new_turn()
            self.take_cards()
            self.check_winner()
            if self.swap:
                self.swap_players()  # Done: Если игрок берёт, то смены игроков не происходит


if __name__ == "__main__":
    player_1 = Player(name="Вася")
    player_2 = Player(name="Петя")
    game = Game(player_1, player_2)
    game.go()
