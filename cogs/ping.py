from discord.ext import commands


class ping(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("- Ping cog loaded")

    @commands.command(
        name="ping",
        help="Check bot ping"
    )
    async def ping(self, ctx):
        await ctx.send(f"Пинг бота - {round(self.bot.latency * 1000)} мс")

async def setup(bot):
    await bot.add_cog(ping(bot))