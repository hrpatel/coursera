__author__ = 'ray'


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
        if line.strip() == "":
            continue

        # first item is a node in the graph
        neighbours = line.split(" ")
        node = int(neighbours.pop(0))
        neighbours = neighbours[:-1]

        # initialize the node data
        graph[node] = set([])
        for entry in neighbours:
            graph[node].add(int(entry))

    return graph