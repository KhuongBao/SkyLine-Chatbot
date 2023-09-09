import discord
from discord.ext import commands

class Test(commands.Cog):

    def __init__(self, client):
        self.client=client

    #Command
    @commands.command()
    async def ping(self, ctx):
        await ctx.send(f'Pong! {round(self.client.latency*1000)}ms')


def setup(client):
    client.add_cog(Test(client))
