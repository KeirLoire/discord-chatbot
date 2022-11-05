import discord
from classes.openai import Model 

class Client(discord.Client):
    def set_prefix(self, prefix = '$'):
        self.prefix = prefix

    async def on_ready(self):
        print(f'Logged on as {self.user}')
    
    async def on_message(self, message):
        if(not message.author.bot):
            if message.content.startswith('$'):
                async with message.channel.typing():
                    await message.channel.send(Model.submit_query(message.content))