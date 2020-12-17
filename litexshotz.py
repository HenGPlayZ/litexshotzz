import discord
from discord.ext import commands

client = commands.Bot(command_prefix = '.') 

@client.event
async def on_ready():
    await client.change_presence(status=discord.status.idle, activity=discord.Game ('litexshot.org'))
    print('Bot is ready.')

client.run('Nzg5MDI5OTAwMzQ1NTQwNjQ5.X9sHWw.UC8MOxZtIIfzWITnLBvqN9hZFgA')
bot.run('token')
