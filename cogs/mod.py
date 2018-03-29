import discord
import sys
import os
import io
import asyncio
import json
import ezjson
import random
from discord.ext import commands


class Moderator:
    def __init__(self, bot):
        self.bot = bot
        
        
    @commands.command()
    @commands.has_permissions(kick_members = True)
    async def kick(self, ctx, user: discord.Member = None):
        """Kicks a member. Gotta hurt."""
        if user is None:
            await ctx.send("To boot the member, use the command like this: \n*kick [@user] [reason]")
        try:
            await user.kick()
            messages = ['it was about time.', 'take the L.', 'get outta here.', 'get booted!', 'nice try.']
            await ctx.send(f"{user.name}, {random.choice(messages)}")
        except discord.Forbidden:
            await ctx.send("RIP. I don't have permissions to kick!")
            
            
    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, user: discord.Member = Nonee):
        """Swings the mighty Ban Hammer on that bad boy."""
        if user is None:
            await ctx.send("To swing the ban hammer, use the command like this: \n*ban [@user] [days of msgs to delete] [reason]")
        try:
            await user.ban()
            await ctx.send("BONG! The ban hammer fell on {user.name}.")
        except discord.Forbidden:
            await ctx.send("RIP. I don't have permissions to ban!")
            
            
def setup(bot): 
    bot.add_cog(Moderator(bot))    
