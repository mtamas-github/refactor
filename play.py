from yatzy import Yatzy

dice = Yatzy.generate_dice()
chance = Yatzy.chance(dice[0], dice[1], dice[2], dice[3], dice[4])
pair = Yatzy.score_pair(dice[0], dice[1], dice[2], dice[3], dice[4])
yatzy = Yatzy.yatzy(dice)
threeofakind = Yatzy.three_of_a_kind(dice[0], dice[1], dice[2], dice[3], dice[4])


# some example calls.
print(chance)
print(pair)
print(yatzy)
print(threeofakind)
