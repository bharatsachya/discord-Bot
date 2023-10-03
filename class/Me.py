import discord
from discord.ext import commands

class Me(commands.Cog):
    def __init__(self,client):
        self.client=client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Me.py is ready")

    # @commands.command()
    # async def me(self,ctx):
    #     botLatency=round(self.client.latency*1000)
    #     await ctx.send(f"{botLatency}ms")

    @commands.command(aliases=['myself','pointtome'])
    async def me(self,ctx):
        embedmessage=discord.Embed(title="Who are you?!", description="Meet this mf", color=discord.Color.gold())

        embedmessage.set_author(name=f"{ctx.author.display_name}", icon_url=ctx.author.avatar)
        embedmessage.set_thumbnail(url=ctx.guild.icon)
        embedmessage.set_image(url=ctx.author.avatar)
        embedmessage.add_field(name="fieldname",value="field value", inline=False)
        embedmessage.set_footer(text="👆👆👆This is your image👆👆👆",icon_url=ctx.author.avatar)

        await ctx.send(embed=embedmessage)

async def setup(client):
    await client.add_cog(Me(client))