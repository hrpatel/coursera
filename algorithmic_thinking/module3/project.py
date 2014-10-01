"""
Template for Project 3
Student will implement four functions:

slow_closest_pairs(cluster_list)
fast_closest_pair(cluster_list) - implement fast_helper()
hierarchical_clustering(cluster_list, num_clusters)
kmeans_clustering(cluster_list, num_clusters, num_iterations)

where cluster_list is a list of clusters in the plane
"""

__author__ = 'hrpatel'


import math
import alg_cluster


def pair_distance(cluster_list, idx1, idx2):
    """
    Helper function to compute Euclidean distance between two clusters in cluster_list with indices idx1 and idx2

    Returns tuple (dist, idx1, idx2) with idx1 < idx2 where dist is distance between cluster_list[idx1]
    and cluster_list[idx2]
    """
    return (cluster_list[idx1].distance(cluster_list[idx2]), min(idx1, idx2), max(idx1, idx2))


def slow_closest_pairs(cluster_list):
    """
    Compute the set of closest pairs of cluster in list of clusters using O(n^2) all pairs algorithm

    Returns the set of all tuples of the form (dist, idx1, idx2) where the cluster_list[idx1] and cluster_list[idx2]
    have minimum distance dist.

    """
    # initialize return variable
    pairs = set()

    # initialize variable
    d_1 = 1000000

    # loop through each point
    list_size = len(cluster_list)
    for p_1 in xrange(list_size):
        for p_2 in xrange(list_size):
            if p_1 is p_2:
                continue
            else:
                (d_2, x_2, y_2) = pair_distance(cluster_list, p_1, p_2)
                # did we find a new lower distance?
                if d_2 < d_1:
                    d_1 = d_2

                    pairs = set()
                    pairs.add((d_2, x_2, y_2))
                # is it  equal to min?
                elif d_2 == d_1:
                    pairs.add((d_2, x_2, y_2))

    return pairs


def fast_closest_pair(cluster_list):
    """
    Compute a closest pair of clusters in cluster_list using O(n log(n)) divide and conquer algorithm

    Returns a tuple (distance, idx1, idx2) with idx1 < idx 2 where cluster_list[idx1] and cluster_list[idx2] have the
    smallest distance dist of any pair of clusters
    """

    def fast_helper(cluster_list, horiz_order, vert_order):
        """
        Divide and conquer method for computing distance between closest pair of points Running time is O(n * log(n))

        horiz_order and vert_order are lists of indices for clusters ordered horizontally and vertically

        Returns a tuple (distance, idx1, idx2) with idx1 < idx 2 where cluster_list[idx1] and cluster_list[idx2]
        have the smallest distance dist of any pair of clusters

        """

        # base case

        # divide

        # conquer

        return (0, 0, 0)

    # compute list of indices for the clusters ordered in the horizontal direction
    hcoord_and_index = [(cluster_list[idx].horiz_center(), idx)
                        for idx in range(len(cluster_list))]
    hcoord_and_index.sort()
    horiz_order = [hcoord_and_index[idx][1] for idx in range(len(hcoord_and_index))]

    # compute list of indices for the clusters ordered in vertical direction
    vcoord_and_index = [(cluster_list[idx].vert_center(), idx)
                        for idx in range(len(cluster_list))]
    vcoord_and_index.sort()
    vert_order = [vcoord_and_index[idx][1] for idx in range(len(vcoord_and_index))]

    # compute answer recursively
    answer = fast_helper(cluster_list, horiz_order, vert_order)
    return (answer[0], min(answer[1:]), max(answer[1:]))


def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters
    Note: the function mutates cluster_list

    Input: List of clusters, number of clusters
    Output: List of clusters whose length is num_clusters
    """

    return []


def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Compute the k-means clustering of a set of clusters

    Input: List of clusters, number of clusters, number of iterations
    Output: List of clusters whose length is num_clusters
    """

    # initialize k-means clusters to be initial clusters with largest populations

    return []
