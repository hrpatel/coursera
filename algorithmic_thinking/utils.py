__author__ = 'ray'

import algorithmic_thinking.module1.project as m1project


def read_graph_data(filename):
    """
    A function to read data from a file

    :param filename: file to read data from
    :rtype : dict
    """
    # read in the citation data first
    file = open(filename, "r")
    raw_data = file.read().split("\n")
    file.close()

    # make a dictionary object from the raw data
    graph = {}
    for line in raw_data:
        # support empty files
        line = line.strip()
        if line == "":
            continue

        # first item is a node in the graph
        neighbours = line.split(" ")
        node = int(neighbours.pop(0))

        # initialize the node data
        graph[node] = set([])
        for entry in neighbours:
            graph[node].add(int(entry))

    return graph


def print_graph_data(graph, name=""):
    out_degrees = m1project.compute_out_degrees(graph)
    in_degrees = m1project.compute_in_degrees(graph)

    num_nodes = len(graph.keys())
    total_in_degrees = sum(in_degrees.values())
    total_out_degrees = sum(out_degrees.values())

    if name is not "":
        print "graph:", name
    print "num nodes: ", str(num_nodes)
    print "total out degree: " + str(total_out_degrees)
    print "total in degree: " + str(total_in_degrees)
    print "average out-degree: " + str(float(total_out_degrees) / num_nodes)
    print "average in-degree: " + str(float(total_in_degrees) / num_nodes)
    print
