import discord
from discord.ext import commands
import json

with open('setting.json','r',encoding='utf8') as jfile:
    jdata = json.load(jfile)

bot = commands.Bot(command_prefix='')

@bot.event
async def on_ready():
    print(">> bot is online <<")

@bot.command()
async def 機器人延遲(ctx):
    await ctx.send(f'{round(bot.latency*1000)}ms')

@bot.command()
async def 你的頭像(ctx):
    pic = discord.File('C:\\Users\\hiwil\\Documents\\GitHub\\genshin_bot\\pic\\ga28kdyivbb71.jpg')
    await ctx.send(file= pic)

@bot.command()
async def 胡桃(ctx):
    if bot.get_channel(id) == bot.get_channel(931567610699599913):
      channel = bot.get_channel(931567610699599913)
      await channel.send(jdata['胡桃pic'])
      await channel.send(jdata['胡桃info'])

bot.run(jdata['TOKEN'])