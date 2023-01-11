import asyncio
import os
import discord
from discord.ext import commands
from conf import settings

intents = discord.Intents.all()
intents.members = True
bot = commands.Bot(command_prefix=settings['prefix'], intents=discord.Intents.all())


async def load():
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            await bot.load_extension(f'cogs.{filename[:-3]}')


async def main():
    await load()
    await bot.start(settings['token'])

@bot.event
async def on_ready():
    print('Log as {0.user}'.format(bot))
    await bot.change_presence(status=discord.Status.online, activity=discord.Game(settings['game']))
    print(discord.__version__)
    print("Wake up boy!")

asyncio.run(main())
