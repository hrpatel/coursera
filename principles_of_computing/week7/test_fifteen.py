__author__ = 'ray'

import fifteen_puzzle as puz

# Test lower_row_invariant(...)
obj = puz.Puzzle(3, 3, [[8, 7, 6],
                        [5, 4, 3],
                        [2, 1, 0]])
assert obj.lower_row_invariant(2, 2) is True

# Test solve_interior_tile(...)
obj = puz.Puzzle(3, 3, [[0, 1, 2],
                        [3, 4, 5],
                        [6, 7, 8]])
assert obj.row0_invariant(0) is True