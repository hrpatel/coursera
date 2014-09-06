"""
This is code to complete the assignment portion of module 1
"""
__author__ = 'mamaray'

import math
import alg_module1 as funcs
import matplotlib.pyplot as plt


def read_citation_data(filename):
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
    cita_data = {}
    for line in raw_data:
        if line.strip() == "":
            continue

        # first item is a node in the graph
        neighbours = line.split(" ")
        node = int(neighbours.pop(0))
        neighbours = neighbours[1:-1]

        # initialize the node data
        cita_data[node] = set([])
        for entry in neighbours:
            cita_data[node].add(int(entry))

    return cita_data


# get the data into a dict
data = read_citation_data("alg_phys-cite.txt")

# number of entries in the data
num_entries = len(data.keys())

# get the distribution of in-degrees
dist = funcs.in_degree_distribution(data)
#print dist

# remove 0 in-degrees
dist.pop(0)

# generate the log data
norm_dist = {}
for keys in dist.keys():
    norm_dist[math.log(keys)] = math.log(dist[keys])

plt.plot(norm_dist.keys(), norm_dist.values(), 'ro')
plt.title("In-degree distribution of citations (log scale)")
plt.ylabel("# of papers with given in-degree (log base 2)")
plt.xlabel("in-degree of paper (log base 2)")
plt.show()
plt.grid(True)
