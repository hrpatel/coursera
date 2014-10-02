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
    for p_1 in xrange(list_size - 1):
        for p_2 in xrange(p_1 + 1, list_size):
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
        # initialize size of horizontal points
        h_size = len(horiz_order)

        # base case
        if h_size <= 3:

            small_list = []
            for node in horiz_order:
                small_list.append(cluster_list[node])

            pair = slow_closest_pairs(small_list)
            min_d, p_1, p_2 = pair.pop()

            return (min_d, horiz_order[p_1], horiz_order[p_2])

        # divide
        else:
            # midpoint
            h_mid = h_size / 2
            mid_x = 0.5 * (cluster_list[horiz_order[h_mid - 1]].horiz_center() +
                           cluster_list[horiz_order[h_mid]].horiz_center())

            # half the x-coordinates
            h_l = horiz_order[:h_mid]
            h_r = horiz_order[h_mid:]

            # half the y-coordinates (ordered)
            # TODO: make this faster
            vlidx = [(cluster_list[idx].vert_center(), idx) for idx in h_l]
            vlidx.sort()
            v_l = [vlidx[idx][1] for idx in range(len(vlidx))]

            vridx = [(cluster_list[idx].vert_center(), idx) for idx in h_r]
            vridx.sort()
            v_r = [vridx[idx][1] for idx in range(len(vridx))]

            # break the problem into smaller bits
            d_l, i_l, j_l = fast_helper(cluster_list, h_l, v_l)
            d_r, i_r, j_r = fast_helper(cluster_list, h_r, v_r)

            # conquer
            if d_l < d_r:
                min_d, p_1, p_2 = d_l, i_l, j_l
            else:
                min_d, p_1, p_2 = d_r, i_r, j_r

            # check around the mid point of x
            s_list = []
            for v_node in vert_order:
                if abs(cluster_list[v_node].horiz_center() - mid_x) < min_d:
                    s_list.append(v_node)

            s_size = len(s_list)
            for idx in xrange(s_size - 1):
                for idy in xrange(idx + 1, min(idx + 4, s_size)):
                    s_d = cluster_list[s_list[idx]].distance(cluster_list[s_list[idy]])
                    if s_d < min_d:
                        min_d, p_1, p_2 = s_d, s_list[idx], s_list[idy]

        return (min_d, p_1, p_2)

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
