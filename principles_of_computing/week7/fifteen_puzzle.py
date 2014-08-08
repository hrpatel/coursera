"""
Loyd's Fifteen puzzle - solver and visualizer
Note that solved configuration has the blank (zero) tile in upper left
Use the arrows key to swap this tile with its neighbors
"""

__author__ = 'ray'


class Puzzle:
    """
    Class representation for the Fifteen puzzle
    """

    def __init__(self, puzzle_height, puzzle_width, initial_grid=None):
        """
        Initialize puzzle with default height and width
        Returns a Puzzle object
        """
        self._height = puzzle_height
        self._width = puzzle_width
        self._grid = [[col + puzzle_width * row
                       for col in range(self._width)]
                      for row in range(self._height)]

        if initial_grid is not None:
            for row in range(puzzle_height):
                for col in range(puzzle_width):
                    self._grid[row][col] = initial_grid[row][col]

    def __str__(self):
        """
        Generate string representaion for puzzle
        Returns a string
        """
        ans = ""
        for row in range(self._height):
            ans += str(self._grid[row])
            ans += "\n"
        return ans

    # ####################################
    # GUI methods

    def get_height(self):
        """
        Getter for puzzle height
        Returns an integer
        """
        return self._height

    def get_width(self):
        """
        Getter for puzzle width
        Returns an integer
        """
        return self._width

    def get_number(self, row, col):
        """
        Getter for the number at tile position pos
        Returns an integer
        """
        return self._grid[row][col]

    def set_number(self, row, col, value):
        """
        Setter for the number at tile position pos
        """
        self._grid[row][col] = value

    def clone(self):
        """
        Make a copy of the puzzle to update during solving
        Returns a Puzzle object
        """
        new_puzzle = Puzzle(self._height, self._width, self._grid)
        return new_puzzle

    # #######################################################
    # Core puzzle methods

    def current_position(self, solved_row, solved_col):
        """
        Locate the current position of the tile that will be at
        position (solved_row, solved_col) when the puzzle is solved
        Returns a tuple of two integers
        """
        solved_value = (solved_col + self._width * solved_row)

        for row in range(self._height):
            for col in range(self._width):
                if self._grid[row][col] == solved_value:
                    return row, col
        assert False, "Value " + str(solved_value) + " not found"

    def update_puzzle(self, move_string):
        """
        Updates the puzzle state based on the provided move string
        """
        zero_row, zero_col = self.current_position(0, 0)
        for direction in move_string:
            if direction == "l":
                assert zero_col > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col - 1]
                self._grid[zero_row][zero_col - 1] = 0
                zero_col -= 1
            elif direction == "r":
                assert zero_col < self._width - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row][zero_col + 1]
                self._grid[zero_row][zero_col + 1] = 0
                zero_col += 1
            elif direction == "u":
                assert zero_row > 0, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row - 1][zero_col]
                self._grid[zero_row - 1][zero_col] = 0
                zero_row -= 1
            elif direction == "d":
                assert zero_row < self._height - 1, "move off grid: " + direction
                self._grid[zero_row][zero_col] = self._grid[zero_row + 1][zero_col]
                self._grid[zero_row + 1][zero_col] = 0
                zero_row += 1
            else:
                assert False, "invalid direction: " + direction

    ##################################################################
    # Phase one methods

    def lower_row_invariant(self, target_row, target_col):
        """
        Check whether the puzzle satisfies the specified invariant
        at the given position in the bottom rows of the puzzle (target_row > 1)
        Returns a boolean
        """

        # check if the target position is a 0
        if self.get_number(target_row, target_col) != 0:
            return False

        # check the rest of the row
        for col in xrange(target_col + 1, self.get_width()):
            expected_val = (col + self._width * target_row)
            if self.get_number(target_row, col) != expected_val:
                return False

        # check the rest of the grid
        for row in xrange(target_row + 1, self._height):
            for col in xrange(self._width):
                expected_val = (col + self._width * row)
                if self.get_number(row, col) != expected_val:
                    return False

        return True

    def solve_interior_tile(self, target_row, target_col):
        """
        Place correct tile at target position
        Updates puzzle and returns a move string
        """

        # initialize local variables
        move = ""

        target_cur_pos = self.current_position(target_row, target_col)
        zero_pos = self.current_position(0, 0)
        #print 'target', target_cur_pos
        #print "zero", zero_pos

        # move 0 to the same row as the target
        move += "u" * (zero_pos[0] - target_cur_pos[0])

        # calculate any left or right moves
        left_right = target_cur_pos[1] - zero_pos[1]
        #print "left/right", left_right
        if left_right < 0:
            # move 0 left
            #print "move target right", left_right * -1
            move += "l" * (left_right * -1)
            # continue moving target right
            move += "drrul" * ((-1 * left_right) - 1)
            # move 0 around ttarget moving it down
            move += "druld" * (zero_pos[0] - target_cur_pos[0])
        elif left_right > 0:
            # move 0 right
            #print "move target left", left_right
            move += "r" * left_right
            # continue moving target left
            move += "dllur" * (left_right - 1)
            # move 0 down, left, up over target
            move += "dlu"
            # continue moving target down
            move += "lddru" * (zero_pos[0] - target_cur_pos[0] - 1)
            # move 0 left, down beside target
            move += "ld"
        elif left_right is 0:
            # target is below zero now
            #print "move target down"
            # continue moving target down
            move += "lddru" * (zero_pos[0] - target_cur_pos[0] - 1)
            # move 0 left, down beside target
            move += "ld"

        print "move", move
        self.update_puzzle(move)
        return move

    def solve_col0_tile(self, target_row):
        """
        Solve tile in column zero on specified row (> 1)
        Updates puzzle and returns a move string
        """

        # initialize local variables
        move = ""

        target_cur_pos = self.current_position(target_row, 0)
        zero_pos = self.current_position(0, 0)
        print 'target', target_cur_pos
        print "zero", zero_pos

        # special case
        if (target_cur_pos[0] == zero_pos[0] -1) and \
                (target_cur_pos[1] == zero_pos[1]  + 1):
            move += "u"
            move += "ruldrdlurdluurddlu"
            move += "r" * (self._width - 1)

            print "move", move
            self.update_puzzle(move)
            return move

        # target is in the same column as 0
        if target_cur_pos[1] == zero_pos[1]:
            up_down = zero_pos[0] - target_cur_pos[0]

            # move up all the way
            move += "u" * up_down

            if up_down > 1:
                # continue moving down
                move += "rddlu" * (up_down - 2)

                # move into position for 3x2 move
                move += "rdl"
                move += "ruldrdlurdluurddlu"

            move += "r" * (self._width - 1)

            print "move", move
            self.update_puzzle(move)
            return move

        # target is at least 2 rows above
        if target_cur_pos[0] <= zero_pos[0] - 2:
            # go up and right
            up_down = zero_pos[0] - target_cur_pos[0]
            # move up all the way
            move += "u" * up_down

            left_right = target_cur_pos[1] - zero_pos[1]
            move += "r" * left_right

            # continue moving target left
            move += "dllur" * (left_right - 1)
            # move 0 over target in col 0
            move += "dlu"

            # continue moving down
            move += "rddlu" * (up_down - 2)

            # move into position for 3x2 move
            move += "rdl"
            move += "ruldrdlurdluurddlu"
            move += "r" * (self._width - 1)

            print "move", move
            self.update_puzzle(move)
            return move

        # target is 1 row above more than 2 col over
        if target_cur_pos[0] == zero_pos[0] - 1:
            # go up and right
            up_down = zero_pos[0] - target_cur_pos[0]
            # move up all the way
            move += "u" * up_down

            left_right = target_cur_pos[1] - zero_pos[1]
            move += "r" * left_right

            # continue moving target left
            move += "ulldr" * (left_right - 1)

            # move into position for 3x2 move
            move += "l"
            move += "ruldrdlurdluurddlu"
            move += "r" * (self._width - 1)

            print "move", move
            self.update_puzzle(move)
            return move

    #############################################################
    # Phase two methods

    def row0_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row zero invariant
        at the given column (col > 1)
        Returns a boolean
        """

        # check if the target position is a 0
        if self.get_number(0, target_col) != 0:
            return False

        # check the rest of the 1st row
        for col in xrange(target_col + 1, self.get_width()):
            if self.get_number(0, col) != col:
                return False

        # check the 2nd row
        for col in xrange(target_col, self.get_width()):
            expected_val = (col + self._width * 1)
            if self.get_number(1, col) != expected_val:
                return False

        # check the rest of the grid
        for row in xrange(2, self._height):
            for col in xrange(self._width):
                expected_val = (col + self._width * row)
                if self.get_number(row, col) != expected_val:
                    return False

        return True

    def row1_invariant(self, target_col):
        """
        Check whether the puzzle satisfies the row one invariant
        at the given column (col > 1)
        Returns a boolean
        """

        # check if the target position is a 0
        if self.get_number(1, target_col) != 0:
            return False

        # check the rest of the row
        for col in xrange(target_col + 1, self.get_width()):
            expected_val = (col + self._width * 1)
            if self.get_number(1, col) != expected_val:
                return False

        # check the rest of the grid
        for row in xrange(2, self._height):
            for col in xrange(self._width):
                expected_val = (col + self._width * row)
                if self.get_number(row, col) != expected_val:
                    return False

        return True

    def solve_row0_tile(self, target_col):
        """
        Solve the tile in row zero at the specified column
        Updates puzzle and returns a move string
        """

        # initialize local variables
        move = ""

        target_cur_pos = self.current_position(0, target_col)
        zero_pos = self.current_position(0, 0)
        print 'target', target_cur_pos
        print "zero", zero_pos

        # target is beside/left of 0
        if (target_cur_pos[0] == zero_pos[0]) and \
                (target_cur_pos[1] == zero_pos[1] - 1):
            move += "ld"

            print "move", move
            self.update_puzzle(move)
            return move

        # target is 1 row down and more than 2 col away
        if (target_cur_pos[0] == zero_pos[0] + 1) and \
                (target_cur_pos[1] <= zero_pos[1] - 2):
            move += "ld"

            left_right = zero_pos[1] - target_cur_pos[1]
            move += "l" * (left_right - 1)

            if left_right > 2:
                # continue moving target left
                move += "urrdl" * (left_right - 2)

            move += "urdlurrdluldrruld"

            print "move", move
            self.update_puzzle(move)
            return move

        # target is 1 row down, 1 col away
        if (target_cur_pos[0] == zero_pos[0] + 1) and \
                (target_cur_pos[1] == zero_pos[1] - 1):
            move += "lld"
            move += "urdlurrdluldrruld"

            print "move", move
            self.update_puzzle(move)
            return move

        # target is 1 row down and more than 2 col away
        if (target_cur_pos[0] == zero_pos[0]) and \
                (target_cur_pos[1] <= zero_pos[1] - 2):
            #move += "ld"

            left_right = zero_pos[1] - target_cur_pos[1]
            move += "l" * (left_right - 1)

            # put target on second row, 2nd col
            move += "dlurdl"

            if left_right > 2:
                # continue moving target left
                move += "urrdl" * (left_right - 2)

            move += "urdlurrdluldrruld"

            print "move", move
            self.update_puzzle(move)
            return move


    def solve_row1_tile(self, target_col):
        """
        Solve the tile in row one at the specified column
        Updates puzzle and returns a move string
        """

        # initialize local variables
        move = ""

        target_cur_pos = self.current_position(1, target_col)
        zero_pos = self.current_position(0, 0)
        print 'target', target_cur_pos
        print "zero", zero_pos

        # target is above 0
        if (target_cur_pos[0] == zero_pos[0] - 1) and \
                (target_cur_pos[1] == zero_pos[1]):
            move += "u"

            print "move", move
            self.update_puzzle(move)
            return move

        # target top/left of 0
        if (target_cur_pos[0] == zero_pos[0] - 1) and \
                (target_cur_pos[1] == zero_pos[1] - 1):
            move += "uldru"

            print "move", move
            self.update_puzzle(move)
            return move

        # target left of 0
        if (target_cur_pos[0] == zero_pos[0]) and \
                (target_cur_pos[1] == zero_pos[1] - 1):
            move += "lur"

            print "move", move
            self.update_puzzle(move)
            return move

        # target same row
        if (target_cur_pos[0] == zero_pos[0]):

            left_right = zero_pos[1] - target_cur_pos[1]
            move += "l" * left_right

            # continue moving target right
            move += "urrdl" * (left_right - 1)
            # finish off the move
            move += "ur"

            print "move", move
            self.update_puzzle(move)
            return move

        # target 1 row above row
        if (target_cur_pos[0] == zero_pos[0] - 1):
            # we know its only 1 row up
            move += "u"

            left_right = zero_pos[1] - target_cur_pos[1]
            move += "l" * left_right

            # continue moving target right
            move += "drrul" * (left_right - 1)
            # finish off move
            move += "dru"

            print "move", move
            self.update_puzzle(move)
            return move




    ###########################################################
    # Phase 3 methods

    def solve_2x2(self):
        """
        Solve the upper left 2x2 part of the puzzle
        Updates the puzzle and returns a move string
        """

        # local variables
        move = ""

        zero_pos = self.current_position(0, 0)
        print "zero", zero_pos

        # move 0 to corner
        move += "u" * zero_pos[1]
        move += "l" * zero_pos[0]

        move += "drul"

        print "move", move
        self.update_puzzle(move)
        return move

    def solve_puzzle(self):
        """
        Generate a solution string for a puzzle
        Updates the puzzle and returns a move string
        """
        # replace with your code
        return ""
