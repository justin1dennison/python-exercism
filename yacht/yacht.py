from collections import Counter
# Score categories
# Change the values as you see fit
YACHT = 0 
ONES = 1 
TWOS = 2 
THREES = 3 
FOURS = 4 
FIVES = 5 
SIXES = 6 
FULL_HOUSE = 7 
FOUR_OF_A_KIND = 8 
LITTLE_STRAIGHT = 9 
BIG_STRAIGHT = 10 
CHOICE = 11 

def is_straight(dice):
    dice = list(sorted(dice))
    diffs = ((p - n) for p, n in zip(dice, dice[1:]))
    absolutes = (abs(d) for d in diffs)
    return all(a == 1 for a in absolutes)


def score(dice, category):
    counts = Counter(dice)
    if category == ONES:
        return 1 * counts.get(1, 0)
    if category == TWOS:
        return 2 * counts.get(2, 0)
    if category == THREES:
        return 3 * counts.get(3, 0)
    if category == FOURS:
        return 4 * counts.get(4, 0)
    if category == FIVES:
        return 5 * counts.get(5, 0)
    if category == SIXES:
        return 6 * counts.get(6, 0)
    if category == BIG_STRAIGHT:
        return (30 if is_straight(dice) and 1 not in dice
                    else 0)
    if category == LITTLE_STRAIGHT:
        return (30 if is_straight(dice)  and 1 in dice
                  else 0)
    if category == CHOICE:
        return sum(dice)
    if category == FOUR_OF_A_KIND:
        most_common = counts.most_common()
        topval, top_count = counts.most_common(1)[0]
        return 0 if top_count < 4 else 4 * topval
    if category == FULL_HOUSE:
        most_common = counts.most_common()
        cs = [count for val, count in most_common]
        return 0 if cs != [3,2] else sum(dice)
    if category == YACHT:
        return (50 if counts.most_common(1)[0][1] == 5 else 0)
