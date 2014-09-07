"""
This is code to complete the assignment portion of module 1
"""
__author__ = 'mamaray'

import math
import alg_module1 as funcs
import matplotlib.pyplot as plt

LOG_BASE = 10
SCALE = "LOG"

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
        neighbours = neighbours[:-1]

        # initialize the node data
        cita_data[node] = set([])
        for entry in neighbours:
            cita_data[node].add(int(entry))

    return cita_data


def draw_plot(data, point_style, line_label):
    # get the NORMALIZED distribution of in-degrees
    dist = funcs.normalize_in_degree_dist(data)

    # remove 0 in-degrees
    if dist.has_key(0):
        dist.pop(0)

    # generate the log data
    norm_dist = {}
    if SCALE == "LINEAR":
        for keys in dist.keys():
            norm_dist[keys] = dist[keys]
    elif SCALE == "LOG":
        for keys in dist.keys():
            norm_dist[math.log(keys, LOG_BASE)] = math.log(dist[keys], LOG_BASE)


    plt.plot(norm_dist.keys(), norm_dist.values(), point_style, label=line_label)
    plt.title("In-degree distribution (" + SCALE + " scale)")
    plt.ylabel("% of papers (log base " + str(LOG_BASE) + ")")
    plt.xlabel("# of citations (log base " + str(LOG_BASE) + ")")
    plt.grid(True)
    plt.legend()


# set the canvas size (in inches)
plt.figure(figsize=(12,7))

def app_q1():
    # get the data into a dict
    data = read_citation_data("alg_phys-cite.txt")

    draw_plot(data, "r+", "citations")
    plt.show()


def app_q2():
    data3 = funcs.generate_random_graph(500, .25)
    data2 = funcs.generate_random_graph(700, .55)
    data1 = funcs.generate_random_graph(1000, .9)
    data = read_citation_data("alg_phys-cite.txt")

    draw_plot(data, "r+", "citations")
    draw_plot(data3, "g^", "random_graph(500, .25)")
    draw_plot(data2, "ys", "random_graph(700, .55)")
    draw_plot(data1, "mo", "random_graph(1000, .9)")
    plt.show()


def app_q2_2():
    data1 = funcs.generate_random_graph(5000, .85)

    draw_plot(data1, "mo", "random_graph(5000, .85)")
    plt.show()


def app_q3():
    # get the data into a dict
    data = read_citation_data("alg_phys-cite.txt")
    out_degrees = funcs.compute_out_degrees(data)
    in_degrees = funcs.compute_in_degrees(data)

    num_nodes = len(data.keys())
    total_in_degrees = sum(in_degrees.values())
    total_out_degrees = sum(out_degrees.values())
    print "num nodes: ", str(num_nodes)
    print "total out degree: " + str(total_out_degrees)
    print "total in degree: " + str(total_in_degrees)
    print "average out-degree of citations: " + str(float(total_out_degrees)/num_nodes)
    print "average in-degree of citations: " + str(float(total_in_degrees)/num_nodes)


def app_q4():
    # get the data into a dict
    data1 = funcs.dpa_graph(27770,13)

    draw_plot(data1, "gs", "dpa_graph(27770,13)")
    plt.show()


def app_q5():
    # get the data into a dict
    data1 = funcs.dpa_graph(27770,13)
    data = read_citation_data("alg_phys-cite.txt")

    draw_plot(data, "r+", "citations")
    draw_plot(data1, "gs", "dpa_graph(27770,13)")
    plt.show()


app_q5()