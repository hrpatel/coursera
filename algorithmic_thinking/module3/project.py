"""
Template for Project 3
Student will implement four functions:

slow_closest_pairs(cluster_list)
fast_closest_pair(cluster_list) - implement fast_helper()
hierarchical_clustering(cluster_list, num_clusters)
kmeans_clustering(cluster_list, num_clusters, num_iterations)

where cluster_list is a list of clusters in the plane
"""

__author__ = 'mamaray'

import alg_cluster


def pair_distance(cluster_list, idx1, idx2):
    """
    Helper function to compute Euclidean distance between two clusters in cluster_list with indices idx1 and idx2

    Returns tuple (dist, idx1, idx2) with idx1 < idx2 where dist is distance between cluster_list[idx1]
    and cluster_list[idx2]
    :param cluster_list:
    :param idx1:
    :param idx2:
    :rtype : tuple
    """
    return cluster_list[idx1].distance(cluster_list[idx2]), min(idx1, idx2), max(idx1, idx2)


def slow_closest_pairs(cluster_list):
    """
    Compute the set of closest pairs of cluster in list of clusters using O(n^2) all pairs algorithm

    Returns the set of all tuples of the form (dist, idx1, idx2) where the cluster_list[idx1] and cluster_list[idx2]
    have minimum distance dist.

    :param cluster_list:
    :rtype : set
    """
    # initialize return variable
    pairs = set()

    # initialize variable
    d_1 = 10000000

    # loop through each point
    list_size = len(cluster_list)
    for p_1 in xrange(list_size - 1):
        for p_2 in xrange(p_1 + 1, list_size):
            # calculate distance between all possible combinations
            (d_2, x_2, y_2) = pair_distance(cluster_list, p_1, p_2)
            # did we find a new lower distance?
            if d_2 < d_1:
                d_1 = d_2

                # new lower distance so start over
                pairs = set()
                pairs.add((d_2, x_2, y_2))
            elif d_2 == d_1:
                # equal distance, so add to pairs
                pairs.add((d_2, x_2, y_2))

    return pairs


def fast_closest_pair(cluster_list):
    """
    Compute a closest pair of clusters in cluster_list using O(n log(n)) divide and conquer algorithm

    Returns a tuple (distance, idx1, idx2) with idx1 < idx 2 where cluster_list[idx1] and cluster_list[idx2] have the
    smallest distance dist of any pair of clusters
    :rtype : tuple
    :param cluster_list:
    """

    def fast_helper(c_list, h_order, v_order):
        """
        Divide and conquer method for computing distance between closest pair of points Running time is O(n * log(n))

        horiz_order and vert_order are lists of indices for clusters ordered horizontally and vertically

        Returns a tuple (distance, idx1, idx2) with idx1 < idx 2 where cluster_list[idx1] and cluster_list[idx2]
        have the smallest distance dist of any pair of clusters

        :rtype : tuple
        :type c_list: list
        :param c_list:
        :param h_order:
        :param v_order:
        """

        # base case
        if len(h_order) <= 3:
            # use brute force method on such a small set
            min_pair = slow_closest_pairs([c_list[dummy_ctr] for dummy_ctr in h_order]).pop()

            return min_pair[0], h_order[min_pair[1]], h_order[min_pair[2]]

        # divide
        else:
            # calculate midpoint and middle x value
            h_mid = len(h_order) / 2
            mid_x = 0.5 * (c_list[h_order[h_mid - 1]].horiz_center() +
                           c_list[h_order[h_mid]].horiz_center())

            # half the x-coordinates
            h_l = h_order[:h_mid]
            h_r = h_order[h_mid:]

            # half the y-coordinates (ordered)
            # TODO: make this faster
            vlidx = [(c_list[dummy_ctr].vert_center(), dummy_ctr) for dummy_ctr in h_l]
            vlidx.sort()
            v_l = [vlidx[dummy_ctr][1] for dummy_ctr in range(len(vlidx))]

            vridx = [(c_list[dummy_ctr].vert_center(), dummy_ctr) for dummy_ctr in h_r]
            vridx.sort()
            v_r = [vridx[dummy_ctr][1] for dummy_ctr in range(len(vridx))]

            # break the problem into halves
            pair_l = fast_helper(c_list, h_l, v_l)
            pair_r = fast_helper(c_list, h_r, v_r)

            # conquer
            if pair_l[0] < pair_r[0]:
                min_pair = pair_l
            else:
                min_pair = pair_r

            # check around the mid point of x
            s_list = [dummy_ctr
                      for dummy_ctr in v_order
                      if abs(c_list[dummy_ctr].horiz_center() - mid_x) < min_pair[0]]

            s_size = len(s_list)
            for dummy_idx in xrange(s_size - 1):
                for dummy_idy in xrange(dummy_idx + 1, min(dummy_idx + 4, s_size)):
                    s_d = c_list[s_list[dummy_idx]].distance(c_list[s_list[dummy_idy]])
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

    return answer[0], min(answer[1:]), max(answer[1:])


def hierarchical_clustering(cluster_list, num_clusters):
    """
    Compute a hierarchical clustering of a set of clusters
    :rtype : list
    :param cluster_list:
    :param num_clusters:
    Note: the function mutates cluster_list

    Input: List of clusters, number of clusters
    Output: List of clusters whose length is num_clusters
    """

    # loop until desired num_clusters
    while len(cluster_list) > num_clusters:
        # find the two closest clusters (points)
        closest = fast_closest_pair(cluster_list)

        # merge point 2 -> point 1
        cluster_list[closest[1]].merge_clusters(cluster_list[closest[2]])

        # remove point 2
        cluster_list.pop(closest[2])

    return cluster_list


def kmeans_clustering(cluster_list, num_clusters, num_iterations):
    """
    Compute the k-means clustering of a set of clusters

    :rtype : list
    :param cluster_list:
    :param num_clusters:
    :param num_iterations:
    Input: List of clusters, number of clusters, number of iterations
    Output: List of clusters whose length is num_clusters
    """

    # initialize k-means clusters to be initial clusters with largest populations
    populations = [(cluster_list[idx].total_population(), idx) for idx in range(len(cluster_list))]
    populations.sort(reverse=True)

    # generate "random" centers (but based on most populated num_cluster's)
    u_clusters = [cluster_list[populations[idx][1]].copy() for idx in xrange(num_clusters)]

    k_clusters = []
    # run through each iteration
    for dummy_iteration in range(num_iterations):
        # initialize k empty Clusters
        k_clusters = [alg_cluster.Cluster(set(), 0, 0, 0, 0) for dummy_ctr in range(num_clusters)]

        # loop through each point in cluster_list
        for point in range(len(cluster_list)):

            # for each point, find the closest u_clusters cluster distance
            min_d = 10000000
            min_k_idx = -1
            for dummy_idx in range(num_clusters):
                tmp_d = cluster_list[point].distance(u_clusters[dummy_idx])
                if tmp_d < min_d:
                    min_d = tmp_d
                    min_k_idx = dummy_idx

            # merge the closest point with k_clusters (same index as u_clusters)
            k_clusters[min_k_idx].merge_clusters(cluster_list[point])

        # update each u_center with the new k_clusters centers
        for idx in xrange(num_clusters):
            u_clusters[idx] = k_clusters[idx].copy()

    return k_clusters
