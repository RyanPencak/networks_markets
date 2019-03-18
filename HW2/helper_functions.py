import os
import networkx as nx
import matplotlib.pyplot as plt


# Create graph from figure 6.1
def create_figure6_1():
    G=nx.DiGraph()

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

    plt.plot()
    nx.draw(G, with_labels=True, font_weight='bold')
    # plt.show()

    return G


# Create graph from figure 6.3
def create_figure6_3():
    G=nx.DiGraph()

    G.add_nodes_from([1,2,3,4,5,6,7,8,9,10,11,12])
    G.add_edge(1,2)
    G[1][2]['cap'] = 1
    G.add_edge(1,3)
    G[1][3]['cap'] = 1
    G.add_edge(1,4)
    G[1][4]['cap'] = 1
    G.add_edge(1,5)
    G[1][5]['cap'] = 1
    G.add_edge(1,6)
    G[1][6]['cap'] = 1

    G.add_edge(2,8)
    G[2][8]['cap'] = 1
    G.add_edge(3,7)
    G[3][7]['cap'] = 1
    G.add_edge(3,8)
    G[3][8]['cap'] = 1
    G.add_edge(4,7)
    G[4][7]['cap'] = 1
    G.add_edge(5,9)
    G[5][9]['cap'] = 1
    G.add_edge(5,11)
    G[5][11]['cap'] = 1
    G.add_edge(6,9)
    G[6][9]['cap'] = 1
    G.add_edge(6,10)
    G[6][10]['cap'] = 1

    G.add_edge(8,2)
    G[8][2]['cap'] = 1
    G.add_edge(7,3)
    G[7][3]['cap'] = 1
    G.add_edge(8,3)
    G[8][3]['cap'] = 1
    G.add_edge(7,4)
    G[7][4]['cap'] = 1
    G.add_edge(9,5)
    G[9][5]['cap'] = 1
    G.add_edge(11,5)
    G[11][5]['cap'] = 1
    G.add_edge(9,6)
    G[9][6]['cap'] = 1
    G.add_edge(10,6)
    G[10][6]['cap'] = 1

    G.add_edge(7,12)
    G[7][12]['cap'] = 1
    G.add_edge(8,12)
    G[8][12]['cap'] = 1
    G.add_edge(9,12)
    G[9][12]['cap'] = 1
    G.add_edge(10,12)
    G[10][12]['cap'] = 1
    G.add_edge(11,12)
    G[11][12]['cap'] = 1

    plt.plot()
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


def create_q_5_fig_1():
    G = nx.Graph()

    G.add_edge("g", "h")
    G.add_edge("h", "c")
    G.add_edge("h", "m")
    G.add_edge("c", "e")
    G.add_edge("c", "d")
    G.add_edge("m", "k")
    G.add_edge("m", "n")
    G.add_edge("e", "k")
    G.add_edge("e", "f")
    G.add_edge("k", "f")
    G.add_edge("k", "l")
    G.add_edge("f", "l")
    G.add_edge("f", "d")
    G.add_edge("l", "n")
    G.add_edge("n", "i")
    G.add_edge("d", "i")
    G.add_edge("i", "j")

    return G

def create_figure4_1_1():
    G = nx.Graph()
    G.add_edge("a", "b")
    G.add_edge("b", "c")
    G.add_edge("c", "d")

    return G

def create_figure4_1_2():
    G = nx.Graph()
    G.add_edge("a", "b")
    G.add_edge("b", "c")
    G.add_edge("b", "d")
    G.add_edge("d", "e")
    G.add_edge("d", "f")
    G.add_edge("f", "g")

    return G



