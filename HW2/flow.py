# include any code you need for your assignment in this file or in auxiliary
# files that can be imported here.

import os
import networkx as nx
from random import random as roll
from helper_functions import *
# import numpy as np
# from numpy.random import randint

# 8 (a)
# implement an algorithm that computes the maximum flow in a graph G
# Note: you may represent the graph, source, sink, and edge capacities
# however you want. You may also change the inputs to the function below.
# I am passing in edge capacities in the graph structure itself
def max_flow(G, s, t):

    max_flow = 0
    residual_g = G
    path = BFS(residual_g, s, t)

    # While there is a path from source to sink
    while (path != None):

        # Push maximum flow along this path (minimum cap of edges)
        path_flow = float("Inf")
        for i in range(0, len(path)-2):
            if (residual_g[path[i]][path[i+1]]['cap'] < path_flow):
                path_flow = residual_g[path[i]][path[i+1]]['cap']

        print("Path Flow: " + str(path_flow))

        # Increase max flow by max flow of current path
        max_flow += path_flow

        print("Max Flow: " + str(max_flow))

        # Decrease capacity of each edge where flow was added
        # Create a reverse edge with capacity equal to the flow passed through that edge
        for i in range(0, len(path)-2):
            residual_g[path[i]][path[i+1]]['cap'] -= path_flow
            if (residual_g[path[i]][path[i+1]]['cap'] == 0):
                residual_g.remove_edge(path[i],path[i+1])

            if (residual_g.has_edge(path[i+1],path[i])):
                residual_g[path[i+1]][path[i]]['cap'] += path_flow
            else:
                residual_g.add_edge(path[i+1], path[i])
                residual_g[path[i+1]][path[i]]['cap'] = path_flow

        plt.plot()
        nx.draw(residual_g, with_labels=True, font_weight='bold')
        # plt.show()

        # Find a path from source to sink in new residual graph
        path = BFS(residual_g, s, t)

    return max_flow


# 8 (d)
# implement an algorithm that determines the number of edge-disjoint paths
# between two nodes in a graph G
def edge_disjoint_paths(G, u, v):
    return -1


# given a graph G and nodes i,j, output a path if one exists else return None
def BFS(G,i,j):
    # Check if source is target
    if (i == j):
      return [j]

    queue = [[i]]

    while queue:
        cur_path = queue.pop(0)
        temp = cur_path[-1]

        if temp == j:
            return cur_path

        for neighbor in [n for n in list(G[temp]) if n not in queue and n not in cur_path and n]:
            next_path = list(cur_path)
            next_path.append(neighbor)
            queue.append(next_path)

    return None


##########################################################
# Problem 8a Figure 6.1
##########################################################
def problem8a_figure61():
    G = create_figure6_1()
    f = max_flow(G,1,4)
    print(f)


##########################################################
# Problem 8a Figure 6.3
##########################################################
def problem8a_figure63():
    pass


##########################################################
# Problem 8d
##########################################################
def problem8d():
    pass


##########################################################
# Problem 9a Figure 3.1
##########################################################
def problem9a_figure31():
    pass


##########################################################
# Problem 9b
##########################################################
def problem9b():
    pass


##########################################################
# Problem 9c
##########################################################
def problem9c():
    pass


problem8a_figure61()
