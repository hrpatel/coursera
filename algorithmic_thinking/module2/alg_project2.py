"""
module 2 project for algorithmic thinking
"""

__author__ = 'mamaray'

from collections import deque
import random
# import alg_project2_graphs as data

def bfs_visited(ugraph, start_node):
    """
    a function to get the set consisting of all nodes that are visited by a given node

    :rtype : set
    :param ugraph: undirected graph
    :param start_node: starting node
    :return: the set consisting of all nodes that are visited by a breadth-first search that starts at start_node
    """
    # stores all visited nodes
    visited = set()
    visited.add(start_node)

    # initialize the queue with the current element
    queue = deque()
    queue.append(start_node)

    while len(queue) > 0:
        # pop the next item from the queue
        next_item = queue.pop()

        # iterate through each neighbour of the dequed node
        for neighbour in ugraph[next_item]:
            if not visited.__contains__(neighbour):
                # add to visited and queue so it gets inspected
                visited.add(neighbour)
                queue.append(neighbour)

    return visited


def cc_visited(ugraph):
    """
    a function to get the set of connected components of a given graph

    :rtype : list
    :param ugraph: undirected graph
    :return: list of connected components of ugraph
    """
    #start a list of connected component
    ccs = []

    # initialize local variable
    remaining_nodes = ugraph.keys()

    while len(remaining_nodes) > 0:
        node = random.choice(remaining_nodes)

        visited = bfs_visited(ugraph, node)

        ccs.append(visited)

        for item in visited:
            remaining_nodes.remove(item)

    return ccs


def largest_cc_size(ugraph):
    """
    a function to get the size of the largest connected component of a graph

    :rtype : int
    :param ugraph: undirected graph
    :return: size (integer) of the largest connected component in ugraph
    """
    max_size = -1

    # get all connected components
    ccs = cc_visited(ugraph)

    for component in ccs:
        if len(component) > max_size:
            max_size = len(component)

    return max_size


# print cc_visited(data.GRAPH0)
#
# print cc_visited(data.GRAPH4)
# print largest_cc_size(data.GRAPH4)
