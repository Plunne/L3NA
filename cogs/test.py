from discord.ext import commands

#############
#    BOT    #
#############

class Test(commands.Cog):
    
    def __init__(self, in_bot):
        self.bot = in_bot
    
    @commands.command(name="test")
    async def cmd_test(self, ctx):
        await ctx.channel.send("Test")

async def setup(bot):
    await bot.add_cog(Test(bot))