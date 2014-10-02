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


import alg_cluster


def pair_distance(cluster_list, idx1, idx2):
    """
    Helper function to compute Euclidean distance between two clusters in cluster_list with indices idx1 and idx2

    Returns tuple (dist, idx1, idx2) with idx1 < idx2 where dist is distance between cluster_list[idx1]
    and cluster_list[idx2]
    :rtype : tuple
    """
    return (cluster_list[idx1].distance(cluster_list[idx2]), min(idx1, idx2), max(idx1, idx2))


def slow_closest_pairs(cluster_list):
    """
    Compute the set of closest pairs of cluster in list of clusters using O(n^2) all pairs algorithm

    Returns the set of all tuples of the form (dist, idx1, idx2) where the cluster_list[idx1] and cluster_list[idx2]
    have minimum distance dist.

    :rtype : set
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

        # base case
        if len(horiz_order) <= 3:
            # use brute force method on such a small set
            min_pair = slow_closest_pairs([cluster_list[dummy_ctr] for dummy_ctr in horiz_order]).pop()

            return (min_pair[0], horiz_order[min_pair[1]], horiz_order[min_pair[2]])

        # divide
        else:
            # calculate midpoint and middle x value
            h_mid = len(horiz_order) / 2
            mid_x = 0.5 * (cluster_list[horiz_order[h_mid - 1]].horiz_center() +
                           cluster_list[horiz_order[h_mid]].horiz_center())

            # half the x-coordinates
            h_l = horiz_order[:h_mid]
            h_r = horiz_order[h_mid:]

            # half the y-coordinates (ordered)
            # TODO: make this faster
            vlidx = [(cluster_list[dummy_ctr].vert_center(), dummy_ctr) for dummy_ctr in h_l]
            vlidx.sort()
            v_l = [vlidx[dummy_ctr][1] for dummy_ctr in range(len(vlidx))]

            vridx = [(cluster_list[dummy_ctr].vert_center(), dummy_ctr) for dummy_ctr in h_r]
            vridx.sort()
            v_r = [vridx[dummy_ctr][1] for dummy_ctr in range(len(vridx))]

            # break the problem into smaller bits
            pair_l = fast_helper(cluster_list, h_l, v_l)
            pair_r = fast_helper(cluster_list, h_r, v_r)

            # conquer
            if pair_l[0] < pair_r[0]:
                min_pair = pair_l
            else:
                min_pair = pair_r

            # check around the mid point of x
            s_list = [dummy_ctr
                      for dummy_ctr in vert_order
                      if abs(cluster_list[dummy_ctr].horiz_center() - mid_x) < min_pair[0]]

            s_size = len(s_list)
            for dummy_idx in xrange(s_size - 1):
                for dummy_idy in xrange(dummy_idx + 1, min(dummy_idx + 4, s_size)):
                    s_d = cluster_list[s_list[dummy_idx]].distance(cluster_list[s_list[dummy_idy]])
                    if s_d < min_pair[0]:
                        min_pair = (s_d, s_list[dummy_idx], s_list[dummy_idy])

        return min_pair

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


# def compare_slow_fast_pairs():
#     from random import randint
#     import cProfile
#
#     pointList = [alg_cluster.Cluster(set(), randint(0,1000), randint(0,1000), 0, 0) for i in range(1000)]
#
#     for i in range(1):
#         cProfile.run('fast_closest_pair(pointList)')
#         cProfile.run('slow_closest_pairs(pointList)')


# print fast_closest_pair([alg_cluster.Cluster(set([]), 90.9548590217, -17.089022585, 1, 0), alg_cluster.Cluster(set([]), 90.2536656675, -70.5911544718, 1, 0), alg_cluster.Cluster(set([]), -57.5872347006, 99.7124028905, 1, 0), alg_cluster.Cluster(set([]), -15.9338519877, 5.91547495626, 1, 0), alg_cluster.Cluster(set([]), 19.1869055492, -28.0681513017, 1, 0), alg_cluster.Cluster(set([]), -23.0752410653, -42.1353490324, 1, 0), alg_cluster.Cluster(set([]), -65.1732261872, 19.675582646, 1, 0), alg_cluster.Cluster(set([]), 99.7789872101, -11.2619165604, 1, 0), alg_cluster.Cluster(set([]), -43.3699854405, -94.7349852817, 1, 0), alg_cluster.Cluster(set([]), 48.2281912402, -53.3441788034, 1, 0)])
# expected one of the tuples in set([(10.5745166749, 0, 7)])
# received (38.500309620222225, 4, 9)