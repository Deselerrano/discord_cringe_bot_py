from discord.ext import commands
import aiohttp
import discord
from io import BytesIO



class images(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        print("- Randpics cog loaded")

    @commands.command(
        name = 'thpnex',
        help = 'This person does not exist.'
    )
    async def thispersondoesnotexist(self, ctx):
        async with ctx.channel.typing():
            async with aiohttp.ClientSession() as cs:
                async with cs.get("https://thispersondoesnotexist.com/image") as r:
                    buffer = BytesIO(await r.read())

                    await ctx.send(file=discord.File(buffer, filename='person.png'))

    @commands.command(
        name = 'rndapic',
        help = 'randpic + [dog, cat, panda, fox, racoon] = <3'
    )
    async def animal_pic(self, ctx, animal: str):
        async with ctx.channel.typing():
            animal = animal.lower()
            if (animal in (['dog', 'cat', 'panda', 'fox', 'racoon'])):
                if animal == 'bird':
                    img_url = 'https://some-random-api.ml/animal/birb'
                else:
                    img_url = f'https://some-random-api.ml/animal/{animal}'

                async with aiohttp.ClientSession() as cs:
                    async with cs.get(img_url) as r:
                        if r.status == 200:
                            data = await r.json()

                            embed = discord.Embed(
                                title=f'{animal.upper()}',
                                colour=ctx.author.colour
                            )
                            embed.set_image(url=data['image'])
                            await ctx.send(embed=embed)
                        else:
                            await ctx.send(f"API returned {r.status} code.")
            else:
                await ctx.send("No Image available at the moment.")


async def setup(bot):
    await bot.add_cog(images(bot))