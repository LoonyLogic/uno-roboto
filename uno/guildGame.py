import time
import random
import discord
import uno.glob
from uno.game import Game
from uno.guildPlayer import GuildPlayer


class GuildGame:
    def __init__(self, guild, category, channel, imager):
        self.guild = guild
        self.category = category
        self.channel = channel
        self.imager = imager
        self.game = Game()
        self.game_embed = None
        self.game_msg = None
        self.game_stage = 'join'
        self.pid = []
        self.user_players = {}
        self.up_prev = None
        self.up_now = None
        self.up_next = None
        self.clockwise_order = []
        self.counterclockwise_order = []
        self.action_note = 'None'
        self.wild_card = None
        self.wild_msg = None
        self.kick_votes = []
        self.time_stamp = time.time()

    async def new_game(self):
        self.game.new_game()
        self.game_stage = 'join'
        self.pid = []
        self.user_players = {}
        self.game_embed = discord.Embed(
            title='Starting a new game soon.',
            description=f'{uno.glob.join_emoji}React to join. Remove your reaction to leave.',
            color=uno.glob.white
        )
        self.game_msg = await self.channel.send(embed=self.game_embed)
        await self.game_msg.add_reaction(uno.glob.join_emoji)

    async def user_join(self, user, channel):
        if self.game_stage != 'join':
            return
        if user.id in self.pid:
            return
        embed = discord.Embed(
            title='YOUR HAND',
            description='Waiting for the game to begin...',
            color=uno.glob.gray
        )
        embed.add_field(name='PLAYING NOW', value='NA')
        embed.add_field(name='PLAYING NEXT', value='NA')
        embed.add_field(name='RECENT ACTION', value='You joined the game', inline=False)
        msg = channel.send(embed)
        self.pid.append(user.id)
        self.user_players[user.id] = GuildPlayer(user, channel, msg, embed)
        await self.update_join_msg()

    async def user_leave(self, user):
        if self.game_stage != 'join':
            return
        if user[id] in self.pid:
            await self.user_players[user.id].channel.delete()
            self.pid.remove(user.id)
            del self.user_players[user.id]
        await self.update_join_msg()

    async def update_join_msg(self):
        if self.game_stage != 'join':
            return
        if len(self.pid) < 2:
            self.game_embed.description = f'{uno.glob.join_emoji}React to join. Remove your reaction to leave.'
        elif len(self.pid) == 10:
            self.game_embed.description = f'GAME IS FULL. Remove your {uno.glob.join_emoji}reaction to leave. Say `uno.start` to start the game.'
        else:
            self.game_embed.description = f'{uno.glob.join_emoji}React to join. Remove your reaction to leave. Say `uno.start` to start the game.'
        self.game_embed.clear_fields()
        i = 1
        for up in self.user_players.values():
            self.game_embed.add_field(name=uno.glob.reaction_emojis[i], value=up.name)
            i += 1
        await self.game_msg.edit(embed=self.game_embed)

    async def start_game(self):
        if self.game_stage != 'join':
            return
        number = len(self.pid)
        if number < 2 or number > 10:
            return
        self.game_stage = 'play'
        await self.game_msg.clear_reactions()

        self.set_action_note(self.game.start_game(number))
        random.shuffle(self.pid)
        self.clockwise_order = []
        self.counterclockwise_order = []
        for i in range(number):
            player = self.user_players[self.pid[i]]
            player.set_player(self.game.players[i])
            self.clockwise_order.append(player.name)
            self.counterclockwise_order.insert(0, player.name)
        for p in self.user_players.values():
            p.embed.set_footer(text=' -> '.join(self.clockwise_order))
        self.next()

        self.game_embed.title = ''
        self.game_embed.description = ''
        self.game_embed.clear_fields()
        self.game_embed.add_field(name='PLAYING NOW', value=self.up_now.name)
        self.game_embed.add_field(name='PLAYING NEXT', value=self.up_next.name)
        self.game_embed.add_field(name='RECENT ACTION', value=self.action_note, inline=False)
        await self.update_all_players()

    def set_action_note(self, action):
        note = ''
        if action.act_flags.has_actor:
            note += self.user_players[self.pid[action.actor]].name
            if action.act_flags.is_draw:
                note += ' drew a card'
                if action.act_flags.is_play:
                    note += ', and'
            if action.act_flags.has_target:
                target = self.user_players[self.pid[action.target]].name
                if action.act_flags.is_draw2:
                    note += f' compels {target} to draw 2 cards'
                elif action.act_flags.is_skip:
                    note += f' skips {target}\'s turn'
                elif action.act_flags.is_draw4:
                    note += f' compels {target} to draw 4 cards'
                    if action.has_color:
                        note += f', and chooses {action.color}'
                elif action.act_flags.is_play:
                    note += f' played a {action.card}'
                    if action.has_color:
                        note += f', and chooses {action.color}'
            if action.act_flags.is_reverse:
                note += ' reverses the order of play'
            if action.act_flags.is_kick:
                note += ' was removed from the game'
            if action.act_flags.is_end:
                note += ' won this game'
        elif action.act_flags.is_end:
            note += 'This game has ended. No one won'
        note += '.'
        self.action_note = note

    async def update_all_players(self):
        top = self.game.discard_pile[0]
        top_url = ''
        if top.number >= 50:
            top_url = uno.glob.wild_image_urls[top.number - 50]
        else:
            top_url = uno.glob.card_image_urls[top.suit][top.number]
        self.game_embed.colour = uno.glob.colours[top.suit]
        self.game_embed.set_image(url=top_url)
        self.game_embed.set_author(name=self.up_now.name, icon_url=self.up_now.url)
        self.game_embed.set_field_at(0, name='PLAYING NOW', value=self.up_now.name)
        self.game_embed.set_field_at(1, name='PLAYING NEXT', value=self.up_next.name)
        self.game_embed.set_field_at(2, name='RECENT ACTION', value=self.action_note, inline=False)
        await self.game_msg.edit(embed=self.game_embed)

        for up in self.user_players.values():
            up.embed.colour = uno.glob.colours[top.suit]
            up.embed.set_thumbnail(url=top_url)
            up.embed.set_field_at(0, name='PLAYING NOW', value=self.up_now.name)
            up.embed.set_field_at(1, name='PLAYING NEXT', value=self.up_next.name)
            up.embed.set_field_at(2, name='RECENT ACTION', value=self.action_note, inline=False)
            await up.msg.edit(embed=up.embed)

        if self.up_prev:
            self.up_prev.embed.description += f' {self.up_now.name} is playing now.'
            if len(self.up_prev.player.cards) > 0:
                img_url = await self.imager(self.guild.id, self.up_prev.cards)
                self.up_prev.embed.set_image(url=img_url)
                self.up_prev.embed.set_thumbnail(url=top_url)
            await self.up_prev.msg.edit(embed=self.up_prev.embed)

        self.up_next.embed.description = f'{self.up_now.name} is playing now. Your turn to play next.'
        await self.up_next.msg.edit(embed=self.up_next.embed)

        for up in self.user_players.values():
            if up == self.up_now or up == self.up_next or up == self.up_prev:
                continue
            else:
                up.embed.description = f'{self.up_now.name} is playing now.'
                await up.msg.edit(embed=up.embed)

        self.up_now.embed.description = 'It is now your turn to play.'
        self.up_now.embed.colour = uno.glob.colours[top.suit]
        self.up_now.embed.set_thumbnail(url=top_url)
        img_url = await self.imager(self.guild.id, self.up_now.player.cards, True)
        self.up_now.embed.set_image(url=img_url)
        await self.up_now.msg.edit(embed=self.up_now.embed)
        self.time_stamp = time.time()
        for i in range(len(self.game.playable_cards) + 1):
            await self.up_now.msg.add_reaction(uno.glob.reaction_emojis[i])

    async def reaction_play(self, reaction, user):
        if self.up_now:
            if reaction.message.channel.id == self.up_now.channel.id:
                if self.user_players[user.id] == self.up_now:
                    if self.game_stage == 'kick':
                        await self.cancel_kick()
                    await self.now_reaction(reaction)

    async def now_reaction(self, reaction):
        if reaction.emoji in uno.glob.color_emojis:
            await self.wild_msg.delete()
            suit = uno.glob.color_emojis.index(reaction.emoji)
            self.set_action_note(await self.game.play(self.wild_card, suit))
        elif reaction.emoji == uno.glob.draw_emoji:
            await self.up_now.msg.clear_reactions()
            self.set_action_note(await self.game.draw())
        elif reaction.emoji in uno.glob.reaction_emojis:
            i = uno.glob.reaction_emojis.index(reaction.emoji)
            if i >= len(self.game.playable_cards):
                return
            await self.up_now.msg.clear_reactions()
            c = self.game.playable_cards[i]
            if c.number == 50 or c.number == 51:
                self.wild_card = i
                uno.glob.wild_embed.set_footer(text=c.name)
                self.wild_msg = await self.up_now.channel.send(embed=uno.glob.wild_embed)
                for e in uno.glob.color_emojis:
                    await self.wild_msg.add_reaction(e)
            else:
                self.set_action_note(await self.game.play(i))

    async def play(self, channel_id, user_id, letter, color='none'):
        if not self.up_now:
            return
        if channel_id != self.up_now.channel.id:
            return
        if user_id != self.up_now.user.id:
            return
        i = uno.glob.letters.index(letter)
        if i >= len(self.game.playable_cards):
            return
        card = self .game.playable_cards[i]
        suit = -1
        if card.number == 50 or card.number == 51:
            if color == 'r' or color == 'red':
                suit = 0
            elif color == 'y' or color == 'yellow':
                suit = 1
            elif color == 'g' or color == 'green':
                suit = 2
            elif color == 'b' or color == 'blue':
                suit = 3
            else:
                return
        await self.up_now.msg.clear_reactions()
        self.set_action_note(await self.game.play(i, suit))
        self.next()
        await self.update_all_players()

    async def draw(self, channel_id, user_id):
        if not self.up_now:
            return
        if channel_id != self.up_now.channel.id:
            return
        if user_id != self.up_now.user.id:
            return
        await self.up_now.msg.clear_reactions()
        self.set_action_note(await self.game.draw())
        self.next()
        await self.update_all_players()

    def next(self):
        for up in self.user_players.values():
            if self.game.order == 1:
                up.embed.set_footer(text=' -> '.join(self.clockwise_order))
            else:
                up.embed.set_footer(text=' -> '.join(self.counterclockwise_order))
        for up in self.user_players.values():
            if self.game.p_prev == up.player:
                self.up_prev = up
            if self.game.p_now == up.player:
                self.up_now = up
            if self.game.p_next == up.player:
                self.up_next = up

    async def now_win(self):
        for up in self.user_players.values():
            embed = discord.Embed(
                title=f'{self.up_now.name} won this game!',
                description=f'This channel will be deleted very soon. Go to {self.channel.mention} to join the next game.',
                color=uno.glob.purple
            )
            await up.channel.send(embed=embed)
        time.sleep(5.0)
        self.game_stage = 'join'
        for up in self.user_players.values():
            await up.channel.delete()
        self.user_players = {}
        self.game_embed = discord.Embed(
            title=f'{self.up_now.name} won! Starting a new game soon.',
            description=f'{uno.glob.join_emoji}React to join. Remove your reaction to leave.',
            color=uno.glob.white
        )
        await self.game_msg.edit(embed=self.game_embed)
        await self.game_msg.clear_reactions()
        await self.game_msg.add_reaction(uno.glob.join_emoji)

    async def end_game(self):
        self.game_stage = 'join'
        for up in self.user_players.values():
            await up.channel.delete()
        self.user_players = {}
        self.game_embed = discord.Embed(
            title='The game ended. Starting a new game soon.',
            description=f'{uno.glob.join_emoji}React to join. Remove your reaction to leave.',
            color=uno.glob.white
        )
        await self.game_msg.edit(embed=self.game_embed)
        await self.game_msg.clear_reactions()
        await self.game_msg.add_reaction(uno.glob.join_emoji)

    async def close_game(self):
        for up in self.user_players.values():
            await up.channel.delete()

    async def kick(self, channel):
        if self.game_stage != 'play':
            return
        elapsed = time.time() - self.time_stamp
        if elapsed > uno.glob.timeout:
            self.game_stage = 'kick'
            for up in self.user_players.values():
                if up == self.up_now:
                    continue
                embed = discord.Embed(
                    title=f'Is {self.up_now.user.display_name} taking too long to play?',
                    description=f'{uno.glob.kick_emoji}React to kick them from the game.',
                    color=uno.glob.purple
                )
                up.kick_msg = await up.channel.send(embed=embed)
                await up.kick_msg.add_reaction(uno.glob.kick_emoji)
        else:
            embed = discord.Embed(
                title='Be patient',
                description=f'You cannot kick a player unless they are taking longer than {str(uno.glob.timeout)} seconds to play.',
                color=uno.glob.purple
            )
            embed.add_field(name='elapsed time', value=f'{str(elapsed)} seconds')
            msg = await channel.send(embed=embed)
            await msg.delete(delay=2)

    async def cancel_kick(self):
        if self.game_stage != 'kick':
            return
        self.game_stage = 'play'
        self.kick_votes = []
        for up in self.user_players.values():
            if up == self.up_now:
                continue
            embed = discord.Embed(
                title=f'{self.up_now.user.display_name} is now playing.',
                description='This vote has been canceled',
                color=uno.glob.purple
            )
            await up.kick_msg.clear_reactions()
            await up.kick_msg.edit(embed=embed)
            await up.kick_msg.delete(delay=2)

    async def kick_vote_add(self, user_id, message_id):
        if self.game_stage != 'kick':
            return
        if self.user_players[user_id].player == self.game.p_now:
            return
        if user_id not in self.pid:
            return
        if message_id != self.user_players[user_id].kick_msg.id:
            return
        if user_id not in self.kick_votes:
            self.kick_votes.append(user_id)
            print(f'{str(len(self.kick_votes))} votes')
            if len(self.kick_votes) > (len(self.pid) - 1) / 2:
                await self.kick_now()

    def kick_vote_remove(self, user):
        if self.game_stage != 'kick':
            return
        if user.id in self.kick_votes:
            self.kick_votes.remove(user.id)

    async def kick_now(self):
        if self.game_stage != 'kick':
            return
        self.game_stage = 'play'
        self.action_note = f'{self.up_now.user.display_name} was kicked from the game.'
        for up in self.user_players.values():
            if not up.kick_msg:
                continue
            embed = discord.Embed(
                title='Majority rules!',
                description=f'{self.up_now.user.display_name} has been removed from the game.',
                color=uno.glob.purple
            )
            await up.kick_msg.clear_reactions()
            await up.kick_msg.edit(embed=embed)
            await up.kick_msg.delete(delay=2)
            up.kick_msg = None
        self.set_action_note(self.game.kick_now())
        await self.up_now.channel.delete()
        del self.user_players[self.up_now.id]
        self.clockwise_order = []
        self.counterclockwise_order = []
        for up in self.user_players.values():
            self.clockwise_order.append(up.user.display_name)
            self.counterclockwise_order.insert(0, up.user.display_name)
        self.next()
        await self.update_all_players()

    async def user_exit(self, user):
        if self.game_stage != 'play':
            return
        player = self.user_players[user.id]
        for up in self.user_players.values():
            embed = discord.Embed(
                title='PLAYER LEFT',
                description=f'{user.display_name} has been removed from the game.',
                color=uno.glob.purple
            )
            msg = await up.channel.send(embed=embed)
            await msg.delete(delay=2)
        self.set_action_note(self.game.remove_player(player.player))
        await player.channel.delete()
        del self.user_players[player.id]
        self.clockwise_order = []
        self.counterclockwise_order = []
        for up in self.user_players.values():
            self.clockwise_order.append(up.user.display_name)
            self.counterclockwise_order.insert(0, up.user.display_name)
        self.next()
        await self.update_all_players()
