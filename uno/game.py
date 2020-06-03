import random
from uno.action import Action
from uno.action import ActFlags
from uno.card import Card
from uno.player import Player


class Game:
    def __init__(self):
        self.game_stage = 'end'
        self.turn = 0
        self.order = 1
        self.players = []
        self.draw_pile = []
        self.discard_pile = []
        self.p_now = None
        self.p_next = None
        self.p_prev = None
        self.action_history = []
        self.playable_cards = []

    def new_game(self):
        self.players = []
        self.new_deck()
        self.game_stage = 'join'

    def new_deck(self):
        self.draw_pile = []
        self.discard_pile = []
        for s in range(4):
            for n in range(13):
                if n == 0:
                    self.draw_pile.append(Card(s, n))
                else:
                    self.draw_pile.append(Card(s, n))
                    self.draw_pile.append(Card(s, n))
        for i in range(4):
            self.draw_pile.append(Card(4, 50))
            self.draw_pile.append(Card(4, 51))
        random.shuffle(self.draw_pile)

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

    def start_game(self, number_of_players):
        if self.game_stage != 'join':
            return None
        if number_of_players < 2 or number_of_players > 10:
            return None

        self.game_stage = 'play'
        self.players = []
        for i in range(number_of_players):
            self.players.append(Player(self.pick_from_draw_pile(7)))
        self.turn = 0
        self.discard_pile.insert(0, self.draw_pile.pop(0))
        top = self.discard_pile[0]
        while top.number == 51:
            r = random.randint(1, len(self.draw_pile) + 1)
            print(f'starting on {top.name}... card being inserted back into deck at {str(r)}')
            self.draw_pile.insert(r, self.discard_pile.pop(0))
            self.discard_pile.insert(0, self.draw_pile.pop(0))
            top = self.discard_pile[0]
        af = ActFlags(is_start=True)
        action = Action(af, card=top.name)
        if top.number == 10:
            action.target = 0
            action.cards = self.pick_from_draw_pile(2)
            self.players[0].cards.extend(action.cards)
            action.act_flags.has_target = True
            action.act_flags.is_draw2 = True
        elif top.number == 11:
            self.order = -1
            self.turn = len(self.players) - 1
            action.act_flags.is_reverse = True
        elif top.number == 12:
            action.target = 0
            self.turn = (self.turn + 1) % len(self.players)
            action.act_flags.has_target = True
            action.act_flags.is_skip = True
        self.action_history.append(action)

        self.p_prev = None
        self.p_now = self.players[self.turn]
        self.p_next = self.players[(self.turn + self.order) % len(self.players)]

        self.set_playable()

        return action

    def set_playable(self):
        self.playable_cards = []
        top = self.discard_pile[0]
        can_match_suit = top.suit == 4
        for c in self.p_now.cards:
            c.reaction = 0
            if c.suit == top.suit:
                can_match_suit = True
        for c in self.p_now.cards:
            if c.name in self.playable_cards:
                continue
            if c.suit < 4:
                if c.suit == top.suit or c.number == top.number or top.suit == 4:
                    self.playable_cards.append(c.name)
            if c.suit == 4:
                if c.number == 50:
                    self.playable_cards.append(c.name)
                if c.number == 51:
                    if not can_match_suit:
                        self.playable_cards.append(c.name)

    def play(self, index, suit=-1):
        if not self.p_now:
            return None
        action = None
        n = self.playable_cards[index]
        number = 0
        for c in self.p_now.cards:
            if n == c.name:
                if c.number >= 50 and suit == -1:
                    return
                af = ActFlags(has_actor=True, is_play=True, has_card=True)
                action = Action(af, actor=self.turn, card=c.name)
                if c.number >= 50:
                    action.act_flags.has_color = True
                    action.color = suit
                    c.suit = suit
                self.discard_pile.insert(0, c)
                self.p_now.cards.remove(c)
                number = c.number
                break
        if action is None:
            return None
        return self.next(action, number)

    def draw(self):
        if not self.p_now:
            return None
        c = self.draw_pile.pop(0)
        self.p_now.cards.append(c)
        top = self.discard_pile[0]
        number = 0
        if c.suit != 4 and (c.suit == top.suit or c.number == top.number):
            af = ActFlags(has_actor=True, is_draw=True, is_play=True, has_card=True)
            action = Action(af, actor=self.turn, card=c.name)
            self.discard_pile.insert(0, c)
            self.p_now.cards.remove(c)
            number = c.number
        else:
            af = ActFlags(has_actor=True, is_draw=True)
            action = Action(af, actor=self.turn, card=c.name)
        return self.next(action, number)

    def next(self, action, number=0, color=-1):
        if number == 12 or (number == 11 and len(self.players) == 2):
            self.turn = (self.turn + self.order) % len(self.players)
            action.act_flags.is_skip = True
            action.act_flags.has_target = True
            action.target = self.turn
        elif number == 11:
            self.order *= -1
            action.act_flags.is_reverse = True
        elif number == 10:
            self.turn = (self.turn + self.order) % len(self.players)
            pick = self.pick_from_draw_pile(2)
            self.p_next.cards.extend(pick)
            action.cards = pick
            action.act_flags.is_draw2 = True
            action.act_flags.has_target = True
            action.target = self.turn
        elif number == 51:
            self.turn = (self.turn + self.order) % len(self.players)
            pick = self.pick_from_draw_pile(4)
            self.p_next.cards.extend(pick)
            action.cards = pick
            action.act_flags.is_draw4 = True
            action.act_flags.has_target = True
            action.target = self.turn

        self.action_history.append(action)

        if len(self.p_now.cards) == 0:
            self.end_game()
            action.act_flags.is_end = True
        else:
            self.turn = (self.turn + self.order) % len(self.players)
            self.p_prev = self.p_now
            self.p_now = self.players[self.turn]
            self.p_next = self.players[(self.turn + self.order) % len(self.players)]
            self.set_playable()
        return action

    def end_game(self):
        self.game_stage = 'end'
        # self.players = []
        # self.new_deck()
        return

    def kick_now(self):
        return self.remove_player(self.p_now)

    def remove_player(self, player):
        if self.game_stage != 'play':
            return
        af = ActFlags(has_actor=True, is_exit=True)
        action = Action(af, actor=self.players.index(player))
        self.action_history.append(action)
        while len(player.cards) > 0:
            self.discard_pile.insert(1, player.cards.pop(0))
        self.players.remove(player)
        self.turn = self.turn % len(self.players)
        if player == self.p_prev:
            self.p_prev = None
        elif player == self.p_now:
            self.p_now = self.players[self.turn]
            self.p_next = self.players[(self.turn + self.order) % len(self.players)]
        elif player == self.p_next:
            self.p_next = self.players[(self.turn + self.order) % len(self.players)]
        if len(self.players) == 1:
            action.act_flags.is_end = True
        return action
