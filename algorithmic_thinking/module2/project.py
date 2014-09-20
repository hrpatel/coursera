"""
module 2 project for algorithmic thinking
"""
__author__ = 'mamaray'

from collections import deque


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

    while queue:
        # pop the next item from the queue
        next_item = queue.pop()

        # iterate through each neighbour of the dequeued node
        for neighbour in ugraph[next_item]:
            if neighbour not in visited:
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
    # start an empty list of connected component
    ccs = []

    # initialize local variable
    remaining_nodes = set(ugraph.keys())

    while remaining_nodes:
        # get all connected nodes of a random node
        visited = bfs_visited(ugraph, remaining_nodes.pop())

        # add to the connected component list
        ccs.append(visited)

        # remove from remaining nodes to check
        remaining_nodes = remaining_nodes.difference(visited)

    return ccs


def largest_cc_size(ugraph):
    """
    a function to get the size of the largest connected component of a graph

    :rtype : int
    :param ugraph: undirected graph
    :return: size (integer) of the largest connected component in ugraph
    """
    max_size = 0

    # get all connected components
    ccs = cc_visited(ugraph)

    # find largest connected component
    for component in ccs:
        dummy_len = len(component)
        if dummy_len > max_size:
            max_size = dummy_len

    return max_size


def compute_resilience(ugraph, attack_order):
    """
    a function to test the resiliency of a graph by removing nodes/edges

    :rtype : list
    :param ugraph:
    :param attack_order:
    :return:
    """
    # get all connected components of ugraph and add to list
    lcc = [largest_cc_size(ugraph)]

    # loop through each attack
    for attack in attack_order:
        # remove the node
        edges = ugraph.pop(attack)

        # remove edges from other nodes
        for node in edges:
            ugraph[node].discard(attack)

        # calculate largest connected component
        lcc.append(largest_cc_size(ugraph))

    return lcc


# import cProfile, pstats, StringIO
# pr = cProfile.Profile()
# pr.enable()
#
# import alg_project2_graphs as data
# print compute_resilience(data.GRAPH2, [1, 3, 5, 7, 2, 4, 6, 8])
# print compute_resilience(data.GRAPH7, [1, 3, 5, 7, 2, 4, 9, 11, 23, 12, 6, 8])
# print compute_resilience(data.GRAPH3, [1, 3])
# print compute_resilience(data.GRAPH0, [1, 2])
#
# pr.disable()
# s = StringIO.StringIO()
# ps = pstats.Stats(pr, stream=s)
# ps.print_stats()
# print s.getvalue()
