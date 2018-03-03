from random import shuffle

# Enumerators, could be overrided in subclasses depending of the game type.
# French names because it's a french discord

color_choices = [
	'uncolored',
	'trefle',
	'carreau',
	'coeur',
	'pique',
]

value_choices = [
	'no_value',
	'deux',
	'trois',
	'quatre',
	'cinq',
	'six',
	'sept',
	'huit',
	'neuf',
	'dix',
	'valet',
	'dame',
	'roi',
	'as',
]


class Card:
		def __init__(self, value=value_choices[0], color=color_choices[0]):
			self.value = value
			self.color = color

		def __str__(self):
			return value_choices[self.value] + ' de ' + color_choices[self.color]

class Deck:
	def __init__(self, is_entire=True, is_shuffled=True):
		self.cards = [Card(i, j) for j in range(1, len(color_choices))
								for i in range(1, len(value_choices))]
		if not is_entire:
			self.cards = [card for card in self.cards if card.value >= 7]
		self.cards = self.cards[::-1]
		if is_shuffled:
			shuffle(self.cards)