"""
Student code for Word Wrangler game
"""

__author__ = 'mamaray'

import math


def remove_duplicates(list1):
    """
    Eliminate duplicates in a sorted list. Returns a new sorted list with the same elements in list1, but with no
    duplicates. This function can be iterative.

    :param list1: remove duplicate items from this list
    """

    # nothing to do
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
    Compute the intersection of two sorted lists. Returns a new sorted list containing only elements that are in both
    list1 and list2. This function can be iterative.

    :param list1: first list to generate an intersection
    :param list2: second list to generate intersection
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


def merge(list1, list2):
    """
    Merge two sorted lists. Returns a new sorted list containing all of the elements that are in either list1 and list2.
    This function can be iterative.

    :param list1: first list to merge
    :param list2: second list to merge
    """

    # local variables
    return_list = []
    idx, idy = 0, 0

    # exhaust one of the lists
    while idx < len(list1) and idy < len(list2):
        if list1[idx] < list2[idy]:
            return_list.append(list1[idx])
            idx += 1
        else:
            return_list.append(list2[idy])
            idy += 1

    # attach the rest of the other list to the end
    if idx >= len(list1):
        return_list += list2[idy:]
    elif idy >= len(list2):
        return_list += list1[idx:]

    return return_list


def merge_sort(list1):
    """
    Sort the elements of list1. Return a new sorted list with the same elements as list1. This function should be
    recursive.

    :param list1: unsorted list of items to sort
    """

    if len(list1) == 0:
        # base case
        return []
    elif len(list1) == 1:
        # base case
        return list1
    else:
        mid_point = int(math.floor(len(list1) / 2))

        first_half = merge_sort(list1[:mid_point])
        second_half = merge_sort(list1[mid_point:])

        return merge(first_half, second_half)


def gen_all_strings(word):
    """
    Generate all strings that can be composed from the letters in word in any order. Returns a list of all strings that
    can be formed from the letters in word. This function should be recursive.

    :param word: letters of this word to scramble up and return in a list
    """

    if len(word) == 0:
        # base case
        return [""]
    else:
        # split the word
        first = word[0]
        rest = word[1:]

        # get substrings
        rest_strings = gen_all_strings(rest)
        all_strings = list(rest_strings)

        # add the first letters into the list
        for string in rest_strings:
            for idx in range(len(string) + 1):
                all_strings.append(string[:idx] + first + string[idx:])

        return all_strings
