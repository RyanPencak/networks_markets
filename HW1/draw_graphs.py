import networkx as nx
import matplotlib.pyplot as plt

##########################################################
# Problem 5a
##########################################################
G=nx.Graph()
plt.plot()
G.add_nodes_from([1,2,3,4,5])
G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(3,4)
G.add_edge(4,5)
G.add_edge(5,6)
G.add_edge(6,1)
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()

##########################################################
# Problem 5b
##########################################################
G=nx.Graph()
plt.plot()
G.add_nodes_from([1,2,3,4,5,6,7,8,9])
G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(3,4)
G.add_edge(4,5)
G.add_edge(5,6)
G.add_edge(6,7)
G.add_edge(7,8)
G.add_edge(8,9)
G.add_edge(9,1)
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()

##########################################################
# Problem 5c
##########################################################
G=nx.Graph()
plt.plot()
G.add_nodes_from(['x','1','2','3'])
G.add_edge('x','1')
G.add_edge('x','2')
G.add_edge('x','3')
nx.draw(G, with_labels=True, font_weight='bold')
plt.show()

##########################################################
# Problem 6a
##########################################################
G = nx.complete_graph(32)
plt.plot()
G.add_nodes_from([32,33,34])
G.add_edge(31,32)
G.add_edge(32,33)
G.add_edge(33,34)
nx.draw_spring(G, with_labels=True)
plt.show()
