# include any code you need for your assignment in this file or in auxiliary
# files that can be imported here.

import networkx as nx
from helper_functions import *

# 9 (a)
# implement an algorithm that given a bipartite graph G, outputs
# either a perfect matching or a constricted set
# Note: this will be used in 9 (b) so you can implement it however you
# like
def matching_or_cset(G):
    return -1

# 9 (b)
# implement an algorithm that given n (the number of players and items,
# which you can assume to just be labeled 0,1,...,n-1 in each case),
# and values where values[i][j] represents the ith players value for item j,
# output a market equilibrium consisting of prices and matching
# (p,M) where player i pays p[i] for item M[i].
def market_eq(n, values):
    p = [0]*n
    M = [0]*n
    return (p,M)

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
    print("Problem 9c Figure 8.3...")
    G = generateFigure8_3()
    s = matching_or_cset()
    print(s)


##########################################################
# Problem 10c
##########################################################
def problem10c():
    print("Problem 10c Figure 8.3...")
    G = generateFigure8_3()
    s = vcg()
    print(s)


# problem9c()
# problem10c()
