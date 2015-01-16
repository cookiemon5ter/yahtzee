import random

def randDie():
    """Get a random die roll."""
    return random.randint(1,6)


def gr():
    """Roll 5 dice and return them in a list."""
    roll = [randDie() for i in range(5)]
    # print roll
    return roll


def exchange(dice, *exchange):
    """Exchange dice for another or more rolls."""
    for i in range(1,6):
        if i in exchange:
            dice[i - 1] = randDie()
    return dice


def hold(dice, held):
    """Exchange dice that are not in held variable."""
    for i in range(1,6):
        if i not in held:
            dice[i - 1] = randDie()
    return dice


def ones(dice):
    """Return the product of ones rolled."""
    count = [0,0,0,0,0,0,0]

    for i in dice:
        count[i] += 1

    return count[1] * 1


def twos(dice):
    """Return the product of twos rolled."""
    count = [0,0,0,0,0,0,0]

    for i in dice:
        count[i] += 1

    return count[2] * 2


def threes(dice):
    """Return the product of threes rolled."""
    count = [0,0,0,0,0,0,0]

    for i in dice:
        count[i] += 1

    return count[3] * 3


def fours(dice):
    """Return the product of fours rolled."""
    count = [0,0,0,0,0,0,0]

    for i in dice:
        count[i] += 1

    return count[4] * 4


def fives(dice):
    """Return the product of fives rolled."""
    count = [0,0,0,0,0,0,0]

    for i in dice:
        count[i] += 1

    return count[5] * 5


def sixes(dice):
    """Return the product of sixes rolled."""
    count = [0,0,0,0,0,0,0]

    for i in dice:
        count[i] += 1

    return count[6] * 6


def fh(dice):
    """Check if you have a fullhouse if so return 25 pts else return 0."""
    count = [0,0,0,0,0,0,0]

    for i in dice:
        count[i] += 1

    if 2 in count and 3 in count:
        return 25
    else:
        return 0


def tk(dice):
    """Check if you have three of a kind if so return sum else 0."""
    count = [0,0,0,0,0,0,0]

    for i in dice:
        count[i] += 1

    if 3 in count or 4 in count or 5 in count:
        return sum(dice)
    else:
        return 0


def fk(dice):
    """Check if you have four of a kind if so return sum else 0."""
    count = [0,0,0,0,0,0,0]

    for i in dice:
        count[i] += 1

    if 4 in count or 5 in count:
        return sum(dice)
    else:
        return 0


def ss(dice):
    """Check if you have a smallstraight if so return 30 pts else 0."""
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
    """Check if you have a largestraight if so return 40 pts else 0."""
    dice.sort()
    if tuple(dice) == (1,2,3,4,5):
        return 40
    elif tuple(dice) == (2,3,4,5,6):
        return 40
    else:
        return 0


def yahtzee(dice):
    """Check if you have a Yahtzee if so return 50 else 0."""
    count = [0,0,0,0,0,0,0]

    for i in dice:
        count[i] += 1

    if 5 in count:
        return 50
    else:
        return 0


def chance(dice):
    """Return the sum of your dice."""
    return sum(dice)


def help():
    # this is a work in process it will display a help screen for getnew()
    print "type \"hold\" to hold all dice"
    print "type \"help\" to display this help"
    print "to hold dice specify which e.g. 1 3 4, will hold the first third and fourth"


def getnew():  # need test for bad input
    dice = gr()
    for i in range(2):
        while True:
            b = raw_input("%s hold: " % dice)
            if b == "hold":
                return dice
            elif b == "help":
                help()
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
                    hold(dice, b)
                    break
                else:
                    continue
    return dice

