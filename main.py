#main.py
import os

import discord
from discord.ext import commands
from dotenv import load_dotenv

from cmds import Trivia

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")
client = discord.Client(intents=discord.Intents.default())

bot = commands.Bot(intents=discord.Intents.all(), command_prefix=",")  # bots prefix


# Define an event for when the bot is ready
@bot.event
async def on_ready():
    print(f'{bot.user} has connected to Discord!')


# Define a simple command
@bot.command()
async def ping(ctx):
    await ctx.send('Pong!')

@bot.command()
async def hello(ctx):
    await ctx.send('Hello there!')


bot.run(TOKEN)
