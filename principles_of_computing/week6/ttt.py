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

    winner = board.check_win()
    if winner is not None:
        # base case
        return SCORES[winner], (-1, -1)
    else:
        # initialize local variables
        all_moves = {}

        # get the list of next possible moves
        moves = board.get_empty_squares()
        random.shuffle(moves)

        # calculate points for each move
        for row, col in moves:
            # copy the board before sending it off
            trial_board = board.clone()
            trial_board.move(row, col, player)

            # make a dictionary of points/moves
            next_player = provided.switch_player(player)
            score = (mm_move(trial_board, next_player))[0]

            # multiple by SCORES so we only need to check max(...)
            all_moves[score * SCORES[player]] = row, col

            # we've maximized the score (best move at this point), so quit the loop
            if score == SCORES[player]:
                break

        # return the best scoring move
        best_move = max(all_moves)
        return best_move * SCORES[player], all_moves[best_move]


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
