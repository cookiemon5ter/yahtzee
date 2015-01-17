import yaht


class Player:
    def __init__(self):

        self.upper = ["ones", "twos", "threes", "fours", "fives", "sixes"]

        self.lower = ["fh", "tk", "fk", "ss", "ls", "yahtzee", "chance"]

        self.scores = {}

        for key in self.upper + self.lower:
            self.scores[key] = None

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

    def add_score(self, item, dice):
        functions = {"ones": yaht.ones(dice),
                     "twos": yaht.twos(dice),
                     "threes": yaht.threes(dice),
                     "fours": yaht.fours(dice),
                     "fives": yaht.fives(dice),
                     "sixes": yaht.sixes(dice),
                     "fh": yaht.fh(dice),
                     "tk": yaht.tk(dice),
                     "fk": yaht.fk(dice),
                     "ss": yaht.ss(dice),
                     "ls": yaht.ls(dice),
                     "yahtzee": yaht.yahtzee(dice),
                     "chance": yaht.chance(dice)}

        if item in Player().scores.keys() and self.player.scores[item] is None:
            self.player.scores[item] = functions[item]
            return True
        elif item not in Player().scores.keys():
            print "invalid input"  # think of better things to output
            return False
        else:
            print "That item has been added to already"
            return False