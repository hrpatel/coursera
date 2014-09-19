"""
module 2 project for algorithmic thinking
"""

__author__ = 'mamaray'

from collections import deque
# import alg_project2_graphs as data

def bfs_visited(ugraph, start_node):
    
    """
    a function to get the set consisting of all nodes that are visited by a given node

    :rtype : set
    :param ugraph: undirected graph
    :param start_node: starting node
    :return: the set consisting of all nodes that are visited by a breadth-first search that starts at start_node
    """
    # stores all visited nodes
    visited = set()
    visited.add(start_node)

    # initialize the queue with the current element
    queue = deque()
    queue.append(start_node)

    while len(queue) > 0:
        # pop the next item from the queue
        next_item = queue.pop()

        # iterate through each neighbour of the dequed node
        for neighbour in ugraph[next_item]:
            if not visited.__contains__(neighbour):
                # add to visited and queue so it gets inspected
                visited.add(neighbour)
                queue.append(neighbour)

    return visited

# print bfs_visited(data.GRAPH0, 0)
# print bfs_visited(data.GRAPH1, 0)
# print bfs_visited(data.GRAPH2, 0)
# print bfs_visited(data.GRAPH3, 0)
# print bfs_visited(data.GRAPH5, 3)
# print bfs_visited(data.GRAPH6, 2)
# print bfs_visited(data.GRAPH7, 0)
#
#
