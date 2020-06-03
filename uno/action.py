class Action:
    def __init__(self, act_flags, *, actor=-1, card='NONE', target=-1, cards=None, color=-1):
        self.act_flags = act_flags
        self.actor = actor
        self.card = card
        self.target = target
        self.cards = cards
        self.color = color


class ActFlags:
    def __init__(self, *, has_actor=False, has_target=False, has_card=False, has_cards=False, has_color=False,
                 is_play=False, is_draw=False, is_draw2=False, is_draw4=False, is_reverse=False, is_skip=False,
                 is_exit=False, is_start=False, is_end=False):
        self.has_actor = has_actor
        self.has_target = has_target
        self.has_card = has_card
        self.has_cards = has_cards
        self.has_color = has_color
        self.is_play = is_play
        self.is_draw = is_draw
        self.is_draw2 = is_draw2
        self.is_draw4 = is_draw4
        self.is_reverse = is_reverse
        self.is_skip = is_skip
        self.is_exit = is_exit
        self.is_start = is_start
        self.is_end = is_end
