class GuildPlayer:
    def __init__(self, user, channel, msg, embed):
        self.id = user.id
        self.name = user.display_name
        self.url = user.avatar_url
        self.channel = channel
        self.msg = msg
        self.embed = embed
        self.player = None

    def set_player(self, player):
        self.player = player
