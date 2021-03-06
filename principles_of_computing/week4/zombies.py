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
        if zombie_list is not None:
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
        visited = [[self._cells[_row][_col] for _col in range(self._grid_width)]
                   for _row in range(self._grid_height)]

        # generate a distance grid with the maximum value
        max_dist = self._grid_height * self._grid_width
        dist_field = [[max_dist for _col in range(self._grid_width)] for _row in range(self._grid_height)]

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
            dist_field[row][col] = 0

        # repeat until we're out of boundary items
        while len(boundry) > 0:
            # get the next item in the boundary
            next_item = boundry.dequeue()

            # get a list of neighbour cells
            neighbours = self.four_neighbors(next_item[0], next_item[1])

            for nghbr in neighbours:
                # update visited
                if visited[nghbr[0]][nghbr[1]] != FULL:
                    visited[nghbr[0]][nghbr[1]] = FULL

                    # add to boundry
                    boundry.enqueue(nghbr)

                    # update distance
                    dist_field[nghbr[0]][nghbr[1]] = min(dist_field[nghbr[0]][nghbr[1]],
                                                         dist_field[next_item[0]][next_item[1]] + 1)

        return dist_field

    def move_humans(self, zombie_distance):
        """
        Function that moves humans away from zombies, diagonal moves are allowed
        """
        self.move_body(zombie_distance, HUMAN)

    def move_zombies(self, human_distance):
        """
        Function that moves zombies towards humans, no diagonal moves are allowed
        """
        self.move_body(human_distance, ZOMBIE)

    def move_body(self, dist_array, entity_type):
        """
        Function that moves humans/zombies
        """

        if entity_type == HUMAN:
            entity_list = self._human_list
            comparison = max
            get_neighbours = self.eight_neighbors
        else:
            entity_list = self._zombie_list
            comparison = min
            get_neighbours = self.four_neighbors

        # make a copy of the list of zombies
        list_copy = list(entity_list)

        # loop through each entity
        for entity in entity_list:
            # get a list of neighbour cells
            neighbours = get_neighbours(entity[0], entity[1])

            # initialize local variables
            best_neighbour = []
            changed = False
            distance = dist_array[entity[0]][entity[1]]

            # calculate the best move
            for neighbour in neighbours:
                if self.is_empty(*neighbour):
                    if comparison(dist_array[neighbour[0]][neighbour[1]], distance) != distance:
                        distance = dist_array[neighbour[0]][neighbour[1]]
                        best_neighbour = [neighbour]
                        changed = True
                    elif dist_array[neighbour[0]][neighbour[1]] == distance:
                        best_neighbour.append(neighbour)

            # we have a move to make
            if changed:
                list_copy[list_copy.index(entity)] = random.choice(best_neighbour)

        # save the modified list into the object
        entity_list[:] = list_copy
