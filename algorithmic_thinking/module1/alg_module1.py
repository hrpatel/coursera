"""
Algorithmic Thinking - Module 1 Project
"""
__author__ = 'mamaray'

import random
import DPATrial as dpat

# Example graph objects
EX_GRAPH0 = {0: set([1, 2]),
             1: set([]),
             2: set([])}

EX_GRAPH1 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3]),
             3: set([0]),
             4: set([1]),
             5: set([2]),
             6: set([])}

EX_GRAPH2 = {0: set([1, 4, 5]),
             1: set([2, 6]),
             2: set([3, 7]),
             3: set([7]),
             4: set([1]),
             5: set([2]),
             6: set([]),
             7: set([3]),
             8: set([1, 2]),
             9: set([0, 3, 4, 5, 6, 7])}


def make_complete_graph(num_nodes):
    """
    Return a graph object (dictionary) with all possible edges..

    :rtype : graph object (dictionary)
    :param num_nodes: number of nodes in the (complete) graph
    """

    graph = {}
    tmp = range(num_nodes)
    for ctr in xrange(num_nodes):
        graph[ctr] = set(tmp)
        graph[ctr].remove(ctr)

    return graph


def compute_in_degrees(digraph):
    """
    Compute the in degrees of each node

    :rtype : dict
    :param digraph: input graph
    """
    # initialize all in-degrees to 0
    in_degrees = {}.fromkeys(digraph.keys(), 0)

    # loop through each node
    for node in digraph.keys():
        edges = digraph[node]
        # increment the in-degree for each edge
        for edge in edges:
            in_degrees[edge] += 1

    return in_degrees


def compute_out_degrees(digraph):
    """
    Compute the out-degrees of each node

    :rtype : dict
    :param digraph: input graph
    """
    # initialize all in-degrees to 0
    out_degrees = {}.fromkeys(digraph.keys(), 0)

    # loop through each node
    for node in digraph.keys():
        out_degrees[node] = len(digraph[node])

    return out_degrees


def in_degree_distribution(digraph):
    """
    calculate the in-degree distribution of a given graph

    :rtype : dict
    :param digraph: input graph
    """
    # local variables
    in_degree_graph = compute_in_degrees(digraph)

    # initialize the dict
    in_degree_dist = {}.fromkeys(in_degree_graph.values(), 0)

    # for each "in-degree" increment the count
    for degrees in in_degree_graph.values():
        in_degree_dist[degrees] += 1

    return in_degree_dist


def generate_random_graph(num_nodes, probability):
    """
    This function will generate a random graph based on a probability

    :rtype : dict
    :param num_nodes: number of nodes in this graph
    :param probability: probability of edge existing
    :return: a dictionary object representing a graph
    """
    graph = {}
    for itr in range(num_nodes):
        graph[itr] = set()

    tracker = range(num_nodes)

    # loop through each node
    for node_x in xrange(num_nodes):
        tracker.remove(node_x)

        for node_y in tracker:
            rand = random.random()
            if rand < probability:
                graph[node_x].add(node_y)

            rand = random.random()
            if rand < probability:
                graph[node_y].add(node_x)

    return graph


def normalize_in_degree_dist(digraph):
    """
    Takes a graph and returns a normalized distribution of each nodes in-degree

    :rtype : dict
    :param digraph: a dictionary representing a directed graph
    """
    idd = in_degree_distribution(digraph)
    total_sum = sum(idd.values())

    norm_dist = {}
    for node in idd:
        norm_dist[node] = float(idd[node]) / total_sum

    return norm_dist


def dpa_graph(num_nodes, num_existing_nodes):
    """
    DPA algorithm implementation

    :rtype : dict
    :param num_nodes: final number of nodes
    :param num_existing_nodes: <= num_nodes, the number of existing nodes to which a new node is connected during each
                                iteration
    :return: dictionary object representing a graph
    """
    # First make a complete graph
    graph = make_complete_graph(num_existing_nodes)

    rand_nodes = dpat.DPATrial(num_existing_nodes)

    # iterate through the remaining nodes
    for new_nodes in xrange(num_existing_nodes, num_nodes):
        new_conns = rand_nodes.run_trial(num_existing_nodes)
        graph[new_nodes] = set(new_conns)

    return graph
