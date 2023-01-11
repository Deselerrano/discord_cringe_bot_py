import discord
import random
from discord.ext import commands
from aiohttp import request


class meme(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("- Memes cog loaded")


    @commands.command(
        name = 'meme',
        help = 'lol xd'
    )
    async def meme(self, ctx):

        colour_choices = [0x400000, 0x997379, 0xeb96aa]

        meme_url = "https://meme-api.herokuapp.com/gimme?nsfw=false"
        async with request("GET", meme_url, headers={}) as response:
            if response.status == 200:
                data = await response.json()
                image_link = data["url"]
            else:
                image_link = None

        async with request("GET", meme_url, headers={}) as response:
            if response.status == 200:
                data = await response.json()
                embed = discord.Embed(
                    title=data["title"],
                    url=image_link,
                    colour=random.choice(colour_choices)
                )
                if image_link is not None:
                    embed.set_image(url=image_link)
                    await ctx.send(embed=embed)

            else:
                await ctx.send(f"Finally, IS - {response.status}")


async def setup(bot):
    await bot.add_cog(meme(bot))