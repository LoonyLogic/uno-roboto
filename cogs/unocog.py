import time
import discord
from discord.ext import commands
import uno.glob
from uno.gameManager import GameManager


def is_me():
    def predicate(ctx):
        return ctx.message.author.id == 173405776713482240 and ctx.guild == 714677809666326619
    return commands.check(predicate)


class unoCog(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.manager = GameManager(client)
        self.active = True

    async def post_instructions(self, channel):
        d = [
            f'Click on the url to add the bot to your server.',
            'You must have the **Manage Server** permission in your server to do this.',
            'https://discord.com/api/oauth2/authorize?client_id=711287130378207362&permissions=8&scope=bot'
        ]
        embed = discord.Embed(
            title='STEP 1: Invite the Bot',
            description='\n'.join(d),
            color=uno.glob.colours[0]
        )
        embed.set_thumbnail(url=uno.glob.card_image_urls[0][1])
        await channel.send(embed=embed)
        time.sleep(1)

        d = [
            'Use the command `uno.open` to open up the game environment.',
            'This will create a new category called UNO GAME where the game will be played.'
        ]
        embed = discord.Embed(
            title='STEP 2: Open the Game',
            description='\n'.join(d),
            color=uno.glob.colours[1]
        )
        embed.set_thumbnail(url=uno.glob.card_image_urls[1][2])
        await channel.send(embed=embed)
        time.sleep(1)

        d = [
            'React with the ☑ emoji to join the game.',
            'This will create a private channel for you to view your cards.',
            'Wait for multiple players to do the same before moving on to the next step.'
        ]
        embed = discord.Embed(
            title='STEP 3: Join the Game',
            description='\n'.join(d),
            color=uno.glob.colours[2]
        )
        embed.set_thumbnail(url=uno.glob.card_image_urls[2][3])
        await channel.send(embed=embed)
        time.sleep(1)

        d = [
            'Use the command `uno.start` to start the game.',
            'New players will no longer be allowed to join until the current game has ended.'
        ]
        embed = discord.Embed(
            title='STEP 4: Start the Game',
            description='\n'.join(d),
            color=uno.glob.colours[3]
        )
        embed.set_thumbnail(url=uno.glob.card_image_urls[3][4])
        await channel.send(embed=embed)
        time.sleep(1)

        d = [
            f'This bot implements the rules of UNO posted.',
            'Pay attention to the message in your private channel to know when it is your turn.',
            'To play a card, react to the message according to the markings on your cards.',
            'To pass, react with 🅾 to draw a card'
        ]
        embed = discord.Embed(
            title='STEP 5: Play the Game',
            description='\n'.join(d),
            color=uno.glob.colours[0]
        )
        embed.set_thumbnail(url=uno.glob.card_image_urls[0][5])
        await channel.send(embed=embed)
        time.sleep(1)

        d = [
            'The game ends automatically once a player has played has played their last card.',
            f'If the game ends this way, the winner will be announced in `#game-info`',
            'However, you may use `uno.end` to end the game immediately at any time.'
        ]
        embed = discord.Embed(
            title='STEP 6: End the Game',
            description='\n'.join(d),
            color=uno.glob.colours[1]
        )
        embed.set_thumbnail(url=uno.glob.card_image_urls[1][6])
        await channel.send(embed=embed)
        time.sleep(1)

        d = [
            'The bot is designed to enter back into step 3 immediately when the game ends.',
            'The game is completely reset. Anyone who wants to play must rejoin to play in the next round.'
        ]
        embed = discord.Embed(
            title='STEP 7: Repeat Steps 3-6',
            description='\n'.join(d),
            color=uno.glob.colours[2]
        )
        embed.set_thumbnail(url=uno.glob.card_image_urls[2][7])
        await channel.send(embed=embed)
        time.sleep(1)

        d = [
            'You have the option to close the game by using the `uno.close` command',
            'This will delete the UNO GAME category and all channels within it.',
            'Redo step 2 to open it back up.'
        ]
        embed = discord.Embed(
            title='STEP 8: Close the Game',
            description='\n'.join(d),
            color=uno.glob.colours[3]
        )
        embed.set_thumbnail(url=uno.glob.card_image_urls[3][8])
        await channel.send(embed=embed)
        time.sleep(1)

        d = [
            'A player may choose to unjoin by removing the ☑ reaction before the game starts.',
            'A player may choose to leave in the middle of the game by using the `uno.leave` command.',
            'To initiate a vote to kick the player currently taking their turn, use the `uno.kick` command',
            'Players will be prompted to vote with 🦿 if they agree to kick the player',
            'If the majority of players do this, the player will be removed from the game'
        ]
        embed = discord.Embed(
            title='Unjoining, Leaving, and Kicking',
            description='\n'.join(d),
            color=uno.glob.colours[4]
        )
        embed.set_thumbnail(url=uno.glob.wild_image_urls[0])
        await channel.send(embed=embed)

    async def post_rules(self, channel):
        d = [
            'Before players join the game, the bot randomly shuffles the deck and places it into the draw pile.',
            'Upon joining the game, the bot will deal each player 7 cards randomly from the draw pile.',
            'These cards will be shown to the player through a private channel so only they can see it.',
            'When the game starts, the bot will move one card from the draw pile onto the top of the discard pile.',
            'All players can see the top card of the discard pile at all times.',
            'The bot will randomly determine the order of play at the start of the game.'
        ]
        embed = discord.Embed(
            title='SETUP',
            description=' '.join(d),
            color=uno.glob.colours[2]
        )
        embed.set_thumbnail(url=uno.glob.card_image_urls[2][7])
        await channel.send(embed=embed)
        time.sleep(1)

        d = [
            'On their turn, each player views their cards and tries to match the top card of the discard pile.',
            'They have to match either by the number, color, or the symbol/action.',
            'For instance, if the top card is the blue1, they have to place either a blue card or a card with a 1.',
            'They can also play a wild card (which can alter current color in play).',
            'Read the special rules about playing wild cards below.',
            'Take note that you may only play one card per turn.'
        ]
        embed = discord.Embed(
            title='PLAYING A CARD',
            description=' '.join(d),
            color=uno.glob.colours[3]
        )
        embed.set_thumbnail(url=uno.glob.card_image_urls[3][1])
        await channel.send(embed=embed)
        time.sleep(1)

        d = [
            'If they have no matches or choose not to play any of their cards (even though they might have a match),',
            'they must draw a card from the draw pile.',
            'If that card can be played, play it.',
            'Otherwise, keep the card, and the game moves on to the next person in turn.'
        ]
        embed = discord.Embed(
            title='DRAWING A CARD',
            description=' '.join(d),
            color=uno.glob.colours[0]
        )
        embed.set_thumbnail(url=uno.glob.card_image_urls[0][0])
        await channel.send(embed=embed)
        time.sleep(1)

        d = [
            'When a person places this card, the next player will have to pick up 2 cards and forfeit his/her turn.',
            'It can only be played on a card that matches by color, or on another draw2 card.',
            'If turned up at the beginning of play, the first player draws two cards and gets skipped.'
        ]
        embed = discord.Embed(
            title='THE DRAW2 CARD',
            description=' '.join(d),
            color=uno.glob.colours[1]
        )
        embed.set_thumbnail(url=uno.glob.card_image_urls[1][10])
        await channel.send(embed=embed)
        time.sleep(1)

        d = [
            'When a person places this card, the order of play will be reversed immediately.',
            'It can only be played on a card that matches by color, or on another reverse card.',
            'If turned up at the beginning of play, the last player gets to play first and order of play is reversed.'
        ]
        embed = discord.Embed(
            title='THE REVERSE CARD',
            description=' '.join(d),
            color=uno.glob.colours[2]
        )
        embed.set_thumbnail(url=uno.glob.card_image_urls[2][11])
        await channel.send(embed=embed)
        time.sleep(1)

        d = [
            'When a person places this card, the next player has to skip their turn.',
            'It can only be played on a card that matches by color, or on another skip card.',
            'If turned up at the beginning of play, the first player has to skip their turn.'
        ]
        embed = discord.Embed(
            title='THE SKIP CARD',
            description=' '.join(d),
            color=uno.glob.colours[3]
        )
        embed.set_thumbnail(url=uno.glob.card_image_urls[3][12])
        await channel.send(embed=embed)
        time.sleep(1)

        d = [
            'The wild card represents all four colors, and can be placed on any card.',
            'The player has to state which color it will represent for the next player.',
            'It can be played regardless of whether another card is available.',
            'If turned up at the beginning of play, the first player chooses what color to continue play.'
        ]
        embed = discord.Embed(
            title='THE WILD CARD',
            description=' '.join(d),
            color=uno.glob.colours[4]
        )
        embed.set_thumbnail(url=uno.glob.wild_image_urls[0])
        await channel.send(embed=embed)
        time.sleep(1)

        d = [
            'This card acts just like the wild card except that the next player also has to draw 4 cards as well as skip their turn.',
            'With this card, you must have no other cards to play that matches the **color** of the top card.',
            'Note, this card may be played even if the player can match the **number/symbol/action** of the top card.',
            'If turned up at the beginning of play, it will be returned randomly into the draw pile, and replaced by a new card.',
        ]
        embed = discord.Embed(
            title='THE WILD_DRAW4 CARD',
            description=' '.join(d),
            color=uno.glob.colours[4]
        )
        embed.set_thumbnail(url=uno.glob.wild_image_urls[1])
        await channel.send(embed=embed)

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if user.id == self.client.user.id:
            return
        await self.manager.on_reaction_add(reaction.message.guild, reaction, user)

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        if user.id == self.client.user.id:
            return
        await self.manager.on_reaction_remove(reaction.message.guild, reaction, user)

    @commands.command()
    async def open(self, ctx):
        if not self.active:
            return
        await self.manager.open_game(ctx.guild)
        await ctx.message.delete(delay=2)

    @commands.command()
    async def start(self, ctx):
        if not self.active:
            return
        await self.manager.start_game(ctx.guild)
        await ctx.message.delete(delay=2)

    @commands.command()
    async def play(self, ctx, letter, color='none'):
        if not self.active:
            return
        await self.manager.play(ctx.guild, ctx.channel, ctx.author, letter, color)
        await ctx.message.delete(delay=2)

    @commands.command()
    async def draw(self, ctx):
        if not self.active:
            return
        await self.manager.draw(ctx.guild, ctx.channel, ctx.author)
        await ctx.message.delete(delay=2)

    @commands.command()
    async def end(self, ctx):
        if not self.active:
            return
        await self.manager.end_game(ctx.guild)
        await ctx.message.delete(delay=2)

    @commands.command()
    async def close(self, ctx):
        if not self.active:
            return
        await self.manager.close_game(ctx.guild)
        await ctx.message.delete(delay=2)

    @commands.command()
    async def kick(self, ctx):
        if not self.active:
            return
        await self.manager.kick(ctx.guild)
        await ctx.message.delete(delay=2)

    @commands.command()
    async def exit(self, ctx):
        if not self.active:
            return
        await self.manager.user_exit(ctx.guild, ctx.author)
        await ctx.message.delete(delay=2)

    @commands.command()
    async def support(self, ctx):
        if ctx.author.dm_channel:
            await ctx.author.dm_channel.send(uno.glob.support)
        else:
            await (await ctx.author.create_dm()).send(uno.glob.support)

    @commands.command()
    async def invite(self, ctx):
        if ctx.author.dm_channel:
            await ctx.author.dm_channel.send(uno.glob.invite)
        else:
            await (await ctx.author.create_dm()).send(uno.glob.invite)

    @commands.command()
    @is_me()
    async def instructions(self, ctx):
        await self.post_instructions(ctx.channel)

    @commands.command()
    @is_me()
    async def rules(self, ctx):
        await self.post_rules(ctx.channel)

    @commands.command()
    @is_me()
    async def shutdown(self, ctx):
        if self.active:
            await self.deactivate(ctx)
        await self.client.close()

    @commands.command()
    @is_me()
    async def activate(self, ctx):
        self.active = True

    @commands.command()
    @is_me()
    async def deactivate(self, ctx):
        self.active = False
        await self.manager.deactivate()


def setup(client):
    client.add_cog(unoCog(client))
