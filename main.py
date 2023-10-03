import os
from typing import Any, List, Mapping, Optional
from discord.ext.commands.cog import Cog
from discord.ext.commands.core import Command, Group
from dotenv import load_dotenv
import discord
from discord.ext import commands
import asyncio

load_dotenv()

bottoken=os.getenv('TOKEN')
commandprefix=os.getenv('BOTPREFIX')


# For creating custom help commands.
class customHelpComands(commands.HelpCommand):
    def __init__(self):
        super().__init__()
    
    async def send_bot_help(self, mapping):
        embed_message=discord.Embed(title="Help", description="All commands", color=discord.Color.green)

        embed_message.set_thumbnail(url=self.context.author.guild.icon)

        await self.get_destination().send(embed_message)
    
    async def send_cog_help(self, cog):
        return await super().send_cog_help(cog)
    
    async def send_group_help(self, group):
        return await super().send_group_help(group)
    
    async def send_command_help(self, command):
        return await super().send_command_help(command)

    
    
client = commands.Bot(command_prefix=commandprefix, intents=discord.Intents.all())

@client.event
async def on_ready():
    print("bot is ready and booming!")
    await client.change_presence(activity=discord.Game(f"type {os.getenv('BOTPREFIX')}help for help"))

async def load():
    for filename in os.listdir("./class"):
        if filename.endswith(".py"):
            await client.load_extension(f"class.{filename[:-3]}")

async def main():
    async with client:
        try:
            await load()
            await client.start(bottoken)
        except KeyboardInterrupt:
            print("Exiting...")
        else:
            print("Exiting...")



asyncio.run(main())