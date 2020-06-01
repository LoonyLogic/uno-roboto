class Player:
    def __init__(self, user, cards, channel, embed, msg):
        self.user = user
        self.cards = cards
        self.channel = channel
        self.embed = embed
        self.msg = msg
        self.kick_msg = None
