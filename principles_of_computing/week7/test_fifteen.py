__author__ = 'ray'

import fifteen_puzzle as puz

# Test lower_row_invariant(...)
obj = puz.Puzzle(3, 3, [[8, 7, 6],
                        [5, 4, 3],
                        [2, 1, 0]])
assert obj.lower_row_invariant(2, 2) is True

# Test row0_invariant(...)
obj = puz.Puzzle(3, 3, [[0, 1, 2],
                        [3, 4, 5],
                        [6, 7, 8]])
assert obj.row0_invariant(0) is True


# Test solve_interior_tile(...)
obj = puz.Puzzle(4, 4, [[6, 7, 1, 13],
                        [5, 4, 3, 10],
                        [9, 2, 8, 11],
                        [12, 0, 14, 15]])
print obj
obj.solve_interior_tile(3, 1)
print obj
print

# Test solve_interior_tile(...)
obj = puz.Puzzle(4, 4, [[6, 13, 1, 7],
                        [5, 4, 3, 10],
                        [9, 2, 8, 11],
                        [12, 0, 14, 15]])
print obj
obj.solve_interior_tile(3, 1)
print obj
print

# Test solve_interior_tile(...)
obj = puz.Puzzle(4, 4, [[6, 7, 1, 9],
                        [15, 4, 3, 10],
                        [5, 2, 8, 11],
                        [12, 13, 14, 0]])
print obj
obj.solve_interior_tile(3, 3)
print obj
print

# Test solve_interior_tile(...)
obj = puz.Puzzle(3, 3, [[8, 7, 6],
                        [5, 4, 3],
                        [2, 1, 0]])
print obj
obj.solve_interior_tile(2, 2)
print obj
#obj.solve_interior_tile(2, 1)
#print obj
print


# Test solve_interior_tile(...)
obj = puz.Puzzle(3, 3, [[3, 2, 1],
                        [6, 5, 4],
                        [7, 0, 8]])
print obj
obj.solve_interior_tile(2, 1)
print obj
