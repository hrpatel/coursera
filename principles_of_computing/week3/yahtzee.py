# coding=utf-8
"""
Planner for Yahtzee
Simplifications:  only allow discard and roll, only score against upper level
"""

__author__ = 'mamaray'


def gen_all_sequences(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of outcomes of given length.
    """

    answer_set = {()}
    for dummy_idx in range(length):
        temp_set = set()
        for partial_sequence in answer_set:
            for item in outcomes:
                new_sequence = list(partial_sequence)
                new_sequence.append(item)
                temp_set.add(tuple(new_sequence))
        answer_set = temp_set

    return answer_set


def score(hand):
    """
    Compute the maximal score for a Yahtzee hand according to the upper section of the Yahtzee score card. || This
    function takes a hand (which is a tuple of die values) and computes a score for the hand as the maximum of the
    possible values for each choice of box in the upper section of the Yahtzee scorecard

    :param hand: full yahtzee hand

    Returns an integer score
    """

    # initialize local variables
    all_points = {}

    # generate a list of scores
    for item in hand:
        if item in all_points:
            all_points[item] += item
        else:
            all_points[item] = item

    return max(all_points.values())


def expected_value(held_dice, num_die_sides, num_free_dice):
    """
    Compute the expected value of the held_dice given that num_free_dice are to be rolled, each with num_die_sides.
    This function computes the expected value of the scores for the possible Yahtzee hands that result from holding some
    dice and rolling the remaining free dice. The dice being held are specified by the tuple held_dice.  The number of
    sides and the number of dice that are free to be rolled are specified by num_die_sides and  num_free_dice,
    respectively. You should use gen_all_sequences to compute all possible rolls for the dice being rolled. As an
    example, in a standard Yahtzee game using five dice, the length of held_dice plus num_free_dice should always be 5

    :param held_dice: dice that you will hold
    :param num_die_sides: number of sides on each die
    :param num_free_dice: number of dice to be rolled

    Returns a floating point expected value
    """

    # initialize local variables
    expected_val = 0.0

    # figure out all the possible rolls
    next_rolls = gen_all_sequences(range(1, num_die_sides + 1), num_free_dice)

    # keep a running total of all possible scores
    for roll in next_rolls:
        expected_val += float(score(held_dice + roll)) / (num_die_sides ** num_free_dice)

    return expected_val


def gen_all_holds(hand):
    """
    Generate all possible choices of dice from hand to hold || This function takes a tuple hand and returns the set of
    all possible tuples formed by discarding a subset of the entries in hand. The entries in each of these tuples
    correspond to the dice that will be held. If the tuple hand has the entries (h0,h1,...,hm−1), the returned tuples
    should have the form (hi0,hi1,...,hik−1) where 0≤k≤m and the integer indices satisfy 0≤i0<i1<...<ik−1<m. In the case
    where values in the tuple hand happen to be distinct, the set of tuples returned by gen_all_holds will correspond
    to all possible subsets of hand

    :param hand: full yahtzee hand

    Returns a set of tuples, where each tuple is dice to hold
    """

    result_set = {()}
    for item in hand:
        tmp_set = set([])
        for subset in result_set:
            new_list = list(subset)
            new_list.append(item)
            tmp_set.add(tuple(new_list))
        result_set = result_set.union(tmp_set)

    return result_set


def strategy(hand, num_die_sides):
    """
    Compute the hold that maximizes the expected value when the discarded dice are rolled || This function takes a hand
    and computes which dice to hold to maximize the expected value of the score of the possible hands that result from
    rolling the remaining free dice (with the specified number of sides). The function should return a tuple consisting
    of this maximal expected value and the choice of dice that should be held to achieve this value. If there are
    several holds that generate the maximal expected value, you may return any of these holds

    :param hand: full yahtzee hand
    :param num_die_sides: number of sides on each die

    Returns a tuple where the first element is the expected score and the second element is a tuple of the dice to hold
    """

    # initialize local variables
    expected_score = float("-inf")
    hand_to_hold = ()

    # generate all possible dice to hold
    all_holds = gen_all_holds(hand)

    # calculate the largest expected score for each hold
    for possible_hold in all_holds:
        temp_val = expected_value(possible_hold, num_die_sides, len(hand) - len(possible_hold))
        if temp_val > expected_score:
            expected_score = temp_val
            hand_to_hold = possible_hold

    return expected_score, hand_to_hold


def run_example():
    """
    Compute the dice to hold and expected score for an example hand
    """
    num_die_sides = 6
    hand = (1, 1, 1, 5, 6)
    hand_score, hold = strategy(hand, num_die_sides)
    print "Best strategy for hand", hand, "is to hold", hold, "with expected score", hand_score


# run_example()
