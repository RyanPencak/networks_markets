from graph import create_graph, shortest_path
from numpy.random import randint

G = create_graph(1000,0.1)

distances = []

f = open("avg_shortest_path2.txt", "a")

for i in range(1000):
    n1 = randint(1,1001)
    n2 = randint(1,1001)

    dist = shortest_path(G,n1,n2)

    distances.append(dist)

    f.write("({},{},{})\n".format(n1,n2,dist))

f.close()
print ("The average distance is {}.".format(sum(distances)/len(distances)))
