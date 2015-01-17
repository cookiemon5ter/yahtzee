import yaht


class Player:
    def __init__(self):

        self.upper = ["ones", "twos", "threes", "fours", "fives", "sixes"]

        self.lower = ["fh", "tk", "fk", "ss", "ls", "yahtzee", "chance"]

        self.scores = {}

        for key in self.upper + self.lower:
            self.scores[key] = None

        self.total = 0


class Game:
    def __init__(self):
        self.player = Player()

    def run(self):
        for i in range(13):
            print "roll %d" % (i + 1)
            roll = yaht.getnew()
            # print "%s your roll\n" % roll

            while True:
                print "%s your roll\n" % roll
                item = raw_input("what would you like to do: ")
                if item == "show":
                    self.show_board()
                    continue
                elif self.add_score(item, roll):
                    break
                else:
                    continue

        print self.sum_score()

    def show_board(self):
        print "upper score"
        print "-------------"
        for i in Player().upper:
            if self.player.scores[i] is None:
                pts = 'x'
            else:
                pts = self.player.scores[i]
            print "%-8s = %s" % (i, pts)

        print "\nlower score"
        print "-------------"
        for i in Player().lower:
            if self.player.scores[i] is None:
                pts = 'x'
            else:
                pts = self.player.scores[i]
            print "%-8s = %s" % (i, pts)

    def sum_score(self):
        upper = sum([self.player.scores[i] for i in self.player.upper])
        lower = sum([self.player.scores[i] for i in self.player.lower])

        if upper >= 63:
            upper += 35

        return upper + lower

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