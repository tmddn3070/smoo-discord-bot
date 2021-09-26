from discord.ext import commands
from discord_slash import SlashCommand
from smoobot.config import *
import os

bot = commands.Bot(command_prefix='?')
slash = SlashCommand(bot, sync_commands=True, sync_on_cog_reload=True)

cogs = []
path = "./smoobot/cogs"

for filename in os.listdir(path):
    if filename.endswith('.py'):
        cogs.append(filename)
        bot.load_extension(f'folder.cogs.{filename[:-3]}')
    if filename == '__pycache__':pass

print(f'{len(cogs)}개 코드 로드됨')

bot.run(token)
