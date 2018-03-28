import discord
from discord.ext import commands


class Developer:
    def __init__(self, bot):
        self.bot = bot
        
        
    def dev_check(self, id):
       if id == 277981712989028353 or id == 231028316843278346:
           return True
       return False


    @commands.command()
    async def changename(self, ctx, *, name=None):
        if not self.dev_check(ctx.author.id):
            return await ctx.send("Sorry, but this command is for devs only. ¯\_(ツ)_/¯")
        await self.bot.user.edit(username=name)
        await ctx.send(f"My name is now changed to: **{name}**")


@bot.command()
async def say(ctx, *, message: str):
    '''You say it. Then I say it.'''
    try:
        await ctx.message.delete()
    except discord.Forbidden:
        pass
    await ctx.send(message)  
        if not self.dev_check(ctx.author.id):
            return await ctx.send("Sorry, but this command is for devs only. ¯\_(ツ)_/¯")

        

    @commands.command()
    async def restart(self, ctx):
        if not self.dev_check(ctx.author.id):
            return await ctx.send("Sorry, but this command is for devs only. ¯\_(ツ)_/¯")
        await ctx.send("Turning off...Till next time!")
        await self.bot.logout()
        
def setup(bot): 
    bot.add_cog(Developer(bot))  
