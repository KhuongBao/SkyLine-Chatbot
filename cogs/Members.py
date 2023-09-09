import discord
from discord.ext import commands

class Member(commands.Cog):

    def __init__(self, client):
        self.client=client


    @commands.Cog.listener()
    async def on_member_join(self, member):
        await member.send('Welcome!')
        print(f'{member} has joined')


    @commands.Cog.listener()
    async def on_member_remove(self, member):
        print(f'{member} has left')

def setup(client):
    client.add_cog(Member(client))