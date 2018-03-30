import discord
import sys
import os
import io
import asyncio
import json
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
            await ctx.send("To boot the member, use the command like this: \n.kick [@user]")
        try:
            await user.kick()
            messages = ['it was about time.', 'take the L.', 'get outta here.', 'get booted!', 'nice try.']
            await ctx.send(f"{user.name}, {random.choice(messages)}")
        except discord.Forbidden:
            await ctx.send("RIP. I don't have permissions to kick!")
            
            
    @commands.command()
    @commands.has_permissions(ban_members = True)
    async def ban(self, ctx, user: discord.Member = None):
        """Swings the mighty Ban Hammer on that bad boy."""
        if user is None:
            await ctx.send("To swing the ban hammer, use the command like this: \n.ban [@user]")
        try:
            await user.ban()
            await ctx.send("BONG! The ban hammer fell on {user.name}.")
        except discord.Forbidden:
            await ctx.send("RIP. I don't have permissions to ban!")

            
    
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def mute(self, ctx, user: discord.Member):
        '''Forces someone to shut up. Usage: .mute [user]'''
        try:
            await ctx.channel.set_permissions(user, send_messages=False)
            await ctx.send(f"**{user.name}**, it's time to shut up.")
        except discord.Forbidden:
            await ctx.send("Watch my permissions! I don't have enough.")
            
            
    @commands.command()
    @commands.has_permissions(ban_members=True)
    async def unmute(self, ctx, user: discord.Member):
        '''Allows someone to un-shut up. Usage: .unmute [user]'''
        try:
            await ctx.channel.set_permissions(user, send_messages=True)
            await ctx.channel.send(f"{user.mention} is now un-shutted up.")
        except discord.Forbidden:
            await ctx.send("Couldn't unmute the user. Uh-oh...")
            
            
    @commands.command()
    @commands.has_permissions(manage_guild = True)
    async def dm(self, ctx, user: discord.Member, *, msg: str):
        """DM someone with ME. .dm [tag person] [msg]"""
        try:
            await user.send(msg)
            await ctx.message.delete()            
            await ctx.send(f"Your DM has reached **{user.name}**.:white_check_mark: ")
        except:
            await ctx.send("Error :x:. Make sure your message is shaped in this way: .dm [tag person] [msg]")
            
            
def setup(bot): 
    bot.add_cog(Moderator(bot))    
