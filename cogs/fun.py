import discord
import sys
import os
import io
import asyncio
import aiohttp
import random
import json
from discord.ext import commands


class Fun:
    def __init__(self, bot):
        self.bot = bot
        
        
            
    @commands.command()
    async def hack(self, ctx, user: discord.Member):
        """Hack someone's account!"""
        msg = await ctx.send(f"Currently hacking: **{user}**")
        await asyncio.sleep(2)
        await msg.edit(content="Please wait while we grab the information... [▓▓                  ]")
        await asyncio.sleep(2)
        await msg.edit(content="Please wait while we grab the information... [▓▓▓▓                ]")
        await asyncio.sleep(2)
        await msg.edit(content="Please wait while we grab the information... [▓▓▓▓▓▓              ]")
        await asyncio.sleep(2)
        await msg.edit(content="Please wait while we grab the information... [▓▓▓▓▓▓▓▓            ]")
        await asyncio.sleep(2)
        await msg.edit(content="Please wait while we grab the information... [▓▓▓▓▓▓▓▓▓▓          ]")
        await asyncio.sleep(3)
        await msg.edit(content="Please wait while we grab the information... [▓▓▓▓▓▓▓▓▓▓▓▓        ]")
        await asyncio.sleep(3)
        await msg.edit(content="Please wait while we grab the information... [▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓▓    ]")
        await asyncio.sleep(4)
        await msg.edit(content=f"An error has occurred while hacking **{user}**. Please try again later. :negative_squared_cross_mark:") 
    
        
    @commands.command()
    async def roast(self, ctx, user: discord.Member = None):
        '''Roast someone! If you suck at roasting them yourself.'''
        lol = f"Hey, {user.mention}! " if user is not None else ""
        roasts = ["I'd give you a nasty look but you've already got one.", "If you're going to be two-faced, at least make one of them pretty.", "The only way you'll ever get laid is if you crawl up a chicken's ass and wait.", "It looks like your face caught fire and someone tried to put it out with a hammer.", "I'd like to see things from your point of view, but I can't seem to get my head that far up your ass.", "Scientists say the universe is made up of neutrons, protons and electrons. They forgot to mention morons.", "Why is it acceptable for you to be an idiot but not for me to point it out?", "Just because you have one doesn't mean you need to act like one.", "Someday you'll go far... and I hope you stay there.", "Which sexual position produces the ugliest children? Ask your mother.", "No, those pants don't make you look fatter - how could they?", "Save your breath - you'll need it to blow up your date.", "If you really want to know about mistakes, you should ask your parents.", "Whatever kind of look you were going for, you missed.", "Hey, you have something on your chin... no, the 3rd one down.", "I don't know what makes you so stupid, but it really works.", "You are proof that evolution can go in reverse.", "Brains aren't everything. In your case they're nothing.", "I thought of you today. It reminded me to take the garbage out.", "You're so ugly when you look in the mirror, your reflection looks away.", "Quick - check your face! I just found your nose in my business.", "It's better to let someone think you're stupid than open your mouth and prove it.", "You're such a beautiful, intelligent, wonderful person. Oh I'm sorry, I thought we were having a lying competition.", "I'd slap you but I don't want to make your face look any better.", "You have the right to remain silent because whatever you say will probably be stupid anyway."]
        await ctx.send(f"{lol}{random.choice(roasts)}")
        
    
    @commands.command()
    async def dogmeme(self, ctx):
        """Make a dog meme with this awesome command!"""
        one = await ctx.send("Please enter the text you want on the top half of the meme.")
        try:
            x = await self.bot.wait_for("message", check=lambda x: x.channel == ctx.channel and x.author == ctx.author, timeout=60.0)
        except asyncio.TimeoutError:
            return await ctx.send("Request timed out. Please try again.")
        two = await ctx.send("Great! Now enter the text you want on the bottom half of the meme.")
        try:
            f = await self.bot.wait_for("message", check=lambda f: f.channel == ctx.channel and f.author == ctx.author, timeout=60.0)
        except asyncio.TimeoutError:
            return await ctx.send("Request timed out. Please try again.")
        await ctx.message.delete()
        await one.delete()
        await x.delete()
        await two.delete()
        await f.delete()
        em = discord.Embed(color=discord.Color(value=0x00ff00), title="Done my magic! Here's your dank meme.")
        em.set_image(url=f"https://memegen.link/doge/{x.content.replace(' ', '_')}/{f.content.replace(' ', '_')}.jpg")
        await ctx.send(embed=em)
    
        
    @commands.command()
    async def insult(self, ctx, user: discord.Member = None):
        """You insult me i insult you!"""
        try:
            await ctx.message.delete()
        except discord.Forbidden:
            pass
        if user is None:
            await ctx.send("Who are you insulting? Me? :thinking:")
        else:
            insults = ['fuck you', 'go suck my dick', 'suck my dick', 'fucking gay', 'you little bitch', 'can you fuck off already?', 'fu, smd', 'hope you die']
            await ctx.send(f"{user.mention}, {random.choice(insults)}")
            
        
    @commands.command()
    async def kill(self, ctx, user: discord.Member = None):
        """Kill someone. DIE!"""
        if user is None:
            msg = await ctx.send("Didn't enter anyone, so guess I'm coming for you. :dagger:")
            await asyncio.sleep(3)
            await msg.edit(content=f"Swoooooosh. **{ctx.author.name}** died. :skull_crossbones:")
        else:
            msg = await ctx.send(f"{user.mention}, I'm coming for you. :dagger:")
            await asyncio.sleep(3)
            await msg.edit(content=f"Swoooooosh. **{user.name}** died to **{ctx.author.name}**. :skull_crossbones:")
            
            

def setup(bot):
    bot.add_cog(Fun(bot))
