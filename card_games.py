from base_game import BaseGame
from deck import Deck

class NoMoreCardsException(Exception):
	pass

class CardGame(BaseGame):
	# wands of the player, key is hands, value is a list of cards
	wands = {}

	def __init__(self):
		self.deck = Deck()

	def draw(self, member, card_number=1):
		if card_number > len(self.deck.cards):
			raise NoMoreCardsException()
		self.deck.cards, picked_cards = self.deck.cards[card_number:], \
										self.deck.cards[:card_number]
		if id not in self.wands:
			self.wands[member] = []
		self.wands[member] += picked_cards
		return self.wands[member]