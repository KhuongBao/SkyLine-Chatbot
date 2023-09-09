import discord
from discord.ext import commands
from discord.ext.commands import CommandNotFound
import os


TOKEN='NzcyMDczMjIyMTE5NzUxNzEw.X51XOA.azORnCyRsqoi9RnYF4M4I1aSo4w'

intents=discord.Intents.default()
intents.members=True

client=commands.Bot(command_prefix='!', intents=intents)


#Startup, Invalid command
@client.event
async def on_ready():
    print('Bot is online!')

@client.event
async def on_command_error(ctx, error):
    if isinstance(error, CommandNotFound):
        await ctx.send('Command not found!')

#Chat
@client.command()
async def chat(ctx):
    client.load_extension('cogs.Chat')
    await ctx.send('ChatBot initiallized!')

@client.command()
async def unchat(ctx):
    client.unload_extension('cogs.Chat')
    await ctx.send('ChatBot disabled!')


#Load, Unload, Reload
@client.command()
async def load(ctx, extention):
    client.load_extension(f'cogs.{extention}')
    await ctx.send(f'{extention} has been loaded')

@client.command()
async def unload(ctx, extention):
    client.unload_extension(f'cogs.{extention}')
    await ctx.send(f'{extention} has been unloaded')

@client.command()
async def reload(ctx, extention):
    client.unload_extension(f'cogs.{extention}')
    client.load_extension(f'cogs.{extention}')
    await ctx.send(f'{extention} has been reloaded')

for f in os.listdir('./cogs'):
    if f.endswith('.py') and f != 'Chat.py':
        client.load_extension(f'cogs.{f[:-3]}')


#Run Bot
if __name__=='__main__':
    client.run(TOKEN)