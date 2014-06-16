"""
Clone of 2048 game.
"""
__author__ = "mamaray"


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
        
    def reset(self):
        """
        Reset the game so the grid is empty.
        """
        self._grid = [[0] * self._width] * self._height
        
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
        # replace with your code
        pass
        
    def new_tile(self):
        """
        Create a new tile in a randomly selected empty 
        square.  The tile should be 2 90% of the time and
        4 10% of the time.
        """
        # replace with your code
        pass
        
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

    
poc_2048_gui.run_gui(TwentyFortyEight(4, 4))
