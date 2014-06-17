"""
Clone of 2048 game.
"""
__author__ = "mamaray"


import random
import poc_2048_gui        

# Directions, DO NOT MODIFY
UP = 1
DOWN = 2
LEFT = 3
RIGHT = 4

# Offsets for computing tile indices in each direction.
# DO NOT MODIFY this dictionary.    
OFFSETS = {UP: (1, 0), 
           DOWN: (-1, 0), 
           LEFT: (0, 1), 
           RIGHT: (0, -1)} 
   
def merge(line):
    """
    Helper function that merges a single row or column in 2048
    """
    # return line and merge tracker
    rline = [0] * len(line)
    merged = [False] * len(line)
    
    # move all the values to the "top" of the line and merge
    itr = 0
    for value in line:
        if value != 0:
            if itr > 0 and value == rline[itr - 1] and not merged[itr - 1]:
                rline[itr - 1] += value
                merged[itr - 1] = True
            else:
                rline[itr] = value
                itr += 1
    
    # return the new list
    return rline


class TwentyFortyEight:
    """
    Class to run the game logic.
    """

    def __init__(self, grid_height, grid_width):
        """
        Setup a new board.
        """
        self._height = grid_height
        self._width = grid_width
        
        # reset the grid
        self.reset()
        
        # precompute the indices for directions
        self._indices = { UP: [[0, col] for col in range(self._width)],
                          DOWN: [[self._height - 1, col] for col in range(self._width)],
                          LEFT: [[row, 0] for row in range(self._height)],
                          RIGHT: [[row, self._width - 1] for row in range(self._height)]
                         }
        
        # precompile the length of each direction of move
        self._dir_len = { UP: self._height,
                          DOWN: self._height,
                          LEFT: self._width,
                          RIGHT: self._width
                         }

    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        self._grid = [[0 for dummy_col in range(self._width)] for dummy_row in range(self._height)]
        
    def __str__(self):
        """
        Return a string representation of the grid for debugging.
        """
        output = "[\n"
        for row in range(self._height):
            output += " " + str(self._grid[row]) + "\n"
        output += "]"
        
        return output

    def get_grid_height(self):
        """
        Get the height of the board.
        """
        return self._height
    
    def get_grid_width(self):
        """
        Get the width of the board.
        """
        return self._width
                            
    def move(self, direction):
        """
        Move all tiles in the given direction and add
        a new tile if any tiles moved.
        """
        # helper variable
        need_new_tile = False
        
        for index in self._indices[direction]:
            # helper variables
            line = []
            coords = []
            
            # figure how whats being merged
            for itr in range(self._dir_len[direction]):
                row = index[0] + itr * OFFSETS[direction][0]
                col = index[1] + itr * OFFSETS[direction][1]
                
                # store the list of coordinates and values
                coords.append([row, col])
                line.append(self._grid[row][col])

            # Merge the line
            merged_line = merge(line)
            
            for itr in range(len(merged_line)):
                if merged_line[itr] != line[itr]:
                    need_new_tile = True

            # put the new line back into the grid
            for coord in coords:
                self._grid[coord[0]][coord[1]] = merged_line.pop(0)
                
        # do we need a new tile:
        if need_new_tile:
            self.new_tile()
            
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty 
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # Find an empty cell ("0")
        cell_value = -1
        while cell_value != 0:
            rrow = random.randrange(0, self._height)
            rcol = random.randrange(0, self._width)
            cell_value = self._grid[rrow][rcol]
        
        # Assign a value to it
        if random.randrange(0, 10) > 0:
            self.set_tile(rrow, rcol, 2)
        else:
            self.set_tile(rrow, rcol, 4)
        
    def set_tile(self, row, col, value):
        """
        Set the tile at position row, col to have the given value.
        """
        self._grid[row][col] = value

    def get_tile(self, row, col):
        """
        Return the value of the tile at position row, col.
        """        
        return self._grid[row][col]

    
poc_2048_gui.run_gui(TwentyFortyEight(6, 7))
