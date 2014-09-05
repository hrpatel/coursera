"""
Algorithmic Thinking - Module 1 Project
"""
__author__ = 'mamaray'

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
    for ctr in xrange(num_nodes):
        tmp = range(num_nodes)
        tmp.remove(ctr)
        graph[ctr] = set(tmp)

    return graph


def compute_in_degrees(digraph):
    """
    Compute the in degrees of each node

    :rtype : dictionary of each object with its in degree
    :param digraph: input graph
    """
    in_degrees = {}
    # initialize all in-degrees to 0
    for node in digraph.keys():
        in_degrees[node] = 0

    # loop through each node
    for node in digraph.keys():
        edges = digraph[node]

        # increment the in-degree for each edge
        for edge in edges:
            in_degrees[edge] +=1

    return in_degrees


def in_degree_distribution(digraph):
    """
    calculate the in-degree distribution of a given graph

    :rtype : dictionary object with
    :param digraph: input graph
    """
    # local variables
    in_degree_graph = compute_in_degrees(digraph)
    in_degree_dist = {}

    # initialize the return variable
    for degrees in in_degree_graph.values():
        in_degree_dist[degrees] = 0

    # for each "in-degree" increment the count
    for degrees in in_degree_graph.values():
        in_degree_dist[degrees] += 1

    return in_degree_dist
