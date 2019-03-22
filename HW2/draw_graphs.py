import networkx as nx
import matplotlib.pyplot as plt

##########################################################
# Problem 6a
##########################################################
G=nx.Graph()
G.add_nodes_from([1,2,3,4])
G.add_edge(1,2)
G.add_edge(2,3)
G.add_edge(3,4)
pos = nx.spring_layout(G)
plt.figure()
nx.draw(G, pos, with_labels=True, font_weight='bold')
plt.show()

##########################################################
# Problem 7a
##########################################################
G=nx.DiGraph()
G.add_nodes_from(['A','B','C','D'])
G.add_edge('A','C')
G.add_edge('C','B')
G.add_edge('A','D')
G.add_edge('D','B')
pos = nx.spring_layout(G)
plt.figure()
nx.draw(G, pos, with_labels=True)
nx.draw_networkx_edge_labels(G,pos,edge_labels={('A','C'):'15 + x',('C','B'):'90',('A','D'):'90',('D','B'):'15+y'})
plt.axis('off')
plt.show()
