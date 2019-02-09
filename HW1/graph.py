# include any code you need for your assignment in this file or in auxiliary
# files that can be imported here.

from numpy.random import choice, randint
import itertools

# given number of nodes n and probability p, output a random graph
# as specified in homework
def create_graph(n,p):
    G = {}

    # Initialize undirected graph adjacency list
    for i in range(1,n+1):
        G[int("{}".format(i))] = []

    # Create list of nodes
    node_list = []
    for i in range(1,n+1):
        node_list.append(i)

    # For each combination of nodes, determine if there is an edge
    for pair in itertools.combinations(node_list,2):
        if (choice([True,False], 1, p=[p,1-p])):
            G[pair[0]].append((pair[1], randint(1,101)))

    return G

# given a graph G and nodes i,j, output the length of the shortest
# path between i and j in G.
def shortest_path(G,i,j):

    # Check if source is target
    if (i == j):
      return 0

    # Array for visited nodes, originally containing the source in format (node, back pointer, weight)
    visited = [(i,None,None)]

    # Store neighbor nodes and distance to it
    discovered = {}

    while (len(visited) != 0):
        temp = visited.pop(0)
        if (temp[0] not in list(discovered.keys())):
            discovered[temp[0]] = (temp[1],temp[2])
            for (node, weight) in G[temp[0]]:
                visited.append((node, temp[0], weight))

    if (j in list(discovered.keys())):
        back_reference = discovered[j][0]
        distance = discovered[j][1]

        while (back_reference != i):
            cur = back_reference
            back_reference = discovered[cur][0]
            distance += discovered[cur][1]

        return distance

    else:
        return float("inf")

    return None


# main function creates a graph and finds the shortest path
def main(n,p):
    G = create_graph(n,p)

    f = open("test_output.txt", "a")

    for i in range(5):
        n1 = randint(1,n+1)
        n2 = randint(1,n+1)

        dist = shortest_path(G,n1,n2)

        f.write("({},{},{})\n".format(n1,n2,dist))

main(1000,0.1)
