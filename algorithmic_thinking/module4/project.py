"""
In Project 4, we will implement four functions. The first pair of functions will return matrices that we will use in
computing the alignment of two sequences. The second pair of functions will return global and local alignments of two
input sequences based on a provided alignment matrix. You will then use these functions in Application 4 to analyze two
problems involving comparison of similar sequences.
"""
__author__ = 'mamaray'


def build_scoring_matrix(alphabet, diag_score, off_diag_score, dash_score):
    """
    The function returns a dictionary of dictionaries whose entries are indexed by pairs of characters in alphabet plus
    '-'.The score for any entry indexed by one or more dashes is dash_score. The score for the remaining diagonal
    entries is diag_score. Finally, the score for the remaining off-diagonal entries is off_diag_score.

    :rtype : dict
    :param alphabet: characters in alphabet
    :param diag_score: matching score
    :param off_diag_score: non-matching score
    :param dash_score: null/dash matching score
    """

    scoring_matrix = {}

    for char_x in alphabet:
        scoring_matrix[char_x] = {}

        for char_y in alphabet:

            # match
            if char_x == "-" or char_y == "-":
                scoring_matrix[char_x][char_y] = dash_score

            elif char_x == char_y:
                scoring_matrix[char_x][char_y] = diag_score

            else:
                scoring_matrix[char_x][char_y] = off_diag_score

            print char_x, char_y, scoring_matrix[char_x][char_y]

    return scoring_matrix

# build_scoring_matrix(set(['A', 'C', '-', 'T', 'G']), 6, 2, -4)
# a = {'A': {'A': 6, 'C': 2, '-': -4, 'T': 2, 'G': 2}, 'C': {'A': 2, 'C': 6, '-': -4, 'T': 2, 'G': 2}, '-': {'A': -4, 'C': -4, '-': -4, 'T': -4, 'G': -4}, 'T': {'A': 2, 'C': 2, '-': -4, 'T': 6, 'G': 2}, 'G': {'A': 2, 'C': 2, '-': -4, 'T': 2, 'G': 6}}
# b = {'A': {'A': 6, 'C': 2, '-': -4, 'T': 2, 'G': 2}, 'C': {'A': 2, 'C': 6, '-': -4, 'T': 2, 'G': 2}, '-': {'A': -4, 'C': -4, '-': 6, 'T': -4, 'G': -4}, 'T': {'A': 2, 'C': 2, '-': -4, 'T': 6, 'G': 2}, 'G': {'A': 2, 'C': 2, '-': -4, 'T': 2, 'G': 6}}