__author__ = 'mamaray'

"""
Function to generate permutations of outcomes
Repetition of outcomes not allowed
"""


def gen_permutations(outcomes, length):
    """
    Iterative function that enumerates the set of all sequences of outcomes of given length
    """

    ans = set([()])
    for dummy_idx in range(length):
        temp = set()
        for seq in ans:
            for item in outcomes:
                new_seq = list(seq)
                new_seq.append(item)
                if len(new_seq) == len(set(new_seq)):
                    temp.add(tuple(new_seq))
        ans = temp
    return ans


def run_example():
    # example for digits
    outcome = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    # outcome = ["Red", "Green", "Blue"]
    # outcome = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

    length = 5
    permtutations = gen_permutations(outcome, length)
    print "Computed", len(permtutations), "permutations of length", str(length)
    # print "Permutations were", permtutations


run_example()



# ######################################
# Example output below
#
# Computed 90 permutations of length 2
# Permutations were set([(0, 1), (0, 2), (0, 3), (0, 4), (0, 5), (0, 6), (0, 7), (0, 8), (0, 9), (1, 0), (1, 2), (1, 3),
# (1, 4), (1, 5), (1, 6), (1, 7), (1, 8), (1, 9), (2, 0), (2, 1), (2, 3), (2, 4), (2, 5), (2, 6), (2, 7), (2, 8),
# (2, 9), (3, 0), (3, 1), (3, 2), (3, 4), (3, 5), (3, 6), (3, 7), (3, 8), (3, 9), (4, 0), (4, 1), (4, 2), (4, 3),
# ...


# Computed 6 permutations of length 2
# Permutations were set([('Red', 'Green'), ('Red', 'Blue'), ('Green', 'Red'), ('Green', 'Blue'), ('Blue', 'Red'),
# ('Blue', 'Green')])


# Computed 210 permutations of length 3
# Permutations were set([('Sunday', 'Monday', 'Tuesday'), ('Sunday', 'Monday', 'Wednesday'),
# ('Sunday', 'Monday', 'Thursday'), ('Sunday', 'Monday', 'Friday'), ('Sunday', 'Monday', 'Saturday'),
# ('Sunday', 'Tuesday', 'Monday'), ('Sunday', 'Tuesday', 'Wednesday'), ('Sunday', 'Tuesday', 'Thursday'),
# ...


## Final example for homework problem
#
outcome = set(["a", "b", "c", "d", "e", "f"])

permutations = gen_permutations(outcome, 4)
permutation_list = list(permutations)
permutation_list.sort()
print
print "Answer is", permutation_list[100]
