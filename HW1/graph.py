# include any code you need for your assignment in this file or in auxiliary
# files that can be imported here.

import networkx as nx
import itertools
from numpy.random import choice, randint

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

# create graph from Facebook data
def create_fb_graph():
    G=nx.Graph()

    with open("facebook_combined.txt") as in_file:
        node_list = in_file.readlines()
        node_list = [x.strip().split() for x in node_list]

        for node_pair in node_list:
            node_pair[0] = int(node_pair[0])
            node_pair[1] = int(node_pair[1])

    # Create edges for each pair
    for node_pair in node_list:
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



# main function for each homework problem
def main():
    ##########################################################
    # Question 8c
    ##########################################################
    G = create_graph(1000,0.1)

    distances = []

    f = open("avg_shortest_path.txt", "a")

    for i in range(1000):
        n1 = randint(1,1001)
        n2 = randint(1,1001)

        dist = shortest_path(G,n1,n2)

        distances.append(dist)

        f.write("({},{},{})\n".format(n1,n2,dist))

    f.close()
    print ("The average distance is {}.".format(sum(distances)/len(distances)))

    ##########################################################
    # Question 8d
    ##########################################################
    # G = create_graph(1000,0.1)
    #
    # distances = []
    #
    # f = open("avg_shortest_path.txt", "a")
    #
    # for i in range(1000):
    #     n1 = randint(1,1001)
    #     n2 = randint(1,1001)
    #
    #     dist = shortest_path(G,n1,n2)
    #     distances.append(dist)
    #
    #     avg_path = sum(distances)/len(distances)
    #
    #     f.write("({},{},{})\n".format(p,avg_path,dist))
    #
    # f.close()

    ##########################################################
    # Question 9a
    ##########################################################
    # fb_G = create_fb_graph
    #
    # distances = []
    #
    # f = open("fb_shortest_path.txt", "a")
    #
    # for i in range(1000):
    #     n1 = randint(1,1001)
    #     n2 = randint(1,1001)
    #
    #     dist = shortest_path(G,n1,n2)
    #
    #     distances.append(dist)
    #
    #     f.write("({},{},{})\n".format(n1,n2,dist))
    #
    # f.close()
    # print "The average distance is {}.".format(sum(distances)/len(distances))
