import discord
from discord.ext import commands

bot = commands.Bot(command_prefix='g')

@bot.event
async def on_ready():
    print(">> bot is online <<")

bot.run("OTMxNzc0MTkxMDE4MDcwMDQ2.YeJUVg.VlS--679fURuRMyfvqUB3GsKWAc")