"""
Sorting a list of strings using an alphabetical grid
"""

import random

# constants
NUM_CHARS = 26
CHARACTERS = [chr(ord("a") + char_num) for char_num in range(NUM_CHARS)]


def order_by_letter(string_list, letter_pos):
    """
    Takes a list of strings and order them alphabetically using the letter at the specified position. Start at the end
    of the string and sort letter by letter (by putting in the character buckets)
    """
    buckets = [[] for dummy_idx in range(NUM_CHARS)]
    for string in string_list:
        char_index = ord(string[letter_pos]) - ord("a")
        buckets[char_index] += [string]

    print buckets

    # clean up the empty cells in buckets
    answer = []
    for char_index in range(NUM_CHARS):
        answer += buckets[char_index]

    return answer


def string_sort(string_list, length):
    """
    Order a list of strings of the specific length in ascending alphabetical order
    """
    for position in range(length - 1, -1, -1):
        string_list = order_by_letter(string_list, position)
    return string_list


def run_example():
    """
    Example of string sort
    """
    string_length = 3
    test_list = ["".join([random.choice(CHARACTERS) for _ in range(string_length)]) for dummy_index in range(3)]
    print "Unsorted string list is\n", test_list
    print "Sorted string list is\n", string_sort(test_list, string_length)


run_example()