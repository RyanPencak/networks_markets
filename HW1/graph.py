# include any code you need for your assignment in this file or in auxiliary
# files that can be imported here.

# given number of nodes n and probability p, output a random graph
# as specified in homework
def create_graph(n,p):
    G = {}

    for node in n:
        if (node in self.graph):
            G[node1].append((node2,weight))
        else:
            G[node1] = []
            G[node1].append((node2,weight))

    return G

# given a graph G and nodes i,j, output the length of the shortest
# path between i and j in G.
def shortest_path(G,i,j):
    # Check if source is target
    if (i == j):
      return (([j],0))

    # Array for discovered nodes, originally containing the source
    discovered = []
    discovered.append(i)

    # Store neighbor nodes, total distance to it, and path to it: (node, total_distance, [path_to_this_node])
    queue = []

    # Store current working node: (node,total_distance,[path_to_this_node])
    current_node = (i,0,[i])

    while(current_node[0] != j):
      # Initiate queue with neighbors of source
      for neighbor in G[node](current_node[0]):
          path_to_neighbor = current_node[2] + [neighbor[0]]
          queue.append((neighbor[0],current_node[1]+neighbor[1],path_to_neighbor))

      queue.sort(key=lambda x: x[1])
      current_node = queue.pop(0)
      discovered.append(current_node)

    return ((current_node[2],current_node[1]))
