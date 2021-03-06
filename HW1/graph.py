# include any code you need for your assignment in this file or in auxiliary
# files that can be imported here.

import os
import networkx as nx
from numpy.random import randint
from random import random as roll
import numpy as np
import matplotlib.pyplot as plt

# given number of nodes n and probability p, output a random graph
# as specified in homework
def create_graph(n,p):
    G=nx.Graph()
    G.add_nodes_from([i for i in range(n)])

    for i in range(n):
        for j in range(i+1, n):
            if roll() < p:
                G.add_edge(i,j)

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

    while queue:
        temp = queue.pop(0)
        discovered.append(temp)
        neighbors = [n for n in list(G[temp]) if n not in queue and n not in discovered]
        distance += 1
        if j in neighbors:
            return distance
        queue.extend(neighbors)

    return "infinity"


# Create and return graph from facebook data
def create_fb_graph():
    fb_G = nx.Graph()

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

    return fb_G


##########################################################
# Problem 8c
##########################################################
def problem8c():

    print("\t Building a random graph...")
    G = create_graph(1000,0.1)

    distances = []

    if (os.path.exists("avg_shortest_path.txt")):
        os.remove("avg_shortest_path.txt")

    f = open("avg_shortest_path.txt", "a")

    print("\t Finding the shortest path for 1000 random node pairs...")
    for i in range(1000):
        n1 = randint(0,1000)
        n2 = randint(0,1000)

        dist = shortest_path(G,n1,n2)
        distances.append(dist)

        f.write("({},{},{})\n".format(n1,n2,dist))

    f.close()
    print ("\t\tThe average distance is {}.\n".format(sum(distances)/len(distances)))


##########################################################
# Question 8d
##########################################################
def problem8d():
    if (os.path.exists("varying_p.txt")):
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
            n1 = randint(0,1000)
            n2 = randint(0,1000)

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
            n1 = randint(0,1000)
            n2 = randint(0,1000)

            dist = shortest_path(G,n1,n2)
            distances.append(dist)

        avg_distance = sum(distances)/len(distances)
        y.append(avg_distance)
        f.write("{}, {}\n".format(p,avg_distance))

    f.close()

    print("\t Plotting average distance as a function of p...")

    # Plot the average shortest path as a function of p
    plt.plot(x, y, color='blue', marker='o', linestyle='dashed', linewidth=2)
    plt.ylabel('Average Shortest Path')
    plt.xlabel('p')
    plt.show()


##########################################################
# Problem 9a
##########################################################
def problem9a():

    print("\t Building a graph from facebook combined data...")
    fb_G = create_fb_graph()

    distances = []

    if (os.path.exists("fb_shortest_path.txt")):
        os.remove("fb_shortest_path.txt")

    f = open("fb_shortest_path.txt", "a")

    print("\t Finding the shortest path for 1000 random node pairs...")
    for i in range(1000):
        n1 = randint(0,4039)
        n2 = randint(0,4039)

        dist = shortest_path(fb_G,n1,n2)
        distances.append(dist)

        f.write("({},{},{})\n".format(n1,n2,dist))

    f.close()
    print ("\t\tThe average distance is {}.".format(sum(distances)/len(distances)))


##########################################################
# Problem 9b
##########################################################
def problem9b():
    print("\t Building a graph from facebook combined data...")
    fb_G = create_fb_graph()

    iterations = 100000
    count = 0

    print("Estimating the probability that two random nodes are connected...")
    for i in range(iterations):
        n1 = randint(0,4039)
        n2 = randint(0,4039)

        # If the distance is 1 (n2 is in adjacencies of n1) increment count
        if (n2 in fb_G.neighbors(n1)):
            count += 1

    print ("\t\tThe probability is {}.".format(count/iterations))


##########################################################
# Problem 9c
##########################################################
def problem9c():

    print("\t Building a random graph...")
    G = create_graph(4039,0.01)

    distances = []

    print("\t Finding the shortest path for 1000 random node pairs...")
    for i in range(4039):
        n1 = randint(0,4039)
        n2 = randint(0,4039)

        dist = shortest_path(G,n1,n2)
        distances.append(dist)

    print ("\t\tThe average distance is {}.\n".format(sum(distances)/len(distances)))


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
    # print("Executing Problem 9b...")
    # problem9b()
    # print("Executing Problem 9c...")
    # problem9c()

main()
