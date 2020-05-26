import os
from discord.ext import commands

client = commands.Bot(command_prefix="uno.")


@client.event
async def on_ready():
    channel = client.get_channel(711571536188014615)
    for filename in os.listdir('./cogs'):
        if filename.endswith('.py'):
            client.load_extension(f'cogs.{filename[:-3]}')
    await channel.send("I am ready.")


# @client.command()
# async def load(ctx, extension):
#     client.load_extension(f'cogs.{extension}')
#
#
# @client.command()
# async def unload(ctx, extension):
#     client.unload_extension(f'cogs.{extension}')


client.run('NzExMjg3MTMwMzc4MjA3MzYy.XsAz3Q.M47ow48xbMj8Zx87qqYqAfN1Was')

# await client.wait_until_ready()
# channel = client.get_channel(711571536188014615)
# for filename in os.listdir('./cogs'):
#     if filename.endswith('.py'):
#         client.load_extension('cogs.' + filename[:-3])
# await channel.send('I am ready.')
