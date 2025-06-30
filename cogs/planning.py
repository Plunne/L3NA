import discord
from discord.ext import commands
from datetime import timedelta, date

MONDAY_IDX = 1
SUNDAY_IDX = 7

CMD_PLANNING_OPTS = [
    "semaine",
    "sem",
    "week",
    "w"
]
    
#############
#    BOT    #
#############

class Planning(commands.Cog):
    
    def __init__(self, in_bot):
        self.bot = in_bot
        
        self.daysteps = [
            "Matin",
            "Apres-Midi",
            "Soir"
        ]
        
        self.weekdays = [
            "Lundi",
            "Mardi",
            "Mercredi",
            "Jeudi",
            "Vendredi",
            "Samedi",
            "Dimanche"
        ]

    def get_nextweek_data(self):
        return date.isocalendar(date.today() + timedelta(weeks=1))
    
    def get_nextweek_day(self, in_day):
        return date.fromisocalendar(self.get_nextweek_data().year, self.get_nextweek_data().week, in_day)
    
    @commands.command(name="planning")
    async def cmd_planning_week(self, ctx, in_arg1=CMD_PLANNING_OPTS[0]):

        if in_arg1 in CMD_PLANNING_OPTS:

            for daystep in self.daysteps:       

                next_monday_str = self.get_nextweek_day(MONDAY_IDX).strftime("%d/%m")
                next_sunday_str = self.get_nextweek_day(SUNDAY_IDX).strftime("%d/%m %Y")

                week_poll = discord.Poll(question=f"Du {next_monday_str} au {next_sunday_str} ({daystep})", duration=timedelta(days=8), multiple=True)

                for weekday in self.weekdays:

                    week_poll.add_answer(text=weekday)
                
                await ctx.channel.send(poll=week_poll)
        else:
            print("[WARNING] Planning !planning : Argument not available!")
            pass


async def setup(bot):
    await bot.add_cog(Planning(bot))