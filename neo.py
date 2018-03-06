from discord import Member
from discord.ext import commands
from card_games import CardGame
import asyncio


class Neo(commands.Bot):
	description = """
		A simple bot used to play mini_games
	"""

	def __init__(self, command_prefix, formatter=None, **options):
		super().__init__(command_prefix, formatter, self.description, **options)
		self.game = CardGame()
		self.gm = None
		self.manage_commands()

	def manage_commands(self):
		self.add_command(self.set_gm_status)
		self.add_command(self.cards)

	@commands.command()
	@commands.has_permissions(administrator=True)
	async def set_gm_status(self, member: Member):
		self.gm = member
		await self.say(member.mention + " is now the new game master !")

	@commands.group(pass_context=True)
	async def cards(self, ctx):
		if type(self.game) is not CardGame:
			await self.say("Selected game isn't a card game")
			return
		if ctx.invoked_subcommand is None:
			await self.say('Invalid command, cards needs an argument')

	@cards.command(pass_context=True)
	async def draw(self, ctx, number:int = 1):
		cards = self.game.pick(ctx.message.author, number)
		await self.whisper('Tu pioches ' + str(cards))
		await self.whisper(ctx.message.author.name + ' a pioché ' + str(cards),
						  destination = self.gm)

	async def on_ready(self):
		print('Waked up as ' + self.user.name)