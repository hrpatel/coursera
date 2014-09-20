__author__ = 'ray'

import random


def generate_random_ugraph(num_nodes, probability):
    """
    This function will generate a random graph based on a probability (ER graph, directed)

    :rtype : dict
    :param num_nodes: number of nodes in the generated graph
    :param probability: probability of creating a new node
    :return: a dictionary object representing a graph
    """
    graph = {}
    for itr in xrange(num_nodes):
        graph[itr] = set()

    tracker = range(num_nodes)

    # loop through each node
    for node_x in xrange(num_nodes):
        tracker.remove(node_x)

        for node_y in tracker:
            if random.random() < probability:
                graph[node_x].add(node_y)
                graph[node_y].add(node_x)

    return graph


print generate_random_ugraph(10, 0.5)