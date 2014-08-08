__author__ = 'ray'

import fifteen_puzzle as puz

# Test solve_col0_tile(...)
obj = puz.Puzzle(3, 3, [[8, 7, 6],
                        [5, 4, 3],
                        [2, 1, 0]])
print "------------"
print obj
obj.solve_interior_tile(2, 2)
print obj
obj.solve_interior_tile(2, 1)
print obj
obj.solve_col0_tile(2)
print obj
print


# Test solve_col0_tile(...)
obj = puz.Puzzle(3, 3, [[3, 2, 1],
                        [6, 5, 4],
                        [0, 7, 8]])
print "------------"
print obj
obj.solve_col0_tile(2)
print obj
print


# Test solve_col0_tile(...)
obj = puz.Puzzle(4, 4, [[6, 7, 1, 13],
                        [5, 4, 3, 10],
                        [9, 2, 8, 11],
                        [12, 0, 14, 15]])
print "------------"
print obj
obj.solve_interior_tile(3, 1)
print obj
obj.solve_col0_tile(3)
print obj
print


# Test solve_col0_tile(...)
obj = puz.Puzzle(4, 4, [[11, 7, 1, 6],
                        [5, 4, 3, 2],
                        [9, 10, 8, 12],
                        [0, 13, 14, 15]])
print "------------"
print obj
obj.solve_col0_tile(3)
print obj