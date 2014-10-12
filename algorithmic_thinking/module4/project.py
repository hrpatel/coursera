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

            # matching a "-"
            if char_x == "-" or char_y == "-":
                scoring_matrix[char_x][char_y] = dash_score
            # matching character
            elif char_x == char_y:
                scoring_matrix[char_x][char_y] = diag_score
            # non-matching character
            else:
                scoring_matrix[char_x][char_y] = off_diag_score

    return scoring_matrix


def compute_alignment_matrix(seq_x, seq_y, scoring_matrix, global_flag):
    """
    The function computes and returns the alignment matrix for seq_x and seq_y as described in the Homework. If
    global_flag is True, each entry of the alignment matrix is computed using the method described in Question 8 of the
    Homework. If global_flag is False, each entry is computed using the method described in Question 12 of the Homework

    :rtype : list
    :param seq_x: first sequence
    :param seq_y: second sequence
    :param scoring_matrix: alphabet scoring matrix
    :param global_flag: global or local alignment
    :return: score matrix for aligning both sequences
    """

    # define the size of the DPS matrix
    x_size = len(seq_x) + 1
    y_size = len(seq_y) + 1

    # initialize matrix and set [0][0] = 0
    dps = [[None for dummy_c in range(y_size)] for dummy_r in range(x_size)]
    dps[0][0] = 0

    # set the null match score for seq_x
    for idx in range(1, x_size):
        dps[idx][0] = dps[idx - 1][0] + scoring_matrix[seq_x[idx - 1]]["-"]

        # local matching
        if not global_flag and dps[idx][0] < 0:
            dps[idx][0] = 0

    # set the null match score for seq_y
    for idy in range(1, y_size):
        dps[0][idy] = dps[0][idy - 1] + scoring_matrix["-"][seq_y[idy - 1]]

        # local matching
        if not global_flag and dps[0][idy] < 0:
            dps[0][idy] = 0

    # calculate the rest of the matrix
    for idx in range(1, x_size):
        for idy in range(1, y_size):
            dps[idx][idy] = max(dps[idx - 1][idy - 1] + scoring_matrix[seq_x[idx - 1]][seq_y[idy - 1]],
                                dps[idx - 1][idy] + scoring_matrix[seq_x[idx - 1]]["-"],
                                dps[idx][idy - 1] + scoring_matrix["-"][seq_y[idy - 1]])

            # local matching
            if not global_flag and dps[idx][idy] < 0:
                dps[idx][idy] = 0

    return dps


def compute_global_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """
    This function computes a global alignment of seq_x and seq_y using the global alignment matrix alignment_matrix.

    :rtype : tuple
    :param seq_x: first sequence
    :param seq_y: second sequence to compare
    :param scoring_matrix: scoring matrix for alphabet
    :param alignment_matrix: alignment matrix for the sequences
    :return: a tuple of the form (score, align_x, align_y) where score is the score of the global alignment
    align_x and align_y. Note that align_x and align_y should have the same length and may include the padding
    character '-'
    """
    x_size = len(seq_x)
    y_size = len(seq_y)

    # return variables
    score = alignment_matrix[x_size][y_size]

    align_x = ""
    align_y = ""

    # loop until we exhaust one of the sequences
    while x_size > 0 and y_size > 0:
        # trace back diagonal
        if alignment_matrix[x_size][y_size] == alignment_matrix[x_size - 1][y_size - 1] + \
                scoring_matrix[seq_x[x_size - 1]][seq_y[y_size - 1]]:
            align_x = seq_x[x_size - 1] + align_x
            align_y = seq_y[y_size - 1] + align_y
            x_size += -1
            y_size += -1
        else:
            # trace back up 1 row ("-" in seq_y)
            if alignment_matrix[x_size][y_size] == alignment_matrix[x_size - 1][y_size] + \
                    scoring_matrix[seq_x[x_size - 1]]["-"]:
                align_x = seq_x[x_size - 1] + align_x
                align_y = "-" + align_y
                x_size += -1
            # trace back left one column ("-" in seq_x)
            else:
                align_x = "-" + align_x
                align_y = seq_y[y_size - 1] + align_y
                y_size += -1

    # finish off the rest of the left over string, if any
    while x_size > 0:
        align_x = seq_x[x_size - 1] + align_x
        align_y = "-" + align_y
        x_size += -1

    while y_size > 0:
        align_x = "-" + align_x
        align_y = seq_y[y_size - 1] + align_y
        y_size += -1

    return score, align_x, align_y


def compute_local_alignment(seq_x, seq_y, scoring_matrix, alignment_matrix):
    """
    This function computes a local alignment of seq_x and seq_y using the local alignment matrix alignment_matrix.

    :rtype : tuple
    :param seq_x:
    :param seq_y:
    :param scoring_matrix:
    :param alignment_matrix:
    :return: a tuple of the form (score, align_x, align_y) where score is the score of the optimal local
    alignment align_x and align_y. Note that align_x and align_y should have the same length and may include the padding
    character '-'.
    """
    score = 0
    align_x = ""
    align_y = ""

    return score, align_x, align_y


# print compute_global_alignment('ACTACT',
#                                'AGCTA',
#                                {'A': {'A': 2, 'C': 1, '-': 0, 'T': 1, 'G': 1},
#                                 'C': {'A': 1, 'C': 2, '-': 0, 'T': 1, 'G': 1},
#                                 '-': {'A': 0, 'C': 0, '-': 0, 'T': 0, 'G': 0},
#                                 'T': {'A': 1, 'C': 1, '-': 0, 'T': 2, 'G': 1},
#                                 'G': {'A': 1, 'C': 1, '-': 0, 'T': 1, 'G': 2}},
#                                [[0, 0, 0, 0, 0, 0],
#                                 [0, 2, 2, 2, 2, 2],
#                                 [0, 2, 3, 4, 4, 4],
#                                 [0, 2, 3, 4, 6, 6],
#                                 [0, 2, 3, 4, 6, 8],
#                                 [0, 2, 3, 5, 6, 8],
#                                 [0, 2, 3, 5, 7, 8]])