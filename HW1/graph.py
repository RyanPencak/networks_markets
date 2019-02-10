# include any code you need for your assignment in this file or in auxiliary
# files that can be imported here.

from numpy.random import choice, randint
import itertools

# given number of nodes n and probability p, output a random graph
# as specified in homework
def create_graph(n,p,fb=False):
    G = {}

    # Initialize undirected graph adjacency list
    for i in range(1,n+1):
        G[int("{}".format(i))] = []

    # If using Facebook data read from file for nodes, else generate nodes
    if (fb):
        with open("facebook_combined.txt") as in_file:
            node_list = in_file.readlines()
            node_list = [x.strip().split() for x in node_list]

            for node_pair in node_list:
                node_pair[0] = int(node_pair[0])
                node_pair[1] = int(node_pair[1])

        # Create edges for each pair
        for node_pair in node_list:
            G[node_pair[0]].append(node_pair[1])
            G[node_pair[1]].append(node_pair[0])
    else:
        # Create list of nodes
        node_list = []

        for i in range(1,n+1):
            node_list.append(i)

        # For each combination of nodes, determine if there is an edge
        for pair in itertools.combinations(node_list,2):
            if (choice([True,False], 1, p=[p,1-p])):
                G[pair[0]].append(pair[1])
                G[pair[1]].append(pair[0])

    return G

# given a graph G and nodes i,j, output the length of the shortest
# path between i and j in G.
def shortest_path(G,i,j):

    # Check if source is target
    if (i == j):
      return 0

    # Array for visited nodes, originally containing the source in format (node, back pointer, weight)
    visited = [(i,None)]

    # Store neighbor nodes and distance to it
    discovered = {}

    while (len(visited) != 0):
        temp = visited.pop(0)
        if (temp[0] not in list(discovered.keys())):
            discovered[temp[0]] = (temp[1])
            for node in G[temp[0]]:
                visited.append((node, temp[0]))

    if (j in list(discovered.keys())):
        back_reference = discovered[j]
        distance = 1

        while (back_reference != i):
            cur = back_reference
            back_reference = discovered[cur]
            distance += 1

        return distance

    else:
        return "infinity"

    return None


# main function creates a graph and finds the shortest path
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
    print (sum(distances)/len(distances))

    ##########################################################
    # Question 8d
    ##########################################################
    # G2 = create_graph(1000,0.1)
    #
    # distances = []
    #
    # f = open("avg_shortest_path.txt", "a")
    #
    # for i in range(1000):
    #     n1 = randint(1,1001)
    #     n2 = randint(1,1001)
    #
    #     dist = shortest_path(G2,n1,n2)
    #
    #     distances.append(dist)
    #
    #     f.write("({},{},{})\n".format(n1,n2,dist))
    #
    # f.close()
    # print (sum(distances)/len(distances))

    ##########################################################
    # Question 9a
    ##########################################################
    # fb_G = create_graph(1000,0.1,True)
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
    # print (sum(distances)/len(distances))

main()
