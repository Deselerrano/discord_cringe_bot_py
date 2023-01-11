from discord.ext import commands
import random


class roll(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("- Roll cog loaded")

    @commands.command(
        name="roll",
        help="/roll + int - roll random number"
    )
    async def roll(self, ctx, max:int):
        await ctx.send(f"Выбираем случайное число от 0 до {max}")
        num = random.randint(0, max)
        await ctx.send(f"Результат - {num}!")

async def setup(bot):
    await bot.add_cog(roll(bot))