from algorithmic_thinking.module1 import graph_data

__author__ = 'ray'

import random
import UPATrial as upa
import algorithmic_thinking.utils as utils
import algorithmic_thinking.module1.project as m1project
import algorithmic_thinking.module2.project as m2project
import matplotlib.pyplot as plt


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


def upa_graph(num_nodes, num_existing_nodes):
    """
    UPA algorithm implementation

    :rtype : dict
    :param num_nodes: final number of nodes
    :param num_existing_nodes: <= num_nodes, the number of existing nodes to which a new node is connected
                                during each iteration
    :return: dictionary object representing a graph
    """
    # First make a complete graph
    graph = m1project.make_complete_graph(num_existing_nodes)

    rand_nodes = upa.UPATrial(num_existing_nodes)

    # iterate through the remaining nodes
    for new_node in xrange(num_existing_nodes, num_nodes):
        # get new connections for the next node
        new_conns = rand_nodes.run_trial(num_existing_nodes)

        # add the new connections
        graph[new_node] = set(new_conns)

        # add the same edges in the opposite direction
        for new_con in new_conns:
            graph[new_con].add(new_node)

    return graph


def random_order(graph):
    """
    that takes a graph and returns a list of the nodes in the graph in some random order

    :rtype : list
    :param graph: graph object
    :return: list of nodes in an random order
    """
    # make a list and shuffle it
    shuffled_nodes = graph.keys()
    random.shuffle(shuffled_nodes)

    # return shuffled node list
    return shuffled_nodes


def q1():
    """
    examine the resilience of the computer network under an attack in which servers are chosen at random. We will
    then compare the resilience of the network to the resilience of ER and UPA graphs of similar size
    :return:
    """
    # get the network graph
    net_g = utils.read_graph_data("alg_rf7.txt")

    # generate a upa graph with the given average out-degree
    total_out_degrees = sum(m1project.compute_out_degrees(net_g).values())
    average_degree =float(total_out_degrees) / len(net_g)
    m = int(round(average_degree))
    upa_g = upa_graph(len(net_g), m)

    # create an ER ugraph
    p = 0.0034328666
    er_g = generate_random_ugraph(len(net_g), p)

    # utils.print_graph_data(net_g, name="net_g")
    # utils.print_graph_data(upa_g, name="upa_g")
    # utils.print_graph_data(er_g, name="er_g")

    # compute the resiliency of each graph
    attack_order = random_order(net_g)
    net_g_r = m2project.compute_resilience(net_g, attack_order)
    upa_g_r = m2project.compute_resilience(upa_g, attack_order)
    er_g_r = m2project.compute_resilience(er_g, attack_order)

    # plot the data
    xvals = range(len(net_g) + 1)

    plt.plot(xvals, net_g_r, '-b', label='network')
    plt.plot(xvals, upa_g_r, '-r', label='upa graph, m='+str(m))
    plt.plot(xvals, er_g_r, '-g', label='er graph, p='+str(p))
    plt.legend(loc='upper right')
    plt.xlabel("Number of nodes removed")
    plt.ylabel("Size of largest connected component")
    plt.title("Comparison of Network/Graph Resiliency")
    plt.show()


q1()


