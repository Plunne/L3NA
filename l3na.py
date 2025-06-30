import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from os.path import dirname, abspath, join

###############
#    TOKEN    #
###############

load_dotenv(dotenv_path=join(dirname(abspath(__file__)), "config"))

#################
#    INTENTS    #
#################

# Intents (Required for connection)
intents = discord.Intents.default()
intents.message_content = True  # Needed to interact with messages
intents.polls = True  # Needed for polls

######################
#    AUTOCOMPLETE    #
######################

# WIP

#############
#    BOT    #
#############

class Bot(commands.Bot):
    
    def __init__(self):
        super().__init__(command_prefix="/", intents=intents)
        self.run(os.getenv("TOKEN"))
    
    async def on_ready(self):
        print("L3N-A is Ready!")

    async def setup_hook(self):
        await self.load_extension("cogs.test")
        await self.load_extension("cogs.planning")

# Bot Init
L3NA = Bot()