import discord
import uno.glob
from uno.guildGame import GuildGame
from PIL import Image


class GameManager:
    def __init__(self, client):
        self.client = client
        self.hand_channel = client.get_channel(714679847418331146)
        self.guildGames = {}

    async def open_game(self, guild):
        if guild.id in self.guildGames:
            return
        category = await guild.create_category('UNO Game')
        channel = await category.create_text_channel('uno-game-info')
        self.guildGames[guild.id] = GuildGame(guild, category, channel, self.image_of_cards)
        await self.guildGames[guild.id].new_game()

    async def user_join(self, guild, user):
        member = guild.get_member(user.id)
        overwrites = {
            guild.default_role: uno.glob.no_perms,
            guild.me: uno.glob.yes_perms,
            member: uno.glob.yes_perms
        }
        category = self.guildGames[guild.id].category
        channel = await category.create_text_channel(f'{user.display_name}-hand', overwrites=overwrites)
        await self.guildGames[guild.id].user_join(user, channel)

    async def user_leave(self, guild, user):
        await self.guildGames[guild.id].user_leave(user)

    async def on_reaction_add(self, guild, reaction, user):
        if guild.id not in self.guildGames:
            return
        if reaction.emoji == uno.glob.join_emoji:
            if reaction.message.id == self.guildGames[guild.id].game_msg.id:
                await self.user_join(guild, user)
        elif reaction.emoji == uno.glob.kick_emoji:
            await self.guildGames[guild.id].kick_vote_add(user.id, reaction.message.id)
        else:
            await self.guildGames[guild.id].reaction_play(reaction, user)

    async def on_reaction_remove(self, guild, reaction, user):
        if guild.id not in self.guildGames:
            return
        if reaction.message.id == self.guildGames[guild.id].game_msg.id:
            if reaction.emoji == uno.glob.join_emoji:
                await self.guildGames[guild.id].user_leave(user)
            elif reaction.emoji == uno.glob.kick_emoji:
                self.guildGames[guild.id].kick_vote_remove(user.id)

    async def start_game(self, guild):
        if guild.id not in self.guildGames:
            return
        await self.guildGames[guild.id].start_game()

    async def play(self, guild, channel, user, letter, color='none'):
        if guild.id not in self.guildGames:
            return
        await self.guildGames[guild.id].play(channel.id, user.id, letter, color)

    async def draw(self, guild, channel, user):
        if guild.id not in self.guildGames:
            return
        await self.guildGames[guild.id].draw(channel.id, user.id)

    async def end_game(self, guild):
        if guild.id not in self.guildGames:
            return
        await self.guildGames[guild.id].end_game()

    async def close_game(self, guild):
        if guild.id not in self.guildGames:
            return
        await self.guildGames[guild.id].close_game()
        await self.guildGames[guild.id].channel.delete()
        await self.guildGames[guild.id].category.delete()
        del self.guildGames[guild.id]

    async def kick(self, guild):
        if guild.id not in self.guildGames:
            return
        await self.guildGames[guild.id].kick()

    async def user_exit(self, guild, user):
        if guild.id not in self.guildGames:
            return
        await self.guildGames[guild.id].user_exit(user)

    async def deactivate(self):
        for gg in self.guildGames.values():
            await self.close_game(gg.guild)

    async def image_of_cards(self, guild_id, cards, playable=None):
        columns = 8
        card_w = 80
        card_h = 120
        n = len(cards)
        if n == 0:
            return ''
        x = n
        y = 1
        if n > columns:
            x = columns
            y = int(n / columns) + 1
        img = Image.open(uno.glob.alpha_image_file)
        img = img.resize((card_w * x, card_h * y))
        for i in range(n):
            x = i
            y = 0
            if n > 8:
                x = i % columns
                y = int(i / columns)
            card_img = uno.glob.alpha_image_file
            if cards[i].number >= 50:
                card_img = uno.glob.wild_image_files[cards[i].number - 50]
            else:
                card_img = uno.glob.card_image_files[cards[i].suit][cards[i].number]
            img.paste(Image.open(card_img), (card_w * x, card_h * y))
            if playable:
                if cards[i].name in playable:
                    img.paste(Image.open(uno.glob.reaction_image_files[playable.index(cards[i].name) + 1]), (card_w * x + 45, card_h * y + 5))
        img.save(f'./img/{guild_id}.png')
        msg = await self.hand_channel.send(file=discord.File(f'./img/{guild_id}.png'))
        return msg.attachments[0].url
