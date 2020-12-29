import configparser
import discord
import openai

# Parse Configuration
config = configparser.ConfigParser()
config.read('config.ini')
prefix = config['Discord']['prefix']

class Client(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}')
    
    async def on_message(self, message):
        if(not message.author.bot):
            if(str(message.channel.id) == config['OpenAI']['channel_id']):
                response = openai.Completion.create(
                    engine='davinci',
                    prompt=f'User: {message.content}\nBot: ',
                    temperature=0.9,
                    max_tokens=150,
                    top_p=1,
                    presence_penalty=0.6,
                    stop=['\n', ' User:', ' Bot:'])

                async with message.channel.typing():
                    if(response['choices'][0]['text']):
                        await message.channel.send(response['choices'][0]['text'])
                    else:
                        await message.channel.send('No response from OpenAI server.')

openai.api_key = config['OpenAI']['token']
client = Client()
client.run(config['Discord']['token'])