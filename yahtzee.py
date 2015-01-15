import yaht


class Player:
    def __init__(self):

        self.scores = {"ones": None, "twos": None, "threes": None, "fours": None, "fives": None, "sixes": None,
                       "fh": None, "tk": None, "fk": None, "ss": None, "ls": None, "yahtzee": None, "chance": None}

        self.upper = ["ones", "twos", "threes", "fours", "fives", "sixes"]

        self.lower = ["fh", "tk", "fk", "ss", "ls", "yahtzee", "chance"]

        self.bonus = 0

        self.total = 0


class Game:
    def __init__(self):
        self.player = Player()

    def run(self):
        for i in range(2):
            print "roll %d" % (i + 1)
            roll = yaht.getnew()
            print "%s your roll\n" % roll