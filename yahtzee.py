import random
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
            roll = self.turn()

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

    def turn(self):
        dice = self.gr()
        for i in range(2):
            while True:
                b = raw_input("%s hold: " % dice)
                if b == "hold":
                    return dice
                elif b == "help":
                    self.show_help()
                    continue
                elif b == "show":
                    self.show_board()
                    continue
                else:
                    b = [int(i) for i in b.split(' ') if i.isdigit()]
                    cont = True
                    for i in b:
                        if i < 1 or i > 5:
                            print "invalid input"
                            cont = False
                            break
                    if cont:
                        self.hold(dice, b)
                        break
                    else:
                        continue
        return dice

    @staticmethod
    def rand_die():
        """Get a random die roll."""
        return random.randint(1, 6)

    @staticmethod
    def gr():
        """Roll 5 dice and return them in a list"""
        return [Game().rand_die() for i in range(5)]

    def hold(self, dice, held):
        """Exchange dice that are not in held variable"""
        for i in range(1, 6):
            if i not in held:
                dice[i - 1] = self.rand_die()
        return dice

    def show_help(self):
        # this is a work in process it will display a help screen for getnew()
        print "type \"hold\" to hold all dice"
        print "type \"help\" to display this help"
        print "to hold dice specify which e.g. 1 3 4, will hold the first third and fourth"

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

    def add_score2(self, item, dice, debug=True):
        upper_digits = {"ones": 1, "twos": 2, "threes": 3, "fours": 4, "fives": 5, "sixes": 6}

        def in_upper(dice, num):
            count = [0, 0, 0, 0, 0, 0, 0]
            for i in dice:
                count[i] += 1
            return count[num] * num

        def fh(dice):
            count = [0, 0, 0, 0, 0, 0, 0]

            for i in dice:
                count[i] += 1

            if 2 in count and 3 in count:
                return 25
            else:
                return 0

        def tk(dice):
            count = [0, 0, 0, 0, 0, 0, 0]

            for i in dice:
                count[i] += 1

            if 3 in count or 4 in count or 5 in count:
                return sum(dice)
            else:
                return 0

        def fk(dice):
            count = [0, 0, 0, 0, 0, 0, 0]

            for i in dice:
                count[i] += 1

            if 4 in count or 5 in count:
                return sum(dice)
            else:
                return 0

        def ss(dice):
            if 3 in dice and 4 in dice:
                if 1 in dice and 2 in dice:
                    return 30
                elif 2 in dice and 5 in dice:
                    return 30
                elif 5 in dice and 6 in dice:
                    return 30
                else:
                    return 0
            else:
                return 0

        def ls(dice):
            copy_dice = list(dice)
            copy_dice.sort()
            if copy_dice == [1, 2, 3, 4, 5]:
                return 40
            elif copy_dice == [2, 3, 4, 5, 6]:
                return 40
            else:
                return 0

        if item in self.player.upper:

            if self.player.scores[item] is None:
                self.player.scores[item] = in_upper(dice, upper_digits[item])
                if debug:
                    print "successfully added"
                return True

            else:
                if debug:
                    print "Item has already been added"
                return False

        elif item in self.player.lower:

            if item == "fh":
                if self.player.scores[item] is None:
                    self.player.scores[item] = fh(dice)
                    if debug:
                        print "successfully added"
                    return True
                else:
                    if debug:
                        print "Item has already been added"
                    return False

            elif item == "ss":
                if self.player.scores[item] is None:
                    self.player.scores[item] = ss(dice)
                    if debug:
                        print "successfully added"
                    return True
                else:
                    if debug:
                        print "Item has already been added"
                    return False

            elif item == "ls":
                if self.player.scores[item] is None:
                    self.player.scores[item] = ls(dice)
                    if debug:
                        print "successfully added"
                    return True
                else:
                    if debug:
                        print "Item was already added"
                    return False

        elif item not in self.player.lower + self.player.upper:
            print "invalid"
        else:
            print "item has been added"