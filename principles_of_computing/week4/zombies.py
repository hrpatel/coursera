"""
Student portion of Zombie Apocalypse mini-project
"""

__author__ = 'mamaray'

import random
import poc_grid
import poc_queue

# global constants
EMPTY = 0
FULL = 1
FOUR_WAY = 0
EIGHT_WAY = 1
OBSTACLE = "obstacle"
HUMAN = "human"
ZOMBIE = "zombie"


class Zombie(poc_grid.Grid):
    """
    Class for simulating zombie pursuit of human on grid with obstacles
    """

    def __init__(self, grid_height, grid_width, obstacle_list=None, zombie_list=None, human_list=None):
        """
        Create a simulation of given size with given obstacles, humans, and zombies
        """
        poc_grid.Grid.__init__(self, grid_height, grid_width)
        if obstacle_list != None:
            for cell in obstacle_list:
                self.set_full(cell[0], cell[1])
        if zombie_list != None:
            self._zombie_list = list(zombie_list)
        else:
            self._zombie_list = []
        if human_list != None:
            self._human_list = list(human_list)
        else:
            self._human_list = []

    def clear(self):
        """
        Set cells in obstacle grid to be empty, Reset zombie and human lists to be empty
        """

        # clear the cells
        poc_grid.Grid.clear(self)

        # clear the human and zombie lists
        self._zombie_list = []
        self._human_list = []

    def add_zombie(self, row, col):
        """
        Add zombie to the zombie list
        """
        self._zombie_list.append((row, col))

    def num_zombies(self):
        """
        Return number of zombies
        """
        return len(self._zombie_list)

    def zombies(self):
        """
        Generator that yields the zombies in the order they were added.
        """
        for zombie in self._zombie_list:
            yield zombie

    def add_human(self, row, col):
        """
        Add human to the human list
        """
        self._human_list.append((row, col))

    def num_humans(self):
        """
        Return number of humans
        """
        return len(self._human_list)

    def humans(self):
        """
        Generator that yields the humans in the order they were added.
        """
        for human in self._human_list:
            yield human

    def compute_distance_field(self, entity_type):
        """
        Function computes a 2D distance field. Distance at member of entity_queue is zero. Shortest paths avoid
        obstacles and use distance_type distances
        """

        # initialize visited cells based on FULL cells
        visited = []
        for dummy_row in range(self._grid_height):
            tmp_row = []
            for dummy_col in range(self._grid_width):
                tmp_row.append(self._cells[dummy_row][dummy_col])
            visited.append(tmp_row)

        # generate a distance grid with the maximum value
        distance_field = []
        for dummy_row in range(self._grid_height):
            distance_field.append([self._grid_height * self._grid_width for dummy_col in range(self._grid_width)])

        # start a new queue
        boundry = poc_queue.Queue()
        if entity_type == ZOMBIE:
            for zombie in self._zombie_list:
                boundry.enqueue(zombie)
        else:
            for human in self._human_list:
                boundry.enqueue(human)

        # initialize the grids
        for row, col in boundry:
            visited[row][col] = FULL
            distance_field[row][col] = 0

        # repeat until we're out of boundary items
        while len(boundry) > 0:
            # get the next item in the boundary
            current_item = boundry.dequeue()

            # get a list of neighbour cells
            neighbours = self.four_neighbors(current_item[0], current_item[1])

            for neighbour in neighbours:
                # update visited
                if visited[neighbour[0]][neighbour[1]] != FULL:
                    visited[neighbour[0]][neighbour[1]] = FULL

                    # add to boundry
                    boundry.enqueue(neighbour)

                    # update distance
                    distance_field[neighbour[0]][neighbour[1]] = min(distance_field[neighbour[0]][neighbour[1]],
                                                                     distance_field[current_item[0]][
                                                                         current_item[1]] + 1)

        return distance_field

    def move_humans(self, zombie_distance):
        """
        Function that moves humans away from zombies, diagonal moves are allowed
        """

        list_copy = list(self._human_list)

        # loop through each human
        for human in self._human_list:
            # get a list of neighbour cells
            neighbours = self.eight_neighbors(human[0], human[1])

            changed = False
            max_distance = zombie_distance[human[0]][human[1]]
            best_neighbour = None
            for neighbour in neighbours:
                if zombie_distance[neighbour[0]][neighbour[1]] >= max_distance:
                    max_distance = zombie_distance[neighbour[0]][neighbour[1]]
                    best_neighbour = neighbour
                    changed = True

            if changed:
                idx = list_copy.index(human)
                list_copy[idx] = best_neighbour

        self._human_list = list_copy

    def move_zombies(self, human_distance):
        """
        Function that moves zombies towards humans, no diagonal moves are allowed
        """

        list_copy = list(self._zombie_list)

        # loop through each zombie
        for zombie in self._zombie_list:
            # get a list of neighbour cells
            neighbours = self.four_neighbors(zombie[0], zombie[1])

            changed = False
            min_distance = human_distance[zombie[0]][zombie[1]]
            best_neighbour = None
            for neighbour in neighbours:
                if human_distance[neighbour[0]][neighbour[1]] <= min_distance:
                    min_distance = human_distance[neighbour[0]][neighbour[1]]
                    best_neighbour = neighbour
                    changed = True

            if changed:
                idx = list_copy.index(zombie)
                list_copy[idx] = best_neighbour

        self._zombie_list = list_copy
