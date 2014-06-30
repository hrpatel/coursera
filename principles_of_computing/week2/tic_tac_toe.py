"""
Monte Carlo Tic-Tac-Toe Player
"""

__author__ = 'mamaray'

import random
import ttt_provided as provided

# Constants f   or Monte Carlo simulator
# Change as desired
NTRIALS = 1  # Number of trials to run
MCMATCH = 1.0  # Score for squares played by the machine player
MCOTHER = 1.0  # Score for squares played by the other player

# Add your functions here.

def mc_trial(board, player):
    """
    This function takes a current board and the next player to move. The function should play a game starting with the
    given player by making random moves, alternating between players. The function should return when the game is over.
    The modified board will contain the state of the game, so the function does not return anything.

    :param board:
    :param player:
    :return:
    """

    return


def mc_update_scores(scores, board, player):
    """
    This function takes a grid of scores (a list of lists) with the same dimensions as the Tic-Tac-Toe board, a board
    from a completed game, and which player the machine player is. The function should score the completed board and
    update the scores grid. As the function updates the scores grid directly, it does not return anything,

    :param scores:
    :param board:
    :param player:
    :return:
    """

    return


def get_best_move(board, scores):
    """
    This function takes a current board and a grid of scores. The  should find all of the empty squares with the maximum
    score and randomly return one of them as a (row, column) tuple. It is an error to call this function with a board
    that has no empty squares (there is no possible next move), so your function may do whatever it wants in that case.
    The case where the board is full will not be tested.

    :param board:
    :param scores:
    :return:
    """

    return


def mc_move(board, player, trials):
    """
    This function takes a current board, which player the machine player is, and the number of trials to run. The
    function should use the Monte Carlo simulation to return a move for the machine player in the form of a
    (row, column) tuple.

    :param board:
    :param player:
    :param trials:
    :return:
    """

    return


# Lets start the game
board = provided.TTTBoard(5)
print board

provided.play_game(mc_move, NTRIALS, False)
