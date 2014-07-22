"""
Student code for Word Wrangler game
"""

__author__ = 'mamaray'

import math
import poc_wrangler_provided as provided

WORDFILE = "assets_scrabble_words3.txt"


# Functions to manipulate ordered word lists

def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list.

    Returns a new sorted list with the same elements in list1, but
    with no duplicates.

    This function can be iterative.
    """

    if len(list1) == 0:
        return []

    # local variables
    return_list = [list1[0]]
    idx = 1

    # remove duplicates
    for item in list1[1:]:
        if return_list[idx - 1] != item:
            return_list.append(item)
            idx += 1

    return return_list


def intersect(list1, list2):
    """
    Compute the intersection of two sorted lists.

    Returns a new sorted list containing only elements that are in
    both list1 and list2.

    This function can be iterative.
    """

    return_list = []

    # remove duplicates first
    nlist1 = remove_duplicates(list1)
    nlist2 = remove_duplicates(list2)

    # find the intersect set
    for idx in range(len(nlist1)):
        for idy in range(len(nlist2)):
            if nlist1[idx] == nlist2[idy]:
                return_list.append(nlist1[idx])

    return return_list


# Functions to perform merge sort

def merge(list1, list2):
    """
    Merge two sorted lists.

    Returns a new sorted list containing all of the elements that
    are in either list1 and list2.

    This function can be iterative.
    :param list1:
    :param list2:
    """

    return_list = []
    idx, idy = 0, 0

    while idx < len(list1) and idy < len(list2):
        if list1[idx] < list2[idy]:
            return_list.append(list1[idx])
            idx += 1
        else:
            return_list.append(list2[idy])
            idy += 1

    if idx >= len(list1):
        return_list += list2[idy:]
    elif idy >= len(list2):
        return_list += list1[idx:]

    return return_list


def merge_sort(list1):
    """
    Sort the elements of list1.

    Return a new sorted list with the same elements as list1.

    This function should be recursive.
    :param list1:
    """
    if len(list1) == 0:
        return []
    elif len(list1) == 1:
        return list1
    else:
        mid_point = int(math.floor(len(list1) / 2))

        first_half = merge_sort(list1[:mid_point])
        second_half = merge_sort(list1[mid_point:])

        return merge(first_half, second_half)


# Function to generate all strings for the word wrangler game

def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word
    in any order.

    Returns a list of all strings that can be formed from the letters
    in word.

    This function should be recursive.
    :param word:
    """
    return []


# Function to load words from a file

def load_words(filename):
    """
    Load word list from the file named filename.

    Returns a list of strings.
    :param filename:
    """
    return []


def run():
    """
    Run game.
    """
    words = load_words(WORDFILE)
    wrangler = provided.WordWrangler(words, remove_duplicates,
                                     intersect, merge_sort,
                                     gen_all_strings)
    provided.run_game(wrangler)

# Uncomment when you are ready to try the game
# run()

import random
for i in range(10):
    list = [random.randrange(1, 40) for _ in range(0, 15)]

    print list
    print merge_sort(list)
    print
