import os
import networkx as nx
import matplotlib.pyplot as plt


# Create graph from figure 6.1
def create_figure6_1():
    G=nx.DiGraph()

    plt.plot()
    G.add_nodes_from([1,2,3,4])
    G.add_edge(1,2)
    G[1][2]['cap'] = 1
    G.add_edge(1,3)
    G[1][3]['cap'] = 3
    G.add_edge(2,3)
    G[2][3]['cap'] = 2
    G.add_edge(2,4)
    G[2][4]['cap'] = 1
    G.add_edge(3,4)
    G[3][4]['cap'] = 1
    nx.draw(G, with_labels=True, font_weight='bold')
    # plt.show()

    return G


# Create graph from figure 6.3
def create_figure6_3():
    G=nx.DiGraph()

    plt.plot()
    G.add_nodes_from([1,2,3,4,5,6,7,8,9,10,11,12])
    G.add_edge(1,2)
    G.add_edge(1,3)
    G.add_edge(1,4)
    G.add_edge(1,5)
    G.add_edge(1,6)

    G.add_edge(2,8)
    G.add_edge(3,7)
    G.add_edge(3,8)
    G.add_edge(4,7)
    G.add_edge(5,9)
    G.add_edge(5,11)
    G.add_edge(6,9)
    G.add_edge(6,10)

    G.add_edge(8,2)
    G.add_edge(7,3)
    G.add_edge(8,3)
    G.add_edge(7,4)
    G.add_edge(9,5)
    G.add_edge(11,5)
    G.add_edge(9,6)
    G.add_edge(10,6)

    G.add_edge(7,12)
    G.add_edge(8,12)
    G.add_edge(9,12)
    G.add_edge(10,12)
    G.add_edge(11,12)
    nx.draw(G, with_labels=True, font_weight='bold')
    # plt.show()

    return G


# Create and return a directed graph from facebook data
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
