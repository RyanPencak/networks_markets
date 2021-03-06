# Please enter here the netids of all memebers of your group (yourself included.)
authors = ['rvp32','cjr268','ds2346','ccs254']

# Which version of python are you using? python 2 or python 3?
python_version = "3"

import operator
import networkx as nx

# Important: You are NOT allowed to modify the method signatures (i.e. the arguments and return types each function takes).

# Implement the methods in this class as appropriate. Feel free to add other methods
# and attributes as needed.
# Assume that nodes are represented by indices between 0 and number_of_nodes - 1
class DirectedGraph:

    def __init__(self,number_of_nodes):
        self.G = nx.DiGraph()

        for n in range(number_of_nodes):
            self.G.add_node(n)

    def add_edge(self, origin_node, destination_node):
        self.G.add_edge(origin_node,destination_node)

    def add_edges_from(self, edge_list):
        self.G.add_edges_from(edge_list)

    def edges_from(self, origin_node):
        ''' This method shold return a list of all the nodes u such that the edge (origin_node,u) is
        part of the graph.'''
        return list(self.G.adj[origin_node])

    def in_edges(self, dest_node):
        in_edges = self.G.in_edges(dest_node)
        return [i[0] for i in in_edges]

    def check_edge(self, origin_node, destination_node):
        ''' This method should return true is there is an edge between origin_node and destination_node
        and destination_node, and false otherwise'''
        return self.G.has_edge(origin_node,destination_node)

    def number_of_nodes(self):
        ''' This method should return the number of nodes in the graph'''
        return self.G.number_of_nodes()

def scaled_page_rank(graph, num_iter, eps = 1/7.0):
    ''' This method, given a directed graph, should run the epsilon-scaled page-rank
    algorithm for num-iter iterations and return a mapping (dictionary) between a node and its weight.
    In the case of 0 iterations, all nodes should have weight 1/number_of_nodes'''

    scores = {}
    n = graph.number_of_nodes()

    # Set Score_0 to 1/n
    for v in range(n):
        scores[v] = [None] * (num_iter+1)
        scores[v][0] = (1/n)

    # Set Score_i+1
    for i in range(num_iter):
        for v in range(n):
            summation = 0
            for v_prime in graph.in_edges(v):
                summation += (scores[v_prime][i]/float(len(graph.edges_from(v_prime))))
            scores[v][i+1] = ((eps/n) + ((1 - eps) * summation))

    for node in scores.keys():
        scores[node] = scores[node][-1]

    return scores

def graph_15_1_left():
    ''' This method, should construct and return a DirectedGraph encoding the left example in fig 15.1
    Use the following indexes: A:0, B:1, C:2, Z:3 '''

    graph = DirectedGraph(4)
    graph.add_edge(0,1)
    graph.add_edge(1,2)
    graph.add_edge(2,0)
    graph.add_edge(0,3)
    graph.add_edge(3,3)

    return graph

def graph_15_1_right():
    ''' This method, should construct and return a DirectedGraph encoding the right example in fig 15.1
    Use the following indexes: A:0, B:1, C:2, Z1:3, Z2:4'''

    graph = DirectedGraph(5)
    graph.add_edge(0,1)
    graph.add_edge(1,2)
    graph.add_edge(2,0)
    graph.add_edge(0,3)
    graph.add_edge(0,4)
    graph.add_edge(3,4)
    graph.add_edge(4,3)

    return graph

def graph_15_2():
    ''' This method, should construct and return a DirectedGraph encoding example 15.2
        Use the following indexes: A:0, B:1, C:2, A':3, B':4, C':5'''

    graph = DirectedGraph(6)
    graph.add_edge(0,1)
    graph.add_edge(1,2)
    graph.add_edge(2,0)
    graph.add_edge(3,4)
    graph.add_edge(4,5)
    graph.add_edge(5,3)

    return graph

def extra_graph_1():
    ''' This method, should construct and return a DirectedGraph of your choice with at least 10 nodes'''

    # random directed graph with 12 nodes
    graph = DirectedGraph(12)
    graph.add_edges_from([
        (0,8),
        (1,10),(1,3),
        (2,1),
        (3,2),(3,5),(3,8),
        (4,11),
        (5,10),
        (6,4),(6,11),
        (7,0),(7,3),
        (8,2),(8,9),
        (9,6),
        (10,3),(10,5),(10,7),(10,8),
        (11,0)
    ])

    return graph

# This dictionary should contain the expected weights for each node when running the scaled page rank on the extra_graph_1 output
# with epsilon = 0.07 and num_iter = 20.
extra_graph_1_weights = {0: 0.09249582061831191, 1: 0.10118309239680018, 2: 0.10267174257902882, 3: 0.09226040814604881, 4: 0.04024699952445642, 5: 0.059561037641300656, 6: 0.07454551265362994, 7: 0.030985065671708525, 8: 0.14622617209528213, 9: 0.07409577060943669, 10: 0.10817150751544692, 11: 0.07755687054854794}

def extra_graph_2():
    ''' This method, should construct and return a DirectedGraph of your choice with at least 10 nodes'''

    # random directed graph with 12 nodes
    graph = DirectedGraph(12)
    graph.add_edges_from([
        (0,1),(0,3),
        (1,2),(1,4),
        (2,4),
        (3,0),(3,6),
        (4,3),(4,7),
        (5,2),(5,7),
        (6,7),(6,9),(6,10),
        (7,11),
        (8,4),(8,11),
        (9,0),(9,6),(9,10),
        (10,11),
        (11,5)
    ])

    return graph

# This dictionary should contain the expected weights for each node when running the scaled page rank on the extra_graph_2 output
# with epsilon = 0.07 and num_iter = 20.
extra_graph_2_weights = {0: 0.05148081005487302, 1: 0.029788322158115242, 2: 0.10048316216002834, 3: 0.0836448799487884, 4: 0.11592508139567571, 5: 0.1738357286026897, 6: 0.05148081005487302, 7: 0.1564707819708666, 8: 0.005833333333333334, 9: 0.02180332588318794, 10: 0.028556739451938817, 11: 0.1806970249856291}

def facebook_graph(filename = "facebook_combined.txt"):
    ''' This method should return a DIRECTED version of the facebook graph as an instance of the DirectedGraph class.
    In particular, if u and v are friends, there should be an edge between u and v and an edge between v and u.'''

    fb_G = DirectedGraph(4039)

    # create graph from Facebook data
    with open(filename) as in_file:
        node_list = in_file.readlines()
        node_list = [x.strip().split() for x in node_list]

        for node_pair in node_list:
            node_pair[0] = int(node_pair[0])
            node_pair[1] = int(node_pair[1])

    # Create edges for each pair
    for node_pair in node_list:
        fb_G.add_edge(node_pair[0],node_pair[1])
        fb_G.add_edge(node_pair[1],node_pair[0])

    return fb_G


# The code necessary for your measurements for question 8b should go in this function.
# Please COMMENT THE LAST LINE OUT WHEN YOU SUBMIT (as it will be graded by hand and we do not want it to interfere
# with the automatic grader).
def question8b():
    fb_G = facebook_graph()
    fb_scores = scaled_page_rank(fb_G, 15) # run Pagerank with 15 rounds

    # Get max and min scored nodes
    max_score_node = max(fb_scores.items(), key=operator.itemgetter(1))[0]
    min_score_node = min(fb_scores.items(), key=operator.itemgetter(1))[0]

    # Print sorted dictionary of weights from Pagerank algorithm
    sorted_scores = sorted(fb_scores.items(), key=lambda x: x[1])
    print("Node : Score : Out-degree")
    for pair in sorted_scores:
        print(str(pair[0]) + " : " + str(pair[1]) + " : " + str(len(fb_G.edges_from(pair[0]))))
    print("Node : Score : Out-degree")

    # Print information on node with maximum score
    print("\n\nNode with max score: " + str(max_score_node))
    print("Max score: " + str(fb_scores[max_score_node]))
    print("Out-degree of max score node: " + str(len(fb_G.edges_from(max_score_node))))

    # Print information on node with maximum score
    print("Node with min score: " + str(min_score_node))
    print("Min score of node: " + str(fb_scores[min_score_node]))
    print("Out-degree of min score node: " + str(len(fb_G.edges_from(min_score_node))))

    return (fb_scores)

# question8b()
