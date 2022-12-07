import os
import discord
from discord.ext import commands
from keep_alive import keep_alive

intents = discord.Intents.default()
intents.message_content = True

client = commands.Bot(command_prefix = '!',intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.command()
async def hello(ctx):
  await ctx.send("Hello!")

@client.command()
async def trenink(ctx):
  trenink = discord.Embed(title="Trenink",url="https://duckduckgo.com/",description="Popisek treninku", color=0x21cd18)
  await ctx.send(embed=trenink)

keep_alive()
client.run(os.getenv('TOKEN'))