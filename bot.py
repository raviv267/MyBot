import discord
import sys
import os
from discord.ext import commands
bot = commands.Bot(command_prefix=commands.when_mentioned_or('.'),description="Ghost's new Discord bot! \n\nHelp Commands:",owner_id=231028316843278346)
bot.load_extension("cogs.developer")

@bot.event
async def on_ready():
    print('Bot is online!')
    await bot.change_presence(activity=discord.Game(name=f".help | Made by Ghost"))
    
    
@bot.command()
async def ping(ctx):
    """Gets the bot latency. Pong!"""
    color = discord.Color(value=0x00ff00)
    em = discord.Embed(color=color, title='Pong! My latency is:')
    em.description = f"{bot.latency * 1000:.4f} ms"
    await ctx.send(embed=em)
    
    
@bot.command()
async def invite(ctx):
    """Invite me to your server. I'll be fun."""
    await ctx.send("Yay! Another one! -> https://discordapp.com/oauth2/authorize?client_id=428310138890223646&scope=bot&permissions=8")

    
@bot.command()
async def say(ctx, *, message: str):
    '''You say it. Then I say it.'''
    try:
        await ctx.message.delete()
    except discord.Forbidden:
        pass
    await ctx.send(message)  
    
  
bot.run(os.environ.get('TOKEN'))
