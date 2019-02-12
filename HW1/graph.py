# include any code you need for your assignment in this file or in auxiliary
# files that can be imported here.

import os
import networkx as nx
import itertools
from numpy.random import choice, randint
import numpy as np
import matplotlib.pyplot as plt

# given number of nodes n and probability p, output a random graph
# as specified in homework
def create_graph(n,p):
    G=nx.Graph()
    G.add_nodes_from([i for i in range(n)])

    # Create list of nodes
    node_list = []

    for i in range(1,n+1):
        node_list.append(i)

    # For each combination of nodes, determine if there is an edge
    for node_pair in itertools.combinations(node_list,2):
        if (choice([True,False], 1, p=[p,1-p])):
            G.add_edge(node_pair[0],node_pair[1])

    return G


# given a graph G and nodes i,j, output the length of the shortest
# path between i and j in G.
def shortest_path(G,i,j):
    # Check if source is target
    if (i == j):
      return 0

    discovered = []
    queue = [i]

    distance = 0

    while (len(queue) != 0):
        temp = queue.pop(0)
        discovered.append(temp)
        neighbors = [n for n in list(G[temp]) if n not in queue and n not in discovered]
        if j in neighbors:
            return distance
        queue.extend(neighbors)
        distance += 1

    return "infinity"


##########################################################
# Problem 8c
##########################################################
def problem8c():

    print("\t Building a random graph...")
    G = create_graph(1000,0.1)

    distances = []

    os.remove("avg_shortest_path.txt")
    f = open("avg_shortest_path.txt", "a")

    print("\t Finding the shortest path for 1000 random nodes...")
    for i in range(1000):
        n1 = randint(1,1001)
        n2 = randint(1,1001)

        dist = shortest_path(G,n1,n2)

        distances.append(dist)

        f.write("({},{},{})\n".format(n1,n2,dist))

    f.close()
    print ("\t\tThe average distance is {}.".format(sum(distances)/len(distances)))


##########################################################
# Question 8d
##########################################################
def problem8d():
    os.remove("varying_p.txt")
    f = open("varying_p.txt", "a")
    f.write("p, avg_shortest_path\n")

    x = []
    y = []

    print("\t Finding the shortest paths for varying p...")
    for p in np.arange(0.01,0.05,0.01):
        x.append(p)
        G = create_graph(1000,p)

        distances = []

        for i in range(1000):
            n1 = randint(1,1001)
            n2 = randint(1,1001)

            dist = shortest_path(G,n1,n2)

            distances.append(dist)

        avg_distance = sum(distances)/len(distances)
        y.append(avg_distance)
        f.write("{}, {}\n".format(p,avg_distance))

    for p in np.arange(0.05,0.55,0.05):
        p = float('%.3f'%(p))   # correct floating point rounding errors from np.arange

        x.append(p)
        G = create_graph(1000,p)

        distances = []

        for i in range(1000):
            n1 = randint(1,1001)
            n2 = randint(1,1001)

            dist = shortest_path(G,n1,n2)

            distances.append(dist)

        avg_distance = sum(distances)/len(distances)
        y.append(avg_distance)
        f.write("{}, {}\n".format(p,avg_distance))

    f.close()

    # Plot the average shortest path as a function of p
    plt.plot(x,y,'o')
    plt.ylabel('Average Shortest Path')
    plt.xlabel('p')
    plt.show()


##########################################################
# Problem 9a
##########################################################
def problem9a():

    fb_G=nx.Graph()

    print("\t Building a graph from facebook combined data...")
    # create graph from Facebook data
    with open("facebook_combined.txt") as in_file:
        node_list = in_file.readlines()
        node_list = [x.strip().split() for x in node_list]

        for node_pair in node_list:
            node_pair[0] = int(node_pair[0])
            node_pair[1] = int(node_pair[1])

    # Create edges for each pair
    for node_pair in node_list:
        fb_G.add_edge(node_pair[0],node_pair[1])

    distances = []

    os.remove("fb_shortest_path.txt")
    f = open("fb_shortest_path.txt", "a")

    print("\t Finding the shortest path for 1000 random nodes...")
    for i in range(1000):
        n1 = randint(1,1001)
        n2 = randint(1,1001)

        dist = shortest_path(fb_G,n1,n2)

        distances.append(dist)

        f.write("({},{},{})\n".format(n1,n2,dist))

    f.close()
    print ("\t\tThe average distance is {}.".format(sum(distances)/len(distances)))


##########################################################
# Run the function for each problem
##########################################################
def main():
    print("Executing Problem 8c...")
    problem8c()
    print("Executing Problem 8d...")
    problem8d()
    print("Executing Problem 9a...")
    problem9a()

main()
