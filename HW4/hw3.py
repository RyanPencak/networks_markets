# include any code you need for your assignment in this file or in auxiliary
# files that can be imported here.
import os
import networkx as nx
from networkx.algorithms.flow import shortest_augmenting_path

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
            if edge[0] != "source" and edge[1] != "sink" and edge[2]["flow"] > 0:
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
            return (True, p,M)
        # print(values)
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

        count = 0
        for v in values:
            if sum(1 for i in v if i < 0) == len(v):
                return (False, count)
            count += 1

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
        for i in idx_of_max_val:
            item ="item_{}".format(i)
            G.add_edge(player, item)
            G.nodes[player]["bipartite"], G.nodes[item]["bipartite"] = 0, 1
    return G
