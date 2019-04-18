# include any code you need for your assignment in this file or in auxiliary
# files that can be imported here.

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
        # print(values)
        # print("--"*10)
        # print(m_or_c[0])
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
    for player in values:
        saved_values.append([x for x in player])

    # Get market equilibrium
    print(saved_values)
    (_,M) = market_eq(n, values)

    # Get social welfare of M
    SV = getSocialVal(saved_values,M)

    # Loop through players to price items
    for player,item in enumerate(M):
        # Get social welfare not including current player
        SV_no_player = SV - saved_values[player][item]
        # print("Social val: " + str(SV))
        # print("SV no player: " + str(SV_no_player))

        # Get values array without current player
        new_values = [x for i,x in enumerate(saved_values) if i!=player]

        # Add dummy players or items (items with value 0 or players with 0 value for everything)
        new_values.append([0]*m)
        # print("New values: " + str(new_values))

        # Get new market_eq without current player
        (_,new_M) = market_eq(n, new_values)
        # print("New eq: " + str(new_M))

        # Get the social welfare of the market_eq without the current player
        new_SV_no_player = getSocialVal(new_values,new_M) - saved_values[player][item]
        # print("New social val: " + str(new_SV_no_player))

        # Set the price that player pays p[i] to its externality
        p[player] = SV_no_player - new_SV_no_player

    print("p:" + str(p))
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
        for i in idx_of_max_val:
            item ="item_{}".format(i)
            G.add_edge(player, item)
            G.nodes[player]["bipartite"], G.nodes[item]["bipartite"] = 0, 1
    return G

# Find and returns social value given a matching M and values
def getSocialVal(values,M):
    SV = 0
    for player,item in enumerate(M):
        SV += values[player][item]
    return SV

# Finds and returns path of max flow
def max_flow(G, s, t):

    max_flow = 0

    # Get a path from s to t
    path = BFS(G, s, t)

    residual = G

    # While there is a path from source to sink
    while (path != None):

        # Push maximum flow along this path (minimum cap of edges)
        path_flow = float("Inf")
        for i in range(0, len(path)-1):
            if (residual[path[i]][path[i+1]]['cap'] < path_flow):
                path_flow = residual[path[i]][path[i+1]]['cap']

        # Increase max flow by max flow of current path
        max_flow += path_flow

        # Decrease capacity of each edge where flow was added
        # Create a reverse edge with capacity equal to the flow passed through that edge
        for i in range(0, len(path)-1):
            residual[path[i]][path[i+1]]['cap'] -= path_flow

            if (residual[path[i]][path[i+1]]['cap'] == 0):
                residual.remove_edge(path[i],path[i+1])

            if (residual.has_edge(path[i+1],path[i])):
                residual[path[i+1]][path[i]]['cap'] += path_flow
            else:
                residual.add_edge(path[i+1], path[i])
                residual[path[i+1]][path[i]]['cap'] = path_flow

        # plt.plot()
        # nx.draw(residual, with_labels=True, font_weight='bold')
        # plt.show()

        # Find a path from source to sink in new residual graph
        path = BFS(residual, s, t)

    return max_flow

# Breadth-First-Search algorithm
def BFS(G,i,j):
    # Check if source is target
    if (i == j):
      return None

    G.nodes[i]['previous'] = None

    discovered = []
    queue = [i]

    path = []

    while queue:
        temp = queue.pop(0)
        discovered.append(temp)
        neighbors = [n for n in list(G[temp]) if n not in queue and n not in discovered]
        for neighbor in neighbors:
            G.nodes[neighbor]['previous'] = temp
        if j in neighbors:
            n = j
            while (G.nodes[n]['previous'] != None):
                path.insert(0,n)
                n = G.nodes[n]['previous']
            path.insert(0,i)
            return path
        queue.extend(neighbors)

    return None


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
    f.write("Figure 8.3\n\tInputs: \n")
    f.write("\t\tn: " + str(len(figure83_values)) + "\n")
    f.write("\t\tvalues: " + str(figure83_values) + "\n")

    f.write("\tOutputs: \n")
    figure83_preferred_graph = get_preferred_graph(len(figure83_values),figure83_values)
    figure83_matching_or_cset = matching_or_cset(figure83_preferred_graph)
    if (figure83_matching_or_cset[1]):
        f.write("\t\tPerfect Matching: " + str(figure83_matching_or_cset[0]))
    else:
        f.write("\t\tConstricted Set: " + str(figure83_matching_or_cset[0]))

    f.write("\n\n")
    print("Done.")


    print("Calling matching_or_cset on Example 1...")
    f.write("Test Example 1\nInputs: \n")
    f.write("\t\tn: " + str(len(example1_values)) + "\n")
    f.write("\t\tvalues: " + str(example1_values) + "\n")

    f.write("\tOutputs: \n")
    example1_preferred_graph = get_preferred_graph(len(example1_values),example1_values)
    example1_matching_or_cset = matching_or_cset(example1_preferred_graph)
    if (example1_matching_or_cset[1]):
        f.write("\t\tPerfect Matching: " + str(example1_matching_or_cset[0]))
    else:
        f.write("\t\tConstricted Set: " + str(example1_matching_or_cset[0]))
    f.write("\n\n")
    print("Done.")


    print("Calling matching_or_cset on Example 2...")
    f.write("Test Example 2\nInputs: \n")
    f.write("\t\tn: " + str(len(example2_values)) + "\n")
    f.write("\t\tvalues: " + str(example2_values) + "\n")

    f.write("\tOutputs: \n")
    example2_preferred_graph = get_preferred_graph(len(example2_values),example2_values)
    example2_matching_or_cset = matching_or_cset(example2_preferred_graph)
    if (example2_matching_or_cset[1]):
        f.write("\t\tPerfect Matching: " + str(example2_matching_or_cset[0]))
    else:
        f.write("\t\tConstricted Set: " + str(example2_matching_or_cset[0]))
    f.write("\n\n")
    print("Done.")


    print("Calling matching_or_cset on Example 3...")
    f.write("Test Example 3\nInputs: \n")
    f.write("\t\tn: " + str(len(example3_values)) + "\n")
    f.write("\t\tvalues: " + str(example3_values) + "\n")

    f.write("\tOutputs: \n")
    example3_preferred_graph = get_preferred_graph(len(example3_values),example3_values)
    example3_matching_or_cset = matching_or_cset(example3_preferred_graph)
    if (example3_matching_or_cset[1]):
        f.write("\t\tPerfect Matching: " + str(example3_matching_or_cset[0]))
    else:
        f.write("\t\tConstricted Set: " + str(example3_matching_or_cset[0]))
    f.write("\n\n\n")
    print("Done.")


    f.write("MARKET_EQ TESTS\n\n")
    print("Calling market_eq on Figure 8.3...")
    f.write("Figure 8.3\n\tInputs: \n")
    f.write("\t\tn: " + str(len(figure83_values)) + "\n")
    f.write("\t\tvalues: " + str(figure83_values) + "\n")

    f.write("\tOutputs: \n")
    figure83_market_eq = market_eq(len(figure83_values),figure83_values)
    f.write("\t\tp: " + str(figure83_market_eq[0]) + "\n")
    f.write("\t\tM: " + str(figure83_market_eq[1]))
    f.write("\n\n")
    print("Done.")


    print("Calling market_eq on Example 1...")
    f.write("Test Example 1\n\tInputs: \n")
    f.write("\t\tn: " + str(len(example1_values)) + "\n")
    f.write("\t\tvalues: " + str(example1_values) + "\n")

    f.write("\tOutputs: \n")
    example1_market_eq = market_eq(len(example1_values),example1_values)
    f.write("\t\tp: " + str(example1_market_eq[0]) + "\n")
    f.write("\t\tM: " + str(example1_market_eq[1]))
    f.write("\n\n")
    print("Done.")


    print("Calling market_eq on Example 2...")
    f.write("Test Example 2\nInputs: \n")
    f.write("\t\tn: " + str(len(example2_values)) + "\n")
    f.write("\t\tvalues: " + str(example2_values) + "\n")

    f.write("\tOutputs: \n")
    example2_market_eq = market_eq(len(example2_values),example2_values)
    f.write("\t\tp: " + str(example2_market_eq) + "\n")
    f.write("\t\tM: " + str(example2_market_eq))
    f.write("\n\n")
    print("Done.")


    print("Calling market_eq on Example 3...")
    f.write("Test Example 3\nInputs: \n")
    f.write("\t\tn: " + str(len(example3_values)) + "\n")
    f.write("\t\tvalues: " + str(example3_values) + "\n")

    f.write("\tOutputs: \n")
    example3_market_eq = market_eq(len(example3_values),example3_values)
    f.write("\t\tp: " + str(example3_market_eq) + "\n")
    f.write("\t\tM: " + str(example3_market_eq))
    f.write("\n\n\n")
    print("Done.")

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
    f.write("Figure 8.3\n\tInputs: \n")
    f.write("\t\tn: " + str(len(figure83_values)) + "\n")
    f.write("\t\tm: " + str(len(figure83_values[0])) + "\n")
    f.write("\t\tvalues: " + str(figure83_values) + "\n")

    f.write("\tOutputs: \n")
    figure83_vcg = vcg(len(figure83_values),len(figure83_values[0]),figure83_values)
    f.write("\t\tp: " + str(figure83_vcg[0]) + "\n")
    f.write("\t\tM: " + str(figure83_vcg[1]) + "\n")

    f.write("\n\n")


    print("Calling vcg on Example 1...")
    f.write("Test Example 1\n\tInputs: \n")
    f.write("\t\tn: " + str(len(example1_values)) + "\n")
    f.write("\t\tm: " + str(len(example1_values[0])) + "\n")
    f.write("\t\tvalues: " + str(example1_values) + "\n")

    f.write("\tOutputs: \n")
    example1_vcg = vcg(len(example1_values),len(example1_values[0]),example1_values)
    f.write("\t\tp: " + str(example1_vcg[0]) + "\n")
    f.write("\t\tM: " + str(example1_vcg[1]) + "\n")

    f.write("\n\n")


    print("Calling vcg on Example 2...")
    f.write("Test Example 2\n\tInputs: \n")
    f.write("\t\tn: " + str(len(example2_values)) + "\n")
    f.write("\t\tm: " + str(len(example2_values[0])) + "\n")
    f.write("\t\tvalues: " + str(example2_values) + "\n")

    f.write("\tOutputs: \n")
    example2_vcg = vcg(len(example2_values),len(example2_values[0]),example2_values)
    f.write("\t\tp: " + str(example2_vcg[0]) + "\n")
    f.write("\t\tM: " + str(example2_vcg[1]) + "\n")

    f.write("\n\n")


    print("Calling vcg on Example 3...")
    f.write("Test Example 3\n\tInputs: \n")
    f.write("\t\tn: " + str(len(example3_values)) + "\n")
    f.write("\t\tm: " + str(len(example3_values[0])) + "\n")
    f.write("\t\tvalues: " + str(example3_values) + "\n")

    f.write("\tOutputs: \n")
    example3_vcg = vcg(len(example3_values),len(example3_values[0]),example3_values)
    f.write("\t\tp: " + str(example3_vcg[0]) + "\n")
    f.write("\t\tM: " + str(example3_vcg[1]) + "\n")

    f.write("\n\n")
    print("Done.")

    f.close()


##########################################################
# Problem 11b
##########################################################
def problem11b():
    print("Problem 11b...")
    print("Done.")


problem9c()
problem10c()
# problem11b()
