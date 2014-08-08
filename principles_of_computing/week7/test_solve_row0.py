__author__ = 'ray'

import fifteen_puzzle as puz

# target is beside/left of 0
obj = puz.Puzzle(3, 3, [[4, 2, 0],
                        [1, 3, 5],
                        [6, 7, 8]])
print "----------"
print obj
obj.solve_row0_tile(2)
print obj



# target is 1 row down and more than 2 col away
obj = puz.Puzzle(3, 3, [[4, 1, 0],
                        [2, 3, 5],
                        [6, 7, 8]])
print "----------"
print obj
obj.solve_row0_tile(2)
print obj


# target is 1 row down, 1 col away
obj = puz.Puzzle(3, 3, [[4, 1, 0],
                        [3, 2, 5],
                        [6, 7, 8]])
print "----------"
print obj
obj.solve_row0_tile(2)
print obj

# target in same row
obj = puz.Puzzle(3, 3, [[2, 1, 0],
                        [4, 3, 5],
                        [6, 7, 8]])
print "----------"
print obj
obj.solve_row0_tile(2)
print obj


# target is 1 row down and more than 2 col away
obj = puz.Puzzle(4, 5, [[7, 6, 5, 3, 0],
                        [4, 8, 2, 1, 9],
                        [10, 11, 12, 13, 14],
                        [15, 16, 17, 18, 19]]   )
print "----------"
print obj
obj.solve_row0_tile(4)
print obj


# target is 1 row down and more than 2 col away
obj = puz.Puzzle(4, 5, [[4, 6, 5, 3, 0],
                        [7, 8, 2, 1, 9],
                        [10, 11, 12, 13, 14],
                        [15, 16, 17, 18, 19]])
print "----------"
print obj
obj.solve_row0_tile(4)
print obj


