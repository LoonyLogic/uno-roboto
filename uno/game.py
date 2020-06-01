import random
from uno.action import Action
from uno.card import Card
from uno.player import Player


class Game:
    def __init__(self):
        self.game_stage = 0
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
        action = Action(-1, 1, top.name)
        if top.number == 10:
            action.target = 0
            action.cards = self.pick_from_draw_pile(2)
            self.players[0].cards.extend(action.cards)
        elif top.number == 11:
            self.order = -1
            self.turn = len(self.players) - 1
        elif top.number == 12:
            action.target = 0
            self.turn = (self.turn + 1) % len(self.players)
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
        for c in self.p_now.cards:
            if n == c.name:
                if c.number >= 50 and suit == -1:
                    return
                action = Action(self.turn, 1, c.name)
                if c.number >= 50:
                    c.suit = suit
                    action.target = suit
                self.discard_pile.insert(0, c)
                self.p_now.cards.remove(c)
                break
        return self.next(action)

    def draw(self):
        if not self.p_now:
            return None
        c = self.draw_pile.pop(0)
        self.p_now.cards.append(c)
        top = self.discard_pile[0]
        if c.suit != 4 and (c.suit == top.suit or c.number == top.number):
            action = Action(self.p_now.turn, 2, c.name)
            self.discard_pile.insert(0, c)
            self.p_now.cards.remove(c)
        else:
            action = Action(self.p_now.turn, 0, c)
        return self.next(action)

    def next(self, action):
        number = 0
        if action.act > 0:
            number = action.card.number
        if number == 12 or (number == 11 and len(self.players) == 2):
            self.turn = (self.turn + self.order) % len(self.players)
            action.act = 8
        elif number == 11:
            self.order *= -1
            action.act = 7
        elif number == 10:
            self.turn = (self.turn + self.order) % len(self.players)
            pick = self.pick_from_draw_pile(2)
            self.p_next.cards.extend(pick)
            action.cards = pick
            action.act = 6
        elif number == 50:
            action.act = 9
        elif number == 51:
            self.turn = (self.turn + self.order) % len(self.players)
            pick = self.pick_from_draw_pile(4)
            self.p_next.cards.extend(pick)
            action.cards = pick
            action.act = 10

        self.action_history.append(action)

        actions = [action]
        if len(self.p_now.cards) == 0:
            actions.append(self.now_win())
        else:
            self.turn = (self.turn + self.order) % len(self.players)
            self.p_prev = self.p_now
            self.p_now = self.players[self.turn]
            self.p_next = self.players[(self.turn + self.order) % len(self.players)]
        return actions

    def now_win(self):
        self.game_stage = 'join'
        action = Action(self.turn, 4, 'None')
        self.action_history.append(action)
        self.players = []
        self.new_deck()
        return action

    def end_game(self):
        self.game_stage = 'join'
        action = Action(-1, 5, 'None')
        self.action_history.append(action)
        self.players = []
        self.new_deck()
        return action

    def kick_now(self):
        return self.remove_player(self.p_now)

    def remove_player(self, player):
        if self.game_stage != 'play':
            return
        action = Action(self.players.index(player), 3, 'None')
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
        actions = [action]
        if len(self.players) == 1:
            actions.append(self.now_win())
        return actions
