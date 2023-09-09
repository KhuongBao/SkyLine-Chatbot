from discord.ext import commands

from cogs.AI.chat import chatting

class ChatBot(commands.Cog):

    def __init__(self, client):
        self.client=client

    @commands.Cog.listener()
    async def on_message(self, message):
        message.content = message.content.lower()
        if message.author == self.client.user:
            return
        elif message.content!=None and message.content.startswith('!')==False:
            bot_output = chatting(message.content)
            await message.channel.send(bot_output)


def setup(client):
    client.add_cog(ChatBot(client))






















    # from Chatbot.ChatterBot import startbot
    # @commands.Cog.listener()
    # async def on_message(self, message):
    #     message.content=message.content.lower()
    #     if message.author==self.client.user:
    #         return
    #     if message.content.startswith('hello') or message.content.startswith('hi') or message.content.startswith('hey'):
    #         await message.channel.send('Hello '+str(message.author)+' !')

    # @commands.Cog.listener()
    # async def on_message(self, message):
    #     message.content=message.content.lower()
    #     if message.author!=self.client.user and message.content.startswith('!')==False:
    #         bot_output=startbot(message.content)
    #         if bot_output!=None:
    #             await message.channel.send(bot_output)