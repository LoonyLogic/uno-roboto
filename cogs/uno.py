import random
import discord
from PIL import Image
from discord.ext import commands

card_image_urls = [
    [
        'https://cdn.discordapp.com/attachments/711726162786910268/712563836728770560/r0.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712563837475356682/r1.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712563838435721256/r2.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712563839140495400/r3.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712563839769772132/r4.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712563858711117844/r5.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712563859952762910/r6.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712563860988755988/r7.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712563862255173802/r8.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712563865795166248/r9.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712563883373494322/rd.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712563884258754590/rr.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712563885235765268/rs.png'
    ],
    [
        'https://cdn.discordapp.com/attachments/711726162786910268/712563886024294430/y0.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712563886867349554/y1.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712563905544847380/y2.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712563906337308692/y3.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712563907050340422/y4.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712563907935600679/y5.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712563908858085416/y6.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712563927200038942/y7.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712563928030249010/y8.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712563929217499177/y9.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712563931314388992/yd.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712563932010774568/yr.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712563950327169075/ys.png'
    ],
    [
        'https://cdn.discordapp.com/attachments/711726162786910268/712563950960771112/g0.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712563951715614720/g1.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712563952524984351/g2.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712563953200267284/g3.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712563971957456936/g4.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712563972787666995/g5.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712563975027425350/g6.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712563975841382440/g7.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712563976730574848/g8.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712563993553666068/g9.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712563994216366090/gd.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712563995416199178/gr.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712563996473032734/gs.png'
    ],
    [
        'https://cdn.discordapp.com/attachments/711726162786910268/712563997102309376/b0.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712564015259320370/b1.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712564016249176085/b2.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712564017121722408/b3.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712564018090344480/b4.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712564018744655892/b5.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712564036922900530/b6.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712564037887721502/b7.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712564038541770782/b8.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712564039204601866/b9.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712564039984742411/bd.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712564059098054686/br.png',
        'https://cdn.discordapp.com/attachments/711726162786910268/712564059907817491/bs.png'
    ]
]

card_image_files = [
    [
        './unocards/r0.png',
        './unocards/r1.png',
        './unocards/r2.png',
        './unocards/r3.png',
        './unocards/r4.png',
        './unocards/r5.png',
        './unocards/r6.png',
        './unocards/r7.png',
        './unocards/r8.png',
        './unocards/r9.png',
        './unocards/rd.png',
        './unocards/rr.png',
        './unocards/rs.png'
    ],
    [
        './unocards/y0.png',
        './unocards/y1.png',
        './unocards/y2.png',
        './unocards/y3.png',
        './unocards/y4.png',
        './unocards/y5.png',
        './unocards/y6.png',
        './unocards/y7.png',
        './unocards/y8.png',
        './unocards/y9.png',
        './unocards/yd.png',
        './unocards/yr.png',
        './unocards/ys.png'
    ],
    [
        './unocards/g0.png',
        './unocards/g1.png',
        './unocards/g2.png',
        './unocards/g3.png',
        './unocards/g4.png',
        './unocards/g5.png',
        './unocards/g6.png',
        './unocards/g7.png',
        './unocards/g8.png',
        './unocards/g9.png',
        './unocards/gd.png',
        './unocards/gr.png',
        './unocards/gs.png'
    ],
    [
        './unocards/b0.png',
        './unocards/b1.png',
        './unocards/b2.png',
        './unocards/b3.png',
        './unocards/b4.png',
        './unocards/b5.png',
        './unocards/b6.png',
        './unocards/b7.png',
        './unocards/b8.png',
        './unocards/b9.png',
        './unocards/bd.png',
        './unocards/br.png',
        './unocards/bs.png'
    ]
]

wild_image_urls = [
    'https://cdn.discordapp.com/attachments/711726162786910268/712564060817981490/z.png',
    'https://cdn.discordapp.com/attachments/711726162786910268/712564061430218822/zd.png'
]

wild_image_files = [
    './unocards/z.png',
    './unocards/zd.png'
]

reaction_image_files = [
    './unocards/o2.png',
    './unocards/qa.png',
    './unocards/qb.png',
    './unocards/qc.png',
    './unocards/qd.png',
    './unocards/qe.png',
    './unocards/qf.png',
    './unocards/qg.png',
    './unocards/qh.png',
    './unocards/qi.png',
    './unocards/qj.png',
    './unocards/qk.png',
    './unocards/ql.png',
    './unocards/qm.png',
    './unocards/qn.png',
    './unocards/qp.png',
    './unocards/qq.png',
    './unocards/qr.png'
]

reaction_emojis = [
        '🅾', '🇦', '🇧', '🇨', '🇩', '🇪',
        '🇫', '🇬', '🇭', '🇮', '🇯', '🇰',
        '🇱', '🇲', '🇳', '🇵', '🇶', '🇷',
]

color_emojis = [
        '🔴', '🟡', '🟢', '🔵'
]

colours = [
    discord.colour.Color.from_rgb(200, 50, 50),
    discord.colour.Color.from_rgb(200, 200, 50),
    discord.colour.Color.from_rgb(50, 200, 50),
    discord.colour.Color.from_rgb(50, 50, 200),
    discord.colour.Color.from_rgb(200, 200, 200),
    discord.colour.Color.from_rgb(0, 0, 0)
]

wild_embed = discord.Embed(
    title='Choose a color!',
    description='🔴red, 🟡yellow, 🟢green, or 🔵blue',
    color=colours[5]
)


class Player:
    def __init__(self, user, cards, channel, embed, msg):
        self.user = user
        self.cards = cards
        self.channel = channel
        self.embed = embed
        self.msg = msg
        self.kick_msg = None


class Card:
    def __init__(self, suit, number, url, img):
        self.number = number
        self.suit = suit
        self.url = url
        self.img = img
        self.reaction = 0
        self.name = ''

        if self.suit == 0:
            self.name = 'red'
        elif self.suit == 1:
            self.name = 'yellow'
        elif self.suit == 2:
            self.name = 'green'
        elif self.suit == 3:
            self.name = 'blue'
        elif self.suit == 4:
            self.name = 'wild'

        if self.number == 10:
            self.name += '_draw2'
        elif self.number == 11:
            self.name += '_reverse'
        elif self.number == 12:
            self.name += '_skip'
        elif self.number == 50:
            self.name += ''
        elif self.number == 51:
            self.name += '_draw4'
        else:
            self.name += str(self.number)


class Game:
    def __init__(self, guild, hand_channel):
        self.guild = guild
        self.hand_channel = hand_channel
        self.category = None
        self.game_channel = None
        self.game_stage = 0
        self.turn = 0
        self.order = 1
        self.game_embed = None
        self.game_msg = None
        self.players = []
        self.draw_pile = []
        self.discard_pile = []
        self.clockwise_order = []
        self.counterclockwise_order = []
        self.wild_card = None
        self.wild_msg = None
        self.p_now = None
        self.p_next = None
        self.p_prev = None
        self.action_note = ''
        self.kick_votes = []

    async def new_game(self):
        self.players = []
        self.new_deck()
        self.category = await self.guild.create_category('UNO Game')
        self.game_channel = await self.category.create_text_channel('game-info')
        self.game_embed = discord.Embed(
            title='Starting a new game soon.',
            description='☑React to join. Remove your reaction to leave.',
            color=colours[4]
        )
        self.game_msg = await self.game_channel.send(embed=self.game_embed)
        await self.game_msg.add_reaction('☑')
        self.game_stage = 'join'

    def new_deck(self):
        self.draw_pile = []
        self.discard_pile = []
        for s in range(4):
            for n in range(13):
                if n == 0:
                    self.draw_pile.append(Card(s, n, card_image_urls[s][n], card_image_files[s][n]))
                else:
                    self.draw_pile.append(Card(s, n, card_image_urls[s][n], card_image_files[s][n]))
                    self.draw_pile.append(Card(s, n, card_image_urls[s][n], card_image_files[s][n]))
        for i in range(4):
            self.draw_pile.append(Card(4, 50, wild_image_urls[0], wild_image_files[0]))
            self.draw_pile.append(Card(4, 51, wild_image_urls[1], wild_image_files[1]))
        random.shuffle(self.draw_pile)

    async def user_join(self, user):
        if self.game_stage != 'join':
            return
        for p in self.players:
            if p.user.id == user.id:
                return
        cards = self.pick_from_draw_pile(7)
        img_url = await self.image_of_cards(cards)
        member = self.guild.get_member(user.id)
        overwrites = {
            self.guild.default_role: discord.PermissionOverwrite(read_messages=False, send_messages=False, add_reactions=False),
            self.guild.me: discord.PermissionOverwrite(read_messages=True, send_messages=True, add_reactions=True),
            member: discord.PermissionOverwrite(read_messages=True, send_messages=True, add_reactions=True)
        }
        channel = await self.category.create_text_channel(user.display_name + '-hand', overwrites=overwrites)
        embed = discord.Embed(
            title='YOUR HAND',
            description='Waiting for the game to begin...',
            color=colours[5]
        )
        embed.set_image(url=img_url)
        embed.add_field(name='PLAYING NOW', value='NA')
        embed.add_field(name='PLAYING NEXT', value='NA')
        embed.add_field(name='RECENT ACTION', value='You joined the game', inline=False)
        msg = await channel.send(embed=embed)
        self.players.append(Player(user, cards, channel, embed, msg))
        self.game_embed.clear_fields()
        for i in range(len(self.players)):
            self.game_embed.add_field(name=reaction_emojis[i + 1], value=self.players[i].user.display_name)
        await self.game_msg.edit(embed=self.game_embed)

    async def user_leave(self, user):
        if self.game_stage == 'join':
            for p in self.players:
                if p.user.id == user.id:
                    while len(p.cards) > 0:
                        self.draw_pile.insert(random.randint(0, len(p.cards)), p.cards.pop(0))
                    await p.channel.delete()
                    self.players.remove(p)
                    break
            self.game_embed.clear_fields()
            for i in range(len(self.players)):
                self.game_embed.add_field(name=reaction_emojis[i + 1], value=self.players[i].user.display_name)
            await self.game_msg.edit(embed=self.game_embed)
        elif self.game_stage == 'play':
            await self.kick_user(user)

    def pick_from_draw_pile(self, number):
        cards = []
        for i in range(number):
            if len(self.draw_pile) == 0:
                top = self.discard_pile.pop(0)
                self.draw_pile.extend(self.discard_pile)
                self.discard_pile.append(top)
                random.shuffle(self.draw_pile)
            cards.append(self.draw_pile.pop(0))
        return cards

    async def image_of_cards(self, cards, playable=False):
        columns = 8
        card_w = 80
        card_h = 120
        n = len(cards)
        x = n
        y = 1
        if n > columns:
            x = columns
            y = int(n / columns) + 1
        img = Image.open('./unocards/alpha.png')
        img = img.resize((card_w * x, card_h * y))
        for i in range(n):
            x = i
            y = 0
            if n > 8:
                x = i % columns
                y = int(i / columns)
            img.paste(Image.open(cards[i].img), (card_w * x, card_h * y))
            if playable:
                if cards[i].reaction > 0:
                    img.paste(Image.open(reaction_image_files[cards[i].reaction]), (card_w * x + 45, card_h * y + 5))
        img.save('i.png')
        msg = await self.hand_channel.send(file=discord.File('i.png'))
        return msg.attachments[0].url

    async def on_reaction_add(self, reaction, user):
        if reaction.emoji == '☑':
            if reaction.message.id == self.game_msg.id:
                await self.user_join(user)
        elif reaction.emoji == '🦿':
            if self.p_now:
                if user.id == self.p_now.user.id:
                    return
            for p in self.players:
                if user.id == p.user.id:
                    if reaction.message.id == p.kick_msg.id:
                        print('kick vote add')
                        await self.kick_vote_add(user)
                    break
        elif self.p_now:
            if reaction.message.channel.id == self.p_now.channel.id:
                if user.id == self.p_now.user.id:
                    if self.game_stage == 'kick':
                        await self.cancel_kick()
                    await self.now_reaction(reaction)

    async def on_reaction_remove(self, reaction, user):
        if reaction.message.id == self.game_msg.id:
            if reaction.emoji == '☑':
                await self.user_leave(user)
            elif reaction.emoji == '🦿':
                self.kick_vote_remove(user)

    async def start_game(self):
        if self.game_stage != 'join':
            return
        self.game_stage = 'play'

        await self.game_msg.clear_reactions()

        random.shuffle(self.players)
        self.clockwise_order = []
        self.counterclockwise_order = []
        for p in self.players:
            self.clockwise_order.append(p.user.display_name)
            self.counterclockwise_order.insert(0, p.user.display_name)
        for p in self.players:
            p.embed.set_footer(text=' -> '.join(self.clockwise_order))
        self.turn = 0

        self.action_note = 'None'
        self.discard_pile.insert(0, self.draw_pile.pop(0))
        while self.discard_pile[0].number == 51:
            r = random.randint(1, len(self.draw_pile) + 1)
            self.draw_pile.insert(r, self.discard_pile.pop(0))
            self.discard_pile.insert(0, self.draw_pile.pop(0))
            print('starting on wilddraw4... card being inserted back into deck at ' + str(r))
        if self.discard_pile[0].number == 10:
            pick = self.pick_from_draw_pile(2)
            self.players[0].cards.extend(pick)
            self.action_note = self.players[0].user.display_name + ' starts by drawing 2 cards.'
        elif self.discard_pile[0].number == 11:
            self.order = -1
            self.turn = len(self.players) - 1
            self.action_note = 'Turn order starts in reverse.'
        elif self.discard_pile[0].number == 12:
            self.turn = (self.turn + 1) % len(self.players)
            self.action_note = self.players[0].user.display_name + ' starts by being skipped.'

        self.p_prev = None
        self.p_now = self.players[self.turn]
        self.p_next = self.players[(self.turn + self.order) % len(self.players)]
        self.game_embed.title = ''
        self.game_embed.description = ''
        self.game_embed.clear_fields()
        self.game_embed.add_field(name='PLAYING NOW', value=self.p_now.user.display_name)
        self.game_embed.add_field(name='PLAYING NEXT', value=self.p_next.user.display_name)
        self.game_embed.add_field(name='RECENT ACTION', value=self.action_note, inline=False)

        await self.update_all_players()

    async def update_all_players(self):
        self.game_embed.colour = colours[self.discard_pile[0].suit]
        self.game_embed.set_image(url=self.discard_pile[0].url)
        self.game_embed.set_author(name=self.p_now.user.display_name, icon_url=self.p_now.user.avatar_url)
        self.game_embed.set_field_at(0, name='PLAYING NOW', value=self.p_now.user.display_name)
        self.game_embed.set_field_at(1, name='PLAYING NEXT', value=self.p_next.user.display_name)
        self.game_embed.set_field_at(2, name='RECENT ACTION', value=self.action_note, inline=False)
        await self.game_msg.edit(embed=self.game_embed)

        for p in self.players:
            p.embed.colour = colours[self.discard_pile[0].suit]
            p.embed.set_thumbnail(url=self.discard_pile[0].url)
            p.embed.set_field_at(0, name='PLAYING NOW', value=self.p_now.user.display_name)
            p.embed.set_field_at(1, name='PLAYING NEXT', value=self.p_next.user.display_name)
            p.embed.set_field_at(2, name='RECENT ACTION', value=self.action_note, inline=False)
            await p.msg.edit(embed=p.embed)

        if self.p_prev:
            self.p_prev.embed.description += " " + self.p_now.user.display_name + ' is playing now.'
            if len(self.p_prev.cards) > 0:
                img_url = await self.image_of_cards(self.p_prev.cards)
                self.p_prev.embed.set_image(url=img_url)
                self.p_prev.embed.set_thumbnail(url=self.discard_pile[0].url)
            await self.p_prev.msg.edit(embed=self.p_prev.embed)

        self.p_next.embed.description = self.p_now.user.display_name + ' is playing now. Your turn to play next.'
        await self.p_next.msg.edit(embed=self.p_next.embed)

        for p in self.players:
            if p == self.p_now or p == self.p_next or p == self.p_prev:
                continue
            else:
                p.embed.description = self.p_now.user.display_name + ' is playing now.'
                await p.msg.edit(embed=p.embed)

        self.p_now.embed.description = 'It is now your turn to play.'
        self.p_now.embed.colour = colours[self.discard_pile[0].suit]
        self.p_now.embed.set_thumbnail(url=self.discard_pile[0].url)
        self.set_card_reactions()
        img_url = await self.image_of_cards(self.p_now.cards, True)
        self.p_now.embed.set_image(url=img_url)
        await self.p_now.msg.edit(embed=self.p_now.embed)
        count = 0
        for c in self.p_now.cards:
            if c.reaction > count:
                count = c.reaction
        for i in range(count + 1):
            await self.p_now.msg.add_reaction(reaction_emojis[i])

    def set_card_reactions(self):
        if self.p_prev:
            for c in self.p_prev.cards:
                c.reaction = 0
        self.discard_pile[0].reaction = 0
        # self.playable_cards = [0]
        can_match_suit = self.discard_pile[0].suit == 4
        for c in self.p_now.cards:
            c.reaction = 0
            if c.suit == self.discard_pile[0].suit:
                can_match_suit = True
        r = 1
        for c in self.p_now.cards:
            if c.reaction == 0:
                if c.suit < 4:
                    if c.suit == self.discard_pile[0].suit or c.number == self.discard_pile[0].number or self.discard_pile[0].suit == 4:
                        a = 1
                        for ci in self.p_now.cards:
                            if ci.reaction == 0:
                                continue
                            if c.name == ci.name:
                                c.reaction = ci.reaction
                                a = 0
                                break
                        if a:
                            c.reaction = r
                            r += 1
                if c.suit == 4:
                    if c.number == 50:
                        a = 1
                        for ci in self.p_now.cards:
                            if ci.reaction == 0:
                                continue
                            if c.name == ci.name:
                                c.reaction = ci.reaction
                                a = 0
                                break
                        if a:
                            c.reaction = r
                            r += 1
                    if c.number == 51:
                        if not can_match_suit:
                            a = 1
                            for ci in self.p_now.cards:
                                if ci.reaction == 0:
                                    continue
                                if c.name == ci.name:
                                    c.reaction = ci.reaction
                                    a = 0
                                    break
                            if a:
                                c.reaction = r
                                r += 1

    async def now_reaction(self, reaction):
        if reaction.emoji in color_emojis:
            self.wild_card.suit = color_emojis.index(reaction.emoji)
            await self.wild_msg.delete()
            await self.now_play(self.wild_card)
        elif reaction.emoji == '🅾':
            await self.p_now.msg.clear_reactions()
            await self.now_draw()
        elif reaction.emoji in reaction_emojis:
            card = 0
            r = reaction_emojis.index(reaction.emoji)
            for c in self.p_now.cards:
                if r == c.reaction:
                    card = c
                    break
            if card == 0:
                return
            await self.p_now.msg.clear_reactions()
            if card.number == 50 or card.number == 51:
                self.wild_card = card
                wild_embed.set_footer(text=card.name)
                self.wild_msg = await self.p_now.channel.send(embed=wild_embed)
                for r in color_emojis:
                    await self.wild_msg.add_reaction(r)
            else:
                await self.now_play(card)

    async def now_draw(self):
        c = self.draw_pile.pop(0)
        dp0 = self.discard_pile[0]
        self.p_now.cards.append(c)
        if c.suit != 4 and (c.suit == dp0.suit or c.number == dp0.number):
            self.action_note = self.p_now.user.display_name + ' opted to draw a card. '
            await self.now_play(c, True)
        else:
            self.action_note = self.p_now.user.display_name + ' opted to draw a card.'
            await self.next()

    async def now_play(self, card, draw=False):
        self.discard_pile.insert(0, card)
        self.p_now.cards.remove(card)
        if draw:
            self.action_note += ' and then played ' + card.name
        else:
            self.action_note = self.p_now.user.display_name + ' played ' + card.name
        d = 'You played ' + card.name + '.'
        if self.discard_pile[0].number == 50 or self.discard_pile[0].number == 51:
            d += ' Color: '
            if self.discard_pile[0].suit == 0:
                d += '🔴red'
                self.action_note += ' 🔴red'
            if self.discard_pile[0].suit == 1:
                d += '🟡yellow'
                self.action_note += ' 🟡yellow'
            if self.discard_pile[0].suit == 2:
                d += '🟢green'
                self.action_note += ' 🟢green'
            if self.discard_pile[0].suit == 3:
                d += '🔵blue'
                self.action_note += ' 🔵blue'
        self.p_now.embed.description = d
        await self.next(card.number)

    async def next(self, number=0):
        if number == 12 or (number == 11 and len(self.players) == 2):
            self.turn = (self.turn + self.order) % len(self.players)
            self.p_next.embed.description = 'Just kidding! You\'ve been skipped.'
            self.action_note = self.p_now.user.display_name + ' skipped ' + self.p_next.user.display_name + '\'s turn'
        elif number == 11:
            self.order *= -1
            for p in self.players:
                if self.order == 1:
                    p.embed.set_footer(text=' -> '.join(self.clockwise_order))
                else:
                    p.embed.set_footer(text=' -> '.join(self.counterclockwise_order))
            self.p_next.embed.description = 'Just kidding! Turn order has been reversed.'
            if self.p_prev:
                self.p_prev.embed.description = 'Surprise! Turn order has been reversed. You get to play now.'
            self.action_note = self.p_now.user.display_name + ' reversed the turn order.'
        elif number == 10:
            self.turn = (self.turn + self.order) % len(self.players)
            pick = self.pick_from_draw_pile(2)
            self.p_next.cards.extend(pick)
            img_url = await self.image_of_cards(self.p_next.cards)
            self.p_next.embed.set_image(url=img_url)
            self.p_next.embed.description = 'That\'s too bad! You\'ve drawn 2 cards.'
            self.action_note = self.p_now.user.display_name + ' compels ' + self.p_next.user.display_name + ' to draw 2 cards.'
        elif number == 51:
            self.turn = (self.turn + self.order) % len(self.players)
            pick = self.pick_from_draw_pile(4)
            self.p_next.cards.extend(pick)
            img_url = await self.image_of_cards(self.p_next.cards)
            self.p_next.embed.set_image(url=img_url)
            self.p_next.embed.description = 'That\'s too bad! You\'ve drawn 4 cards.'
            self.action_note = self.p_next.user.display_name + ' has drawn 4 cards! Color: '
            if self.discard_pile[0].suit == 0:
                self.action_note += '🔴red'
            if self.discard_pile[0].suit == 1:
                self.action_note += '🟡yellow'
            if self.discard_pile[0].suit == 2:
                self.action_note += '🟢green'
            if self.discard_pile[0].suit == 3:
                self.action_note += '🔵blue'

        if len(self.p_now.cards) == 0:
            await self.now_win()
        else:
            self.turn = (self.turn + self.order) % len(self.players)
            self.p_prev = self.p_now
            self.p_now = self.players[self.turn]
            self.p_next = self.players[(self.turn + self.order) % len(self.players)]
            await self.update_all_players()

    async def now_win(self):
        self.game_stage = 'join'
        for p in self.players:
            await p.channel.delete()
        self.players = []
        self.new_deck()
        self.game_embed = discord.Embed(
            title=self.p_now.user.display_name + ' won! Starting a new game soon.',
            description='☑React to join. Remove your reaction to leave.',
            color=colours[4]
        )
        await self.game_msg.edit(embed=self.game_embed)
        await self.game_msg.clear_reactions()
        await self.game_msg.add_reaction('☑')

    async def end_game(self):
        self.game_stage = 'join'
        for p in self.players:
            await p.channel.delete()
        self.players = []
        self.new_deck()
        self.game_embed = discord.Embed(
            title='The game ended. Starting a new game soon.',
            description='☑React to join. Remove your reaction to leave.',
            color=colours[4]
        )
        await self.game_msg.edit(embed=self.game_embed)
        await self.game_msg.clear_reactions()
        await self.game_msg.add_reaction('☑')

    async def close_game(self):
        for p in self.players:
            await p.channel.delete()
        await self.game_channel.delete()
        await self.category.delete()

    async def kick(self):
        if self.game_stage != 'play':
            return
        self.game_stage = 'kick'
        for p in self.players:
            if p == self.p_now:
                continue
            embed = discord.Embed(
                title='Is ' + self.p_now.user.display_name + ' taking too long to play?',
                description='🦿React to kick them from the game.',
                color=discord.colour.Color.from_rgb(50, 200, 200)
            )
            p.kick_msg = await p.channel.send(embed=embed)
            await p.kick_msg.add_reaction('🦿')

    async def cancel_kick(self):
        self.game_stage = 'play'
        self.kick_votes = []
        for p in self.players:
            if p == self.p_now:
                continue
            embed = discord.Embed(
                title=self.p_now.user.display_name + 'is now playing.',
                description='This vote has been canceled',
                color=discord.colour.Color.from_rgb(50, 200, 200)
            )
            await p.kick_msg.clear_reactions()
            await p.kick_msg.edit(embed=embed)
            await p.kick_msg.delete(delay=2)

    async def kick_vote_add(self, user):
        if self.game_stage == 'kick':
            for p in self.players:
                if p.user.id == user.id:
                    self.kick_votes.append(p)
                    print(str(len(self.kick_votes)) + ' votes')
                    if len(self.kick_votes) > (len(self.players) - 1) / 2:
                        await self.kick_now()

    def kick_vote_remove(self, user):
        if self.game_stage == 'kick':
            for p in self.kick_votes:
                if p.user.id == user.id:
                    self.players.remove(p)
                    break

    async def kick_now(self):
        if self.game_stage == 'kick':
            self.game_stage = 'play'
            self.action_note = self.p_now.user.display_name + ' was kicked from the game.'
            for p in self.players:
                if not p.kick_msg:
                    continue
                embed = discord.Embed(
                    title='Majority rules!',
                    description=self.p_now.user.display_name + ' has been removed from the game.',
                    color=discord.colour.Color.from_rgb(50, 200, 200)
                )
                await p.kick_msg.clear_reactions()
                await p.kick_msg.edit(embed=embed)
                await p.kick_msg.delete(delay=2)
            while len(self.p_now.cards) > 0:
                self.discard_pile.insert(1, self.p_now.cards.pop(0))
            await self.p_now.channel.delete()
            self.players.remove(self.p_now)
            self.clockwise_order = []
            self.counterclockwise_order = []
            for p in self.players:
                self.clockwise_order.append(p.user.display_name)
                self.counterclockwise_order.insert(0, p.user.display_name)
            for p in self.players:
                if self.order == 1:
                    p.embed.set_footer(text=' -> '.join(self.clockwise_order))
                else:
                    p.embed.set_footer(text=' -> '.join(self.counterclockwise_order))
            self.turn = self.turn % len(self.players)
            self.p_prev = None
            self.p_now = self.players[self.turn]
            self.p_next = self.players[(self.turn + self.order) % len(self.players)]
            if len(self.players) == 1:
                await self.now_win()
            else:
                await self.update_all_players()

    async def kick_user(self, user):
        if self.game_stage != 'play':
            return
        player = None
        for p in self.players:
            if p.user.id == user.id:
                player = p
                break
        for p in self.players:
            embed = discord.Embed(
                title='PLAYER LEFT',
                description=user.display_name + ' has been removed from the game.',
                color=discord.colour.Color.from_rgb(50, 200, 200)
            )
            msg = await p.channel.send(embed=embed)
            await msg.delete(delay=2)
        while len(player.cards) > 0:
            self.discard_pile.insert(1, player.cards.pop(0))
        await player.channel.delete()
        self.players.remove(player)
        self.clockwise_order = []
        self.counterclockwise_order = []
        for p in self.players:
            self.clockwise_order.append(p.user.display_name)
            self.counterclockwise_order.insert(0, p.user.display_name)
        for p in self.players:
            if self.order == 1:
                p.embed.set_footer(text=' -> '.join(self.clockwise_order))
            else:
                p.embed.set_footer(text=' -> '.join(self.counterclockwise_order))
        self.turn = self.turn % len(self.players)
        if player == self.p_prev:
            self.p_prev = None
        elif player == self.p_now:
            self.p_now = self.players[self.turn]
            self.p_next = self.players[(self.turn + self.order) % len(self.players)]
        elif player == self.p_next:
            self.p_next = self.players[(self.turn + self.order) % len(self.players)]
        if len(self.players) == 1:
            await self.now_win()
        else:
            await self.update_all_players()


class uno(commands.Cog):
    def __init__(self, client):
        self.client = client
        self.hand_channel = client.get_channel(711745233112662117)
        self.games = []

    @commands.Cog.listener()
    async def on_reaction_add(self, reaction, user):
        if user.id == self.client.user.id:
            return
        for g in self.games:
            if reaction.message.guild == g.guild:
                await g.on_reaction_add(reaction, user)
                break

    @commands.Cog.listener()
    async def on_reaction_remove(self, reaction, user):
        if user.id == self.client.user.id:
            return
        for g in self.games:
            if reaction.message.guild == g.guild:
                await g.on_reaction_remove(reaction, user)
                break

    @commands.command()
    async def open(self, ctx):
        for g in self.games:
            if ctx.guild == g.guild:
                return
        game = Game(ctx.guild, self.hand_channel)
        self.games.append(game)
        await game.new_game()

    @commands.command()
    async def start(self, ctx):
        for g in self.games:
            if ctx.guild == g.guild:
                await g.start_game()
                break

    @commands.command()
    async def end(self, ctx):
        for g in self.games:
            if ctx.guild == g.guild:
                await g.end_game()
                break

    @commands.command()
    async def close(self, ctx):
        for g in self.games:
            if ctx.guild == g.guild:
                await g.close_game()
                self.games.remove(g)
                break

    @commands.command()
    async def kick(self, ctx):
        for g in self.games:
            if ctx.guild == g.guild:
                await g.kick()
                break

    @commands.command()
    async def leave(self, ctx):
        for g in self.games:
            if ctx.guild == g.guild:
                await g.kick_user(ctx.author)
                break


def setup(client):
    client.add_cog(uno(client))
