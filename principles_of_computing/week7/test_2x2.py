__author__ = 'ray'

import fifteen_puzzle as puz

obj = puz.Puzzle(3, 3, [[4, 3, 2],
                        [1, 0, 5],
                        [6, 7, 8]])
print obj
obj.solve_2x2()
print obj
print


