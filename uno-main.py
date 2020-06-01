import os
from discord.ext import commands

client = commands.Bot(command_prefix="uno.")


@client.event
async def on_ready():
    channel = client.get_channel(714679921112383498)
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')
    await channel.send("I am ready.")


f = open('Token.txt', 'r')
client.run(f.read())
f.close()
