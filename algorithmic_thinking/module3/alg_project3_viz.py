"""
Example code for creating and visualizing
cluster of county-based cancer risk data

Note that you must download the file
http://www.codeskulptor.org/#alg_clusters_matplotlib.py
to use the matplotlib version of this code
"""

import alg_cluster
import alg_clusters_matplotlib
import math
import matplotlib.pyplot as plt
import project


# ##################################################
# Code to load data tables

# URLs for cancer risk data tables of various sizes
# Numbers indicate number of counties in data table
DIRECTORY = "http://commondatastorage.googleapis.com/codeskulptor-assets/"
DATA_3108_URL = "unifiedCancerData_3108.csv"
DATA_896_URL = "unifiedCancerData_896.csv"
DATA_290_URL = "unifiedCancerData_290.csv"
DATA_111_URL = "unifiedCancerData_111.csv"


def load_data_table(data_url):
    """
    Import a table of county-based cancer risk data
    from a csv format file
    """
    data_file = open(data_url)
    data = data_file.read()
    data_lines = data.split('\n')
    print "Loaded", len(data_lines), "data points"
    data_tokens = [line.split(',') for line in data_lines]
    return [[tokens[0], float(tokens[1]), float(tokens[2]), int(tokens[3]), float(tokens[4])]
            for tokens in data_tokens]


# ###########################################################
# Code to create sequential clustering
# Create alphabetical clusters for county data

def sequential_clustering(singleton_list, num_clusters):
    """
    Take a data table and create a list of clusters
    by partitioning the table into clusters based on its ordering
    
    Note that method may return num_clusters or num_clusters + 1 final clusters
    """

    cluster_list = []
    total_clusters = len(singleton_list)
    cluster_size = float(total_clusters) / num_clusters

    for cluster_idx in range(len(singleton_list)):
        new_cluster = singleton_list[cluster_idx]
        if math.floor(cluster_idx / cluster_size) != \
                math.floor((cluster_idx - 1) / cluster_size):
            cluster_list.append(new_cluster)
        else:
            cluster_list[-1] = cluster_list[-1].merge_clusters(new_cluster)

    return cluster_list


# ####################################################################
# Code to load cancer data, compute a clustering and 
# visualize the results

def run_example():
    """
    Load a data table, compute a list of clusters and 
    plot a list of clusters

    Set DESKTOP = True/False to use either matplotlib or simplegui
    """
    data_table = load_data_table(DATA_3108_URL)

    singleton_list = []
    for line in data_table:
        singleton_list.append(alg_cluster.Cluster({line[0]}, line[1], line[2], line[3], line[4]))

    # cluster_list = sequential_clustering(singleton_list, 50)
    # print "Displaying", len(cluster_list), "sequential clusters"

    # cluster_list = project.hierarchical_clustering(singleton_list, 15)
    # print "Displaying", len(cluster_list), "hierarchical clusters"

    cluster_list = project.kmeans_clustering(singleton_list, 15, 5)
    print "Displaying", len(cluster_list), "k-means clusters"

    # draw the clusters using matplotlib or simplegui
    alg_clusters_matplotlib.plot_clusters(data_table, cluster_list, True)


def assignment_q2():
    """
    Load a data table, compute a list of clusters and
    plot a list of clusters
    """
    data_table = load_data_table(DATA_3108_URL)
    singleton_list = []
    for line in data_table:
        singleton_list.append(alg_cluster.Cluster({line[0]}, line[1], line[2], line[3], line[4]))

    cluster_list = project.hierarchical_clustering(singleton_list, 15)
    print "Displaying", len(cluster_list), "hierarchical clusters"

    alg_clusters_matplotlib.plot_clusters(data_table, cluster_list, True)


def assignment_q3():
    """
    Load a data table, compute a list of clusters and
    plot a list of clusters
    """
    data_table = load_data_table(DATA_3108_URL)
    singleton_list = []
    for line in data_table:
        singleton_list.append(alg_cluster.Cluster({line[0]}, line[1], line[2], line[3], line[4]))

    cluster_list = project.kmeans_clustering(singleton_list, 15, 5)
    print "Displaying", len(cluster_list), "k-means clusters"

    alg_clusters_matplotlib.plot_clusters(data_table, cluster_list, True)


def assignment_q5():
    """
    Load a data table, compute a list of clusters and
    plot a list of clusters
    """
    data_table = load_data_table(DATA_111_URL)
    singleton_list = []
    for line in data_table:
        singleton_list.append(alg_cluster.Cluster({line[0]}, line[1], line[2], line[3], line[4]))

    cluster_list = project.hierarchical_clustering(singleton_list, 9)

    # q7
    distortion = compute_distortion(cluster_list, data_table)
    print "hierarchical_clustering distortion:", distortion

    print "Displaying", len(cluster_list), "hierarchical clusters"

    alg_clusters_matplotlib.plot_clusters(data_table, cluster_list, True)


def assignment_q6():
    """
    Load a data table, compute a list of clusters and
    plot a list of clusters
    """
    data_table = load_data_table(DATA_111_URL)
    singleton_list = []
    for line in data_table:
        singleton_list.append(alg_cluster.Cluster({line[0]}, line[1], line[2], line[3], line[4]))

    cluster_list = project.kmeans_clustering(singleton_list, 9, 5)

    # q7
    distortion = compute_distortion(cluster_list, data_table)
    print "kmeans_clustering distortion:", distortion

    print "Displaying", len(cluster_list), "k-means clusters"

    alg_clusters_matplotlib.plot_clusters(data_table, cluster_list, True)


def compute_distortion(cluster_list, data_table):
    distortion = 0
    for idx in range(len(cluster_list)):
        distortion += cluster_list[idx].cluster_error(data_table)
    return distortion


def assignment_q10():
    """
    Load a data table, compute a list of clusters and
    plot a list of clusters
    """

    distortions = {}

    methods = {"kmeans": project.kmeans_clustering,
               "hierarchical": project.hierarchical_clustering}

    data_tables = {"111": "unifiedCancerData_111.csv",
                   "290": "unifiedCancerData_290.csv",
                   "896": "unifiedCancerData_896.csv"}

    # loop through each data file
    for data in data_tables.keys():
        distortions[data] = {}

        # read in the data
        data_table = load_data_table(data_tables[data])
        singleton_list = []
        for line in data_table:
            singleton_list.append(alg_cluster.Cluster({line[0]}, line[1], line[2], line[3], line[4]))

        # loop through each clustering method
        for method in ["kmeans", "hierarchical"]:
            distortions[data][method] = []

            cluster_list = []
            # loop through cluster sizes in reverse
            for num_clusters in range(20, 5, -1):

                if method == "kmeans":
                    cluster_list = methods[method](singleton_list, num_clusters, 5)

                # WARNING: 'hierarchical' modifies the cluster list
                elif method == "hierarchical":
                    cluster_list = methods[method](singleton_list, num_clusters)

                distortion = compute_distortion(cluster_list, data_table)
                # print distortion
                distortions[data][method].append(distortion)

                print "done with:", method, "method,", num_clusters, "data,", data, "clusters"

            print
            print

        print
        print

    # loop through each data set
    for dataset in distortions.keys():
        colours = ["-b", "-g"]

        # loop through each algorithm
        for alg in distortions[dataset]:
            # reverse the data so it aligns with output clusters
            distortions[dataset][alg].reverse()

            # define the x axis data
            xvals = range(6, 21)

            # add data to plot
            plt.plot(xvals, distortions[dataset][alg], colours.pop(), label=alg)

        # plot the data
        plt.legend(loc='upper right')
        plt.xlabel(" number of output clusters")
        plt.ylabel("distortion associated with each output clustering")
        plt.title("distortion of the list of {} clusters".format(dataset))
        plt.show()


def assignment_q10_graphs():
    """
    leaving here for reference. I've updated the above method to generate data and plot.
    """
    data = {'111': {'hierarchical': [43346616567.370995, 43572685067.322044, 47956771398.36999, 75195590422.5596,
                                     76305792806.40341, 83751677988.91672, 92851824733.8917, 95061330400.91187,
                                     123364931819.36792, 128691501288.44057, 136007319294.4524, 175163886915.8305,
                                     256295541683.34512, 304487213235.6511, 473061548301.70715],
                    'kmeans': [123389671106.6206, 123483080788.27681, 161626921206.76382, 162018028052.88672,
                               163567291743.99063, 164745271371.3518, 165471040577.26993, 173058588040.28055,
                               173535638065.6752, 174267507472.60236, 175790688405.04092, 271254226924.20047,
                               430845493901.4979, 480503404944.00757, 855406302600.9299]},

            '290': {'hierarchical': [158866394846.55307, 165854841465.23853, 209424475932.79617, 210882439099.43875,
                                     257523094470.34372, 265642320327.18256, 273999812286.6749, 300957083742.44525,
                                     409759400590.09357, 452595640777.7162, 479106607308.0914, 607404453849.4803,
                                     607704110695.7351, 873386979469.7281, 1721363375274.0847],
                    'kmeans': [186562044404.06274, 215763229779.78592, 218182336738.10098, 220231070772.07336,
                               232286884261.00916, 238910074068.03934, 397061951861.4956, 397796574329.07294,
                               449630999209.31024, 557173759501.5332, 619318206656.0833, 656031563613.5233,
                               726141205120.559, 1256566786124.0432, 1432446364647.484]},

            '896': {'hierarchical': [377806730495.8184, 463371219437.6528, 466383317148.95233, 468733959164.0338,
                                     504815920302.4635, 509864466993.6245, 581040540888.136, 635476455541.3553,
                                     775480684213.7341, 887973140164.112, 947764944638.2128, 972923457621.6617,
                                     1228012004919.8132, 1263342391158.555, 2211819145957.3906],
                    'kmeans': [341850583704.0547, 392190427938.5421, 418814444487.6942, 441641633333.34503,
                               475260676178.591, 477113007869.9135, 693980006271.2808, 707481162063.751,
                               717297472806.9475, 873017865209.888, 941617184525.7502, 1005638949041.6797,
                               1149516152182.7866, 1632162002379.899, 2376173737632.8]}}


    # loop through each data set
    for dataset in data.keys():
        colours = ["-b", "-g"]

        # loop through each algorithm
        for alg in data[dataset]:
            # reverse the data so it aligns with output clusters
            data[dataset][alg].reverse()

            # define the x axis data
            xvals = range(6, 21)

            # add data to plot
            plt.plot(xvals, data[dataset][alg], colours.pop(), label=alg)

        # plot the data
        plt.legend(loc='upper right')
        plt.xlabel(" number of output clusters")
        plt.ylabel("distortion associated with each output clustering")
        plt.title("distortion of the list of {} clusters".format(dataset))
        plt.show()
