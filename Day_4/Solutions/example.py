class Player:
    def __init__(self, name):
        self.name = name
        self.cards = []
    
    def take(self, cards_in):
        self.cards.extend(cards_in)

class Game:
	def __init__(self):
		self.deck = Deck()
		self.deck.shuffle()
		self.attacker = Player('John')
        self.attacker.take(self.deck.draw(10))
		
	def round(self):
        while conditions:
            pass
		