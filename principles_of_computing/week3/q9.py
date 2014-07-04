__author__ = 'mamaray'

import math

print "using stats", (52/52)*(12.0/51)*(11.0/50)*(10.0/49)*(9.0/48)
print

total_combos = math.factorial(52)/math.factorial(52-5)
suit_combos = math.factorial(13)/math.factorial(13-5)
num_suits = 4.0
print "total 5 card combos in deck", total_combos
print "total 5 card combos in suit", suit_combos
print "num suits", num_suits
print "probability := (suit_combos * num_suits)/total_combos =", float((suit_combos * num_suits)/total_combos)
