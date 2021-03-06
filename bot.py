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
bot = commands.Bot(command_prefix=commands.when_mentioned_or('.'),description="= Command List ⚠️ = \n\nUse .help <commandname> for deteails:",owner_id=231028316843278346)
bot.remove_command("help")
bot.load_extension("cogs.fun")
bot.load_extension("cogs.developer")
bot.load_extension("cogs.mod")
bot.load_extension("cogs.help")

def dev_check(id):
    if id == 277981712989028353 or id == 231028316843278346:
        return True
    return False


@bot.event
async def on_ready():
    print('Bot is online!')
    await bot.change_presence(activity=discord.Game(name=f".help | Made by Ghost"))

    
@bot.event
async def on_message(message):
    if message.guild.id == 372526440324923393:
        pass
    else:
        if "https://discord.gg/" in message.content:
            await message.delete()
            await message.channel.send("Hey there! Don't advertise your servers in this one. :thumbsdown:", delete_after=5)
        else:
            pass
    await bot.process_commands(message)
    
@bot.event
async def on_member_join(member):
    if member.guild.id == 403289272548851714:
        serverchannel = bot.get_channel(425376875553226753)
        msg = f"Welcome aboard, {member.mention} to **{member.guild.name}**! :)"
        await serverchannel.send(msg)
    else:
        pass

    

@bot.event
async def on_member_remove(member):
    if member.guild.id == 403289272548851714:
        serverchannel = bot.get_channel(425376875553226753)
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
async def say(ctx, *, message: str):
    '''You say it. Then I say it.'''
    try:
        await ctx.message.delete()
    except discord.Forbidden:
        pass
    await ctx.send(message)  
    
    
@bot.command()
async def invite(ctx):
    """Invite me to your server. I'll be fun."""
    await ctx.send("Yay! thanks for adding me! -> https://discordapp.com/oauth2/authorize?client_id=428310138890223646&scope=bot&permissions=8")



        
@bot.command(aliases=['8ball'])
async def eightball(ctx, *, question=None):
    """True or False?"""
    if question is None:
        await ctx.send("Ask a question to USE 8ball!")
    else:
        choices = ['It is certain. :white_check_mark:', 'It is decidedly so. :white_check_mark:', 'Without a doubt. :white_check_mark:', 'Yes, definitely. :white_check_mark:', 'You may rely on it. :white_check_mark:', 'As I see it, yes. :white_check_mark:', 'Most likely. :white_check_mark:', ' Outlook good. :white_check_mark:', 'Yes. :white_check_mark:', 'Signs point to yes. :white_check_mark:', 'Reply hazy, try again. :large_orange_diamond: ', 'Ask again later. :large_orange_diamond: ', 'Better not tell you now. :large_orange_diamond: ', 'Cannot predict now. :large_orange_diamond: ', 'Concentrate and ask again. :large_orange_diamond: ', 'Do not count on it. :x:', 'My reply is no. :x:', 'My sources say no. :x:', 'Outlook not so good. :x:', 'Very doubtful. :x:']
        color = discord.Color(value=0x00ff00)
        em = discord.Embed(color=color, title=question)
        em.description = random.choice(choices) 
        em.set_author(name="The Mighty 8 ball", icon_url="https://vignette.wikia.nocookie.net/battlefordreamislandfanfiction/images/5/53/8-ball_my_friend.png/revision/latest?cb=20161109021012")
        em.set_footer(text=f"Sent by {ctx.message.author.name}")
        try:
            await ctx.message.delete()
        except discord.Forbidden:
            pass
        await ctx.send(embed=em)
        
    
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
