"""
Mini-max Tic-Tac-Toe Player
"""
import random

__author__ = 'ray'

import poc_ttt_provided as provided

# SCORING VALUES - DO NOT MODIFY
SCORES = {provided.PLAYERX: 1,
          provided.DRAW: 0,
          provided.PLAYERO: -1}


def mm_move(board, player):
    """
    Make a move on the board.

    Returns a tuple with two elements.  The first element is the score
    of the given board and the second element is the desired move as a
    tuple, (row, col).
    """
    assert isinstance(board, provided.TTTBoard)

    winner = board.check_win()
    if winner is not None:
        return SCORES[winner], (-1, -1)
    else:
        point = -100
        cumulative = {}

        moves = board.get_empty_squares()
        random.shuffle(moves)
        for move in moves:
            trial_board = board.clone()
            trial_board.move(move[0], move[1], player)
            point = (mm_move(trial_board, provided.switch_player(player)))[0]
            cumulative[point] = move

            if player == provided.PLAYERX and point == 1:
                break
            elif player == provided.PLAYERO and point == -1:
                break

        if player == provided.PLAYERX:
            max_move = max(cumulative.keys())
            return max_move, cumulative[max_move]
        else:
            min_move = min(cumulative.keys())
            return min_move, cumulative[min_move]


def move_wrapper(board, player, trials):
    """
    Wrapper to allow the use of the same infrastructure that was used
    for Monte Carlo Tic-Tac-Toe.
    """
    move = mm_move(board, player)

    assert move[1] != (-1, -1), "returned illegal move (-1, -1)"
    return move[1]

# Test game with the console or the GUI.
# Uncomment whichever you prefer.
# Both should be commented out when you submit for
# testing to save time.

# provided.play_game(move_wrapper, 1, False)
