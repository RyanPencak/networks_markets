from graph import create_graph, shortest_path
from numpy.random import randint
import numpy as np
import matplotlib.pyplot as plt

f = open("varying_p.txt", "a")
f.write("p, avg_shortest_path\n")

x = []
y = []

for p in np.arange(0.01,0.05,0.01):
    x.append(p)
    G = create_graph(1000,p)

    distances = []

    for i in range(1000):
        n1 = randint(1,1001)
        n2 = randint(1,1001)

        dist = shortest_path(G,n1,n2)

        distances.append(dist)

    avg_distance = sum(distances)/len(distances)
    y.append(avg_distance)
    f.write("{}, {}\n".format(p,avg_distance))

for p in np.arange(0.05,0.55,0.05):
    p = float('%.3f'%(p))   # correct floating point rounding errors from np.arange

    x.append(p)
    G = create_graph(1000,p)

    distances = []

    for i in range(1000):
        n1 = randint(1,1001)
        n2 = randint(1,1001)

        dist = shortest_path(G,n1,n2)

        distances.append(dist)

    avg_distance = sum(distances)/len(distances)
    y.append(avg_distance)
    f.write("{}, {}\n".format(p,avg_distance))

f.close()

# Plot the average shortest path as a function of p
plt.plot(x,y,'o')
plt.ylabel('Average Shortest Path')
plt.xlabel('p')
plt.show()
