__author__ = 'ray'

import fifteen_puzzle as puz

# target top/left
obj = puz.Puzzle(3, 3, [[2, 5, 4],
                        [1, 3, 0],
                        [6, 7, 8]])
print obj
obj.solve_row1_tile(2)
print obj
print


# target above 0
obj = puz.Puzzle(3, 3, [[2, 4, 5],
                        [1, 3, 0],
                        [6, 7, 8]])
print obj
obj.solve_row1_tile(2)
print obj
print


# target left of 0
obj = puz.Puzzle(3, 3, [[2, 3, 4],
                        [1, 5, 0],
                        [6, 7, 8]])
print obj
obj.solve_row1_tile(2)
print obj
print

# target in same row
obj = puz.Puzzle(3, 3, [[1, 2, 4],
                        [5, 3, 0],
                        [6, 7, 8]])
print obj
obj.solve_row1_tile(2)
print obj
print


# target 1 row above
obj = puz.Puzzle(3, 3, [[5, 2, 4],
                        [1, 3, 0],
                        [6, 7, 8]])
print obj
obj.solve_row1_tile(2)
print obj
print


