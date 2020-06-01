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
