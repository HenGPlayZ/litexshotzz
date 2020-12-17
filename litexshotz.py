import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.') 

@client.event
async def on_ready():
          await client.change_presence(status=discord.Status.online, activity=discord.Game("pornhub.com')) print('Bot Ready")

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith("%hello"):
        await message.channel.send("Hey there buddy!")
        
client.run(os.getenv('TOKEN'))

client.run('6bb71b4165493ed5a3344b3f3ec0312debfe709fcf88b34dfd276433ebdbe716')
