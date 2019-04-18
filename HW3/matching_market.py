# include any code you need for your assignment in this file or in auxiliary
# files that can be imported here.

# include any code you need for your assignment in this file or in auxiliary
# files that can be imported here.
import os
import networkx as nx
from networkx.algorithms.flow import shortest_augmenting_path
from helper_functions import *

def gen_di_graph(G):
    DG = nx.DiGraph()
    for n, d in G.nodes(data=True):
        if d["bipartite"] == 0:
            DG.add_edge("source", n, capacity=1)
            DG.nodes[n]["bipartite"] = 0
            for adj_node in G[n]:
                DG.add_edge(n, adj_node)
        elif d["bipartite"] == 1:
            DG.add_edge(n, "sink", capacity=1)
            DG.nodes[n]["bipartite"] = 1
    return DG

def get_preferred_graph(n, values):
    G = nx.Graph()
    for i in range(n):
        max_val, count = 0, 0
        idx_of_max_val = count
        print(values)
        for val in values[i]:
            if val > max_val:
                max_val = val
                idx_of_max_val = count
            count += 1
        player = "player_{}".format(i)
        item = "item_{}".format(idx_of_max_val)
        G.add_edge(player, item)
        G.nodes[player]["bipartite"], G.nodes[item]["bipartite"] = 0, 1
    return G

# 9 (a)
# implement an algorithm that given a bipartite graph G, outputs
# either a perfect matching or a constricted set
# Note: this will be used in 9 (b) so you can implement it however you
# like

# Double check: is it legit to use min cut?
def matching_or_cset(G):
    DG = gen_di_graph(G)
    min_f, part = nx.minimum_cut(DG, "source", "sink")
    num_xs = len([n for n, d in G.nodes(data=True) if d["bipartite"]==0])
    num_ys = len([n for n, d in G.nodes(data=True) if d["bipartite"]==1])
    residual = shortest_augmenting_path(DG, "source", "sink")
    if num_xs == num_ys and num_xs == min_f:
        ret = []
        for edge in residual.edges.data():
            if edge[0] != "source" and edge[1] != "sink" and edge[2]["flow"] > 0:
                ret.append((edge[0], edge[1]))
        return (ret, True)
    return ([x for x in part[0] if x!="source" and x!="sink" and DG.nodes[x]["bipartite"]==0], False)

# 9 (b)
# implement an algorithm that given n (the number of players and items,
# which you can assume to just be labeled 0,1,...,n-1 in each case),
# and values where values[i][j] represents the ith players value for item j,
# output a market equilibrium consisting of prices and matching
# (p,M) where player i pays p[i] for item M[i].
def market_eq(n, values):
    p = [0]*n
    M = [0]*n
    while True:
        preferred = get_preferred_graph(n, values)
        m_or_c = matching_or_cset(preferred)
        if m_or_c[1]:
            for edge in m_or_c[0]:
                M[int(edge[0].split("_")[1])] = int(edge[1].split("_")[1])
            return (p,M)
        neighbors_incremented = []
        for constrict in m_or_c[0]:
            for neighbor in preferred[constrict]:
                if neighbor not in neighbors_incremented:
                    value_index = int(neighbor.split("_")[1])
                    for i in range(n):
                        values[i][value_index] -= 1
                    p[value_index] += 1
                    neighbors_incremented.append(neighbor)
        count = 0
        for i in p:
            if i > 0: count += 1
        if count == len(p):
            for i in range(len(p)):
                p[i] -= 1



# 10 (b)
# Given n players 0,...,n-1 and m items 0,...,m-1 and valuations
# values such that values[i][j] is player i's valuation for item j,
# implement the VCG mechanism with Clarke pivot rule that outputs
# a set of prices and assignments (p,M) such that player i pays p[i]
# (which should be positive) for item M[i].
def vcg(n, m, values):
    p = [0]*n
    M = [0]*n
    return (p,M)


##########################################################
# Problem 9c
##########################################################
def problem9c():

    (figure83_values) = generateFigure8_3()
    (example1_values) = generateTestExample1()
    (example2_values) = generateTestExample2()
    (example3_values) = generateTestExample3()

    if (os.path.exists("p9.txt")):
        os.remove("p9.txt")

    f = open("p9.txt", "a")

    f.write("MATCHING_OR_CSET TESTS\n\n")
    print("Calling matching_or_cset on Figure 8.3...")
    f.write("Figure 8.3\n\tInputs: \n")
    f.write("\t\tn: " + str(len(figure83_values)) + "\n")
    f.write("\t\tvalues: " + str(figure83_values) + "\n")

    f.write("\tOutputs: \n")
    figure83_preferred_graph = get_preferred_graph(len(figure83_values),figure83_values)
    figure83_matching_or_cset = matching_or_cset(figure83_preferred_graph)
    if (figure83_matching_or_cset[1]):
        f.write("\t\tConstricted Set: " + str(figure83_matching_or_cset[0]))
    else:
        f.write("\t\tPerfect Matching: " + str(figure83_matching_or_cset[0]))

    f.write("\n\n")


    print("Calling matching_or_cset on Example 1...")
    f.write("Test Example 1\nInputs: ")
    f.write("\n")

    f.write("Outputs: ")
    f.write("\n\n")


    print("Calling matching_or_cset on Example 2...")
    f.write("Test Example 2\nInputs: ")
    f.write("\n")

    f.write("Outputs: ")
    f.write("\n\n")


    print("Calling matching_or_cset on Example 3...")
    f.write("Test Example 3\nInputs: ")
    f.write("\n")

    f.write("Outputs: ")
    f.write("\n\n\n")


    f.write("MARKET_EQ TESTS\n\n")
    print("Calling market_eq on Figure 8.3...")
    f.write("Figure 8.3\nInputs: ")
    f.write("\n")
    # figure83_market_eq = market_eq(figure83_n,figure83_values)

    f.write("Outputs: ")
    f.write("\n\n")


    print("Calling market_eq on Example 1...")
    f.write("Test Example 1\nInputs: ")
    f.write("\n")

    f.write("Outputs: ")
    f.write("\n\n")


    print("Calling market_eq on Example 2...")
    f.write("Test Example 2\nInputs: ")
    f.write("\n")

    f.write("Outputs: ")
    f.write("\n\n")


    print("Calling market_eq on Example 3...")
    f.write("Test Example 3\nInputs: ")
    f.write("\n")

    f.write("Outputs: ")
    f.write("\n\n\n")

    f.close()


##########################################################
# Problem 10c
##########################################################
def problem10c():
    if (os.path.exists("p10.txt")):
        os.remove("p10.txt")

    f = open("p10.txt", "a")

    f.write("VCG TESTS\n\n")
    print("Calling vcg on Figure 8.3...")
    f.write("Figure 8.3\n\tInputs: \n")
    f.write("\t\tn: " + str(len(figure83_values)) + "\n")
    f.write("\t\tm: " + str(len(figure83_values[0])) + "\n")
    f.write("\t\tvalues: " + str(figure83_values) + "\n")

    f.write("\tOutputs: ")
    figure83_vcg = vcg(len(figure83_values),len(figure83_values[0]),figure83_values)
    f.write("\t\tp: " + figure83_vcg[0])
    f.write("\t\tM: " + figure83_vcg[1])

    f.write("\n\n")


    print("Calling matching_or_cset on Example 1...")
    f.write("Test Example 1\nInputs: ")
    f.write("\n")

    f.write("Outputs: ")
    f.write("\n\n")


    print("Calling matching_or_cset on Example 2...")
    f.write("Test Example 2\nInputs: ")
    f.write("\n")

    f.write("Outputs: ")
    f.write("\n\n")


    print("Calling matching_or_cset on Example 3...")
    f.write("Test Example 3\nInputs: ")
    f.write("\n")

    f.write("Outputs: ")
    f.write("\n")

    f.close()

    # G = generateFigure8_3()
    # s = vcg()
    # print(s)


##########################################################
# Problem 11b
##########################################################
def problem11b():
    print("Problem 10c Figure 8.3...")
    G = generateFigure8_3()
    s = vcg()
    print(s)


problem9c()
# problem10c()
# problem11b()
