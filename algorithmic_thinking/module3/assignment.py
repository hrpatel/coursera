__author__ = 'mamaray'


import alg_cluster
import project
import random
import time
import matplotlib.pyplot as plt


from random import randint
pointList = [alg_cluster.Cluster(set(), randint(0,1000), randint(0,1000), 0, 0) for i in range(1000)]

def compare_slow_fast_pairs():
    import cProfile

    for i in range(1):
        cProfile.run('project.fast_closest_pair(pointList)')
        cProfile.run('project.slow_closest_pairs(pointList)')

# compare_slow_fast_pairs()



def gen_random_clusters(num_clusters):
    clusters = []
    choices = [0, 1]
    for ctr in xrange(num_clusters):
        clusters.append(alg_cluster.Cluster(set(),
                                            random.choice(choices),
                                            random.choice(choices),
                                            0,
                                            0))
    return clusters


def fast_closest_pair(i):
    return project.fast_closest_pair(gen_random_clusters(i))
def slow_closest_pair(i):
    return project.slow_closest_pairs(gen_random_clusters(i))


def q_1():
    # start a dict to store the running time
    slow_run = {}
    fast_run = {}

    for ctr in range(2, 200):
        t1 = time.time()
        project.slow_closest_pairs(gen_random_clusters(ctr))
        slow_run[ctr] = time.time() - t1

        t1 = time.time()
        project.fast_closest_pair(gen_random_clusters(ctr))
        fast_run[ctr] = time.time() - t1

        print "done:", ctr

    # plot the data
    xvals = slow_run.keys()

    plt.plot(xvals, slow_run.values(), '-b', label='slow_closest_pairs')
    plt.plot(xvals, fast_run.values(), '-r', label='fast_closest_pair')
    plt.legend(loc='upper right')
    plt.xlabel("Number of points")
    plt.ylabel("Running Time")
    plt.title("Comparison of slow_closest_pairs/fast_closest_pair algorithms")
    plt.show()


q_1()