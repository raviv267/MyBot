import discord
import sys
import os
import io
import io
import traceback
import sys
import time
import datetime
import asyncio
import random
import aiohttp
import random
import textwrap
import inspect
from contextlib import redirect_stdout
from discord.ext import commands
bot = commands.Bot(command_prefix=commands.when_mentioned_or('.'),description="= Command List = \n\nUse .help <commandname> for deteails:",owner_id=231028316843278346)
bot.load_extension("cogs.developer")


def dev_check(id):
    if id == 277981712989028353 or id == 231028316843278346:
        return True
    return False


@bot.event
async def on_ready():
    print('Bot is online!')
    await bot.change_presence(activity=discord.Game(name=f".help | Made by Ghost"))

    
@bot.event
async def on_member_join(member):
    if member.guild.id == 403289272548851714:
        serverchannel = bot.get_channel(428498200329191434)
        msg = f"Welcome aboard, {member.mention} to **{member.guild.name}**! :)"
        await serverchannel.send(msg)
    else:
        pass

    

@bot.event
async def on_member_remove(member):
    if member.guild.id == 403289272548851714:
        serverchannel = bot.get_channel(428498200329191434)
        msg = f"Bye Bye {member.mention}"
        await serverchannel.send(msg)
    else:
        pass
    
    
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
    await ctx.send("Yay! thanks for adding me! -> https://discordapp.com/oauth2/authorize?client_id=428310138890223646&scope=bot&permissions=8")

    
@bot.command()
async def say(ctx, *, message: str):
    '''You say it. Then I say it.'''
    try:
        await ctx.message.delete()
    except discord.Forbidden:
        pass
    await ctx.send(message)  
    
    
@bot.command(name='eval', hidden=True)
async def _eval(ctx, *, body):
    """Evaluates python code"""
    if not dev_check(ctx.author.id):
        return await ctx.send("You cannot use this because you are not a developer.")
    env = {
        'ctx': ctx,
        'channel': ctx.channel,
        'author': ctx.author,
        'guild': ctx.guild,
        'message': ctx.message,
    }

    env.update(globals())

    stdout = io.StringIO()
    err = out = None

    to_compile = f'async def func():\n{textwrap.indent(body, "  ")}'

    def paginate(text: str):
        '''Simple generator that paginates text.'''
        last = 0
        pages = []
        for curr in range(0, len(text)):
            if curr % 1980 == 0:
                pages.append(text[last:curr])
                last = curr
                appd_index = curr
        if appd_index != len(text) - 1:
            pages.append(text[last:curr])
        return list(filter(lambda a: a != '', pages))

    try:
        exec(to_compile, env)
    except Exception as e:
        err = await ctx.send(f'```py\n{e.__class__.__name__}: {e}\n```')
        return await ctx.message.add_reaction('\u2049')

    func = env['func']
    try:
        with redirect_stdout(stdout):
            ret = await func()
    except Exception as e:
        value = stdout.getvalue()
        err = await ctx.send(f'```py\n{value}{traceback.format_exc()}\n```')
    else:
        value = stdout.getvalue()
        if ret is None:
            if value:
                try:

                    out = await ctx.send(f'```py\n{value}\n```')
                except:
                    paginated_text = paginate(value)
                    for page in paginated_text:
                        if page == paginated_text[-1]:
                            out = await ctx.send(f'```py\n{page}\n```')
                            break
                        await ctx.send(f'```py\n{page}\n```')
        else:
            bot._last_result = ret
            try:
                out = await ctx.send(f'```py\n{value}{ret}\n```')
            except:
                paginated_text = paginate(f"{value}{ret}")
                for page in paginated_text:
                    if page == paginated_text[-1]:
                        out = await ctx.send(f'```py\n{page}\n```')
                        break
                    await ctx.send(f'```py\n{page}\n```')

    if out:
        await ctx.message.add_reaction('\u2705')  # tick
    elif err:
        await ctx.message.add_reaction('\u2049')  # x
    else:
        await ctx.message.add_reaction('\u2705')

    
  
bot.run(os.environ.get('TOKEN'))
