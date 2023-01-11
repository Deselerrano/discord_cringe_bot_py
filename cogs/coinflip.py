import random
from discord.ext import commands


class coinflip(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("- Coinflip cog loaded")

    @commands.command(
        name="coinflip",
        help="Just r0ll 50/50"
    )
    async def coinflip(self, ctx):
        await ctx.send("Подбрасываем монетку!")
        coin = random.randint(0, 1)
        if coin == 0:
            await ctx.send("Выпадает орёл")
        else:
            await ctx.send("Выпадает решка")

async def setup(bot):
    await bot.add_cog(coinflip(bot))