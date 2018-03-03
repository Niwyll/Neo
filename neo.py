from discord.ext import commands
from card_games import CardGame
import asyncio


class Neo(commands.Bot):
	def __init__(self):
		self.game = CardGame()

	async def on_ready(self):
		print('Waked up as ' + self.user.name)