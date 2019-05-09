# include any code you need for your assignment in this file or in auxiliary
# files that can be imported here.
import os
import networkx as nx
from networkx.algorithms.flow import shortest_augmenting_path
from helper_functions import *

# 9 (a)
# implement an algorithm that given a bipartite graph G, outputs
# either a perfect matching or a constricted set
# Note: this will be used in 9 (b) so you can implement it however you
# like
def matching_or_cset(G):
    DG = gen_di_graph(G)
    # Use networkx min cut to find matching or constricted set
    min_f, part = nx.minimum_cut(DG, "source", "sink")
    num_xs = len([n for n, d in G.nodes(data=True) if d["bipartite"]==0])
    num_ys = len([n for n, d in G.nodes(data=True) if d["bipartite"]==1])
    residual = shortest_augmenting_path(DG, "source", "sink")
    if num_xs == num_ys and num_xs == min_f:
        ret = []
        for edge in residual.edges.data():
            if (edge[0] != "source" and edge[1] != "sink" and edge[1] != "source" 
                and edge[1] != "sink" and edge[2]["flow"] > 0):
                ret.append((edge[0], edge[1]))
        return (ret, True) # return matching set and True
    return ([x for x in part[0] if x!="source" and x!="sink" and DG.nodes[x]["bipartite"]==0], False) # return constricted set and False

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
        preferred = get_preferred_graph(n, values) # get the preferred graph with n and values
        m_or_c = matching_or_cset(preferred) # use 9a function to find matching or constricted set in preferred graph
        if m_or_c[1]: # if there is a matching set, return (p,M)
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
                for j in range(n):
                    values[j][i] += 1

# 10 (b)
# Given n players 0,...,n-1 and m items 0,...,m-1 and valuations
# values such that values[i][j] is player i's valuation for item j,
# implement the VCG mechanism with Clarke pivot rule that outputs
# a set of prices and assignments (p,M) such that player i pays p[i]
# (which should be positive) for item M[i].
def vcg(n, m, values):
    p = [0]*n
    M = [0]*n

    # Store original values
    saved_values = []
    for i in values:
        temp_player1 = []
        for item_value in i:
            temp_player1.append(item_value)
        saved_values.append(temp_player1)

    # Get market equilibrium
    (_,M) = market_eq(n, values)

    # Get social welfare of M
    SV = getSocialVal(saved_values,M)

    # Loop through players to price items
    for player,item in enumerate(M):
        # Get social welfare not including current player
        SV_no_player = SV - saved_values[player][item]

        # Get values array without current player
        new_values = []
        for idx,i in enumerate(saved_values):
            temp_player2 = []
            if (idx != player):
                for item_value in i:
                    temp_player2.append(item_value)
                new_values.append(temp_player2)
            else:
                # Add dummy players or items (items with value 0 or players with 0 value for everything)
                new_values.append([0]*m)

        # Store original values before calling market_eq
        saved_new_values = []
        for i in new_values:
            temp_player3 = []
            for item_value in i:
                temp_player3.append(item_value)
            saved_new_values.append(temp_player3)

        # Get new market_eq without current player
        (_,new_M) = market_eq(n, new_values)

        # Get the social value of the market_eq without the current player
        new_SV_no_player = getSocialVal(saved_new_values,new_M)

        # Set the price that player pays p[i] to its externality
        p[player] = new_SV_no_player - SV_no_player

    return (p,M)


# Takes in a graph and returns digraph representation
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

# Takes number of players n and values array, returning the preferred graph
def get_preferred_graph(n, values):
    G = nx.Graph()
    for i in range(n):
        max_val, count = 0, 0
        idx_of_max_val = [count]
        for val in values[i]:
            if val > max_val:
                max_val = val
                idx_of_max_val = [count]
            elif val == max_val:
                idx_of_max_val.append(count)
            count += 1
        player = "player_{}".format(i)
        for j in idx_of_max_val:
            item ="item_{}".format(j)
            G.add_edge(player, item)
            G.nodes[player]["bipartite"], G.nodes[item]["bipartite"] = 0, 1
    return G

# Find and returns social value given a matching M and values
def getSocialVal(values,M):
    SV = 0
    for player,item in enumerate(M):
        SV += values[player][item]
    return SV


##########################################################
# Problem 9c
##########################################################
def problem9c():

    figure83_values = generateFigure8_3()
    example1_values = generateTestExample1()
    example2_values = generateTestExample2()
    example3_values = generateTestExample3()

    if (os.path.exists("p9.txt")):
        os.remove("p9.txt")

    f = open("p9.txt", "a")

    f.write("MATCHING_OR_CSET TESTS\n\n")
    print("Calling matching_or_cset on Figure 8.3...")
    f.write("Figure 8.3\n---------------\nInputs: \n")
    f.write("n: " + str(len(figure83_values)) + "\n")
    f.write("values: " + str(figure83_values) + "\n")

    f.write("\nOutputs: \n")
    figure83_preferred_graph = get_preferred_graph(len(figure83_values),figure83_values)
    figure83_matching_or_cset = matching_or_cset(figure83_preferred_graph)
    if (figure83_matching_or_cset[1]):
        f.write("Perfect Matching: " + str(figure83_matching_or_cset[0]))
        print("\tPerfect Matching: " + str(figure83_matching_or_cset[0]))
    else:
        f.write("Constricted Set: " + str(figure83_matching_or_cset[0]))
        print("\tConstricted Set: " + str(figure83_matching_or_cset[0]))

    f.write("\n\n")
    print("Done.\n\n")


    print("Calling matching_or_cset on Example 1...")
    f.write("Test Example 1\n---------------\nInputs: \n")
    f.write("n: " + str(len(example1_values)) + "\n")
    f.write("values: " + str(example1_values) + "\n")

    f.write("\nOutputs: \n")
    example1_preferred_graph = get_preferred_graph(len(example1_values),example1_values)
    example1_matching_or_cset = matching_or_cset(example1_preferred_graph)
    if (example1_matching_or_cset[1]):
        f.write("Perfect Matching: " + str(example1_matching_or_cset[0]))
        print("\tPerfect Matching: " + str(example1_matching_or_cset[0]))
    else:
        f.write("Constricted Set: " + str(example1_matching_or_cset[0]))
        print("\tConstricted Set: " + str(example1_matching_or_cset[0]))
    f.write("\n\n")
    print("Done.\n\n")


    print("Calling matching_or_cset on Example 2...")
    f.write("Test Example 2\n---------------\nInputs: \n")
    f.write("n: " + str(len(example2_values)) + "\n")
    f.write("values: " + str(example2_values) + "\n")

    f.write("\nOutputs: \n")
    example2_preferred_graph = get_preferred_graph(len(example2_values),example2_values)
    example2_matching_or_cset = matching_or_cset(example2_preferred_graph)
    if (example2_matching_or_cset[1]):
        f.write("Perfect Matching: " + str(example2_matching_or_cset[0]))
        print("\tPerfect Matching: " + str(example2_matching_or_cset[0]))
    else:
        f.write("Constricted Set: " + str(example2_matching_or_cset[0]))
        print("\tConstricted Set: " + str(example2_matching_or_cset[0]))
    f.write("\n\n")
    print("Done.\n\n")


    print("Calling matching_or_cset on Example 3...")
    f.write("Test Example 3\n---------------\nInputs: \n")
    f.write("n: " + str(len(example3_values)) + "\n")
    f.write("values: " + str(example3_values) + "\n")

    f.write("\nOutputs: \n")
    example3_preferred_graph = get_preferred_graph(len(example3_values),example3_values)
    example3_matching_or_cset = matching_or_cset(example3_preferred_graph)
    if (example3_matching_or_cset[1]):
        f.write("Perfect Matching: " + str(example3_matching_or_cset[0]))
        print("\tPerfect Matching: " + str(example3_matching_or_cset[0]))
    else:
        f.write("Constricted Set: " + str(example3_matching_or_cset[0]))
        print("\tConstricted Set: " + str(example3_matching_or_cset[0]))
    f.write("\n\n\n")
    print("Done.\n\n")


    f.write("MARKET_EQ TESTS\n\n")
    print("Calling market_eq on Figure 8.3...")

    f.write("Figure 8.3\n---------------\nInputs: \n")
    f.write("n: " + str(len(figure83_values)) + "\n")
    f.write("values: " + str(figure83_values) + "\n")

    f.write("\nOutputs: \n")
    figure83_market_eq = market_eq(len(figure83_values),figure83_values)
    f.write("p: " + str(figure83_market_eq[0]) + "\n")
    f.write("M: " + str(figure83_market_eq[1]))
    print("\tp: " + str(figure83_market_eq[0]))
    print("\tM: " + str(figure83_market_eq[1]))
    f.write("\n\n")
    print("Done.\n\n")


    print("Calling market_eq on Example 1...")
    f.write("Test Example 1\n---------------\nInputs: \n")
    f.write("n: " + str(len(example1_values)) + "\n")
    f.write("values: " + str(example1_values) + "\n")

    f.write("\nOutputs: \n")
    example1_market_eq = market_eq(len(example1_values),example1_values)
    f.write("p: " + str(example1_market_eq[0]) + "\n")
    f.write("M: " + str(example1_market_eq[1]))
    print("\tp: " + str(example1_market_eq[0]))
    print("\tM: " + str(example1_market_eq[1]))
    f.write("\n\n")
    print("Done.\n\n")


    print("Calling market_eq on Example 2...")
    f.write("Test Example 2\n---------------\nInputs: \n")
    f.write("n: " + str(len(example2_values)) + "\n")
    f.write("values: " + str(example2_values) + "\n")

    f.write("\nOutputs: \n")
    example2_market_eq = market_eq(len(example2_values),example2_values)
    f.write("p: " + str(example2_market_eq[0]) + "\n")
    f.write("M: " + str(example2_market_eq[1]))
    print("\tp: " + str(example2_market_eq[0]))
    print("\tM: " + str(example2_market_eq[1]))
    f.write("\n\n")
    print("Done.\n\n")


    print("Calling market_eq on Example 3...")
    f.write("Test Example 3\n---------------\nInputs: \n")
    f.write("n: " + str(len(example3_values)) + "\n")
    f.write("values: " + str(example3_values) + "\n")

    f.write("\nOutputs: \n")
    example3_market_eq = market_eq(len(example3_values),example3_values)
    f.write("p: " + str(example3_market_eq[0]) + "\n")
    f.write("M: " + str(example3_market_eq[1]))
    print("\tp: " + str(example3_market_eq[0]))
    print("\tM: " + str(example3_market_eq[1]))
    print("Done.\n\n")

    f.close()


##########################################################
# Problem 10c
##########################################################
def problem10c():

    figure83_values = generateFigure8_3()
    example1_values = generateTestExample1()
    example2_values = generateTestExample2()
    example3_values = generateTestExample3()

    if (os.path.exists("p10.txt")):
        os.remove("p10.txt")

    f = open("p10.txt", "a")

    f.write("VCG TESTS\n\n")
    print("Calling vcg on Figure 8.3...")
    f.write("Figure 8.3\n---------------\nInputs: \n")
    f.write("n: " + str(len(figure83_values)) + "\n")
    f.write("m: " + str(len(figure83_values[0])) + "\n")
    f.write("values: " + str(figure83_values) + "\n")

    f.write("\nOutputs: \n")
    figure83_vcg = vcg(len(figure83_values),len(figure83_values[0]),figure83_values)
    f.write("p: " + str(figure83_vcg[0]) + "\n")
    f.write("M: " + str(figure83_vcg[1]) + "\n")
    print("\tp: " + str(figure83_vcg[0]))
    print("\tM: " + str(figure83_vcg[1]))
    print("Done.\n\n")

    f.write("\n\n")


    print("Calling vcg on Example 1...")
    f.write("Test Example 1\n---------------\nInputs: \n")
    f.write("n: " + str(len(example1_values)) + "\n")
    f.write("m: " + str(len(example1_values[0])) + "\n")
    f.write("values: " + str(example1_values) + "\n")

    f.write("\nOutputs: \n")
    example1_vcg = vcg(len(example1_values),len(example1_values[0]),example1_values)
    f.write("p: " + str(example1_vcg[0]) + "\n")
    f.write("M: " + str(example1_vcg[1]) + "\n")
    print("\tp: " + str(example1_vcg[0]))
    print("\tM: " + str(example1_vcg[1]))
    print("Done.\n\n")

    f.write("\n\n")


    print("Calling vcg on Example 2...")
    f.write("Test Example 2\n---------------\nInputs: \n")
    f.write("n: " + str(len(example2_values)) + "\n")
    f.write("m: " + str(len(example2_values[0])) + "\n")
    f.write("values: " + str(example2_values) + "\n")

    f.write("\nOutputs: \n")
    example2_vcg = vcg(len(example2_values),len(example2_values[0]),example2_values)
    f.write("p: " + str(example2_vcg[0]) + "\n")
    f.write("M: " + str(example2_vcg[1]) + "\n")
    print("\tp: " + str(example2_vcg[0]))
    print("\tM: " + str(example2_vcg[1]))
    print("Done.\n\n")

    f.write("\n\n")


    print("Calling vcg on Example 3...")
    f.write("Test Example 3\n---------------\nInputs: \n")
    f.write("n: " + str(len(example3_values)) + "\n")
    f.write("m: " + str(len(example3_values[0])) + "\n")
    f.write("values: " + str(example3_values) + "\n")

    f.write("\nOutputs: \n")
    example3_vcg = vcg(len(example3_values),len(example3_values[0]),example3_values)
    f.write("p: " + str(example3_vcg[0]) + "\n")
    f.write("M: " + str(example3_vcg[1]) + "\n")
    print("\tp: " + str(example3_vcg[0]))
    print("\tM: " + str(example3_vcg[1]))
    print("Done.\n\n")

    f.close()


##########################################################
# Problem 11b
##########################################################
def problem11b():
    if (os.path.exists("p11.txt")):
        os.remove("p11.txt")

    f = open("p11.txt", "a")

    print("Problem 11a...")
    bundle_values = []
    player_values_for_items = [2,3,47,38,25,8,36,41,12,23,13,13,13,12,30,15,3,16,8,11]
    for player in range(20):
        p_values = [i*player_values_for_items[player] for i in range(1,21,1)]
        bundle_values.append(p_values)
    print("\tPlayers: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]")
    print("\tRandom Player Values for the Item: [2,3,47,38,25,8,36,41,12,23,13,13,13,12,30,15,3,16,8,11]")
    print("\tValues of Item Bundles for Each Player: [[1*2,2*2,3*2,...][1*3,2*3,3*3,...][1*47,2*47,3*47,...][1*38,2*38,3*38,...]...]")
    print("\tGenerated Values: " + str(bundle_values))

    f.write("Problem 11a\n---------------\n\n")
    f.write("Players: [1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]\n")
    f.write("Random Player Values for the Item: [2,3,47,38,25,8,36,41,12,23,13,13,13,12,30,15,3,16,8,11]\n")
    f.write("Values of Item Bundles for Each Player: [[1*2,2*2,3*2,...][1*3,2*3,3*3,...][1*47,2*47,3*47,...][1*38,2*38,3*38,...]...]\n\n")

    f.write("Problem 11b\n---------------\n\n")
    f.write("Inputs: \n")
    f.write("n: " + str(len(bundle_values)) + "\n")
    f.write("m: " + str(len(bundle_values[0])) + "\n")
    f.write("values: " + str(bundle_values) + "\n\n")

    print("\nProblem 11b...")
    (p_problem11,M_problem11) = vcg(len(bundle_values),len(bundle_values[0]),bundle_values)
    f.write("\nOutputs: \n")
    f.write("p: " + str(p_problem11) + "\n")
    f.write("M: " + str(M_problem11) + "\n")
    print("\tp: " + str(p_problem11))
    print("\tM: " + str(M_problem11))
    print("Done.\n\n")


problem9c()
problem10c()
problem11b()
