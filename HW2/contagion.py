from helper_functions import *
import networkx as nx
from random import randint
# include any code you need for your assignment in this file or in auxiliary
# files that can be imported here.

# 9 (a)
# implement an algorithm that given a graph G, set of adopters S,
# and a threshold q performs BRD where the adopters S never change.
def contagion_brd(G, S, q):
	for adopt in S:
		G.nodes[adopt]["x"] = True
	change = True
	while change:
		change = False
		for node in G.nodes:
			if node not in S:
				num_adj = len(G[node])
				num_x = 0
				for n, val in G.adj[node].items():
					if "x" in G.nodes[n] and G.nodes[n]["x"]:
						num_x += 1
				if num_x/float(num_adj) > q and ("x" not in G.nodes[node] or not G.nodes[node]["x"]):
					change = True
					G.nodes[node]["x"] = True
				elif num_x/float(num_adj) < q and "x" in G.nodes[node] and G.nodes[node]["x"]:
					G.nodes[node]["x"] = False
	return G

def did_cascade(G):
	for node in G.nodes:
		if "x" not in G.nodes[node] or not G.nodes[node]["x"]: return False
	return True

def num_infected(G):
	count = 0
	for node in G.nodes:
		if "x" in G.nodes[node] and G.nodes[node]["x"]: count += 1
	return count

def q_9_a():
	success_fig4_1_1 = create_figure4_1_1()

	infected_node = ["a"]
	thresh = 0.45
	success_fig4_1_1 = contagion_brd(success_fig4_1_1, infected_node, thresh)

	print("With {} infected and threshold {}, the cascade was {}".format(infected_node,
		thresh, did_cascade(success_fig4_1_1)))

	failed_fig4_1_1 = create_figure4_1_1()
	infected_node = ["a"]
	thresh = 0.5
	failed_fig4_1_1 = contagion_brd(failed_fig4_1_1, infected_node, thresh)
	print("With {} infected and threshold {}, the cascade was {}".format(infected_node,
		thresh, did_cascade(failed_fig4_1_1)))

	success_fig4_1_2 = create_figure4_1_2()
	infected_node = ["a", "c", "e", "g"]
	thresh = 0.6
	success_fig4_1_2 = contagion_brd(success_fig4_1_2, infected_node, thresh)
	print("With {} infected and threshold {}, the cascade was {}".format(infected_node,
		thresh, did_cascade(success_fig4_1_2)))

	failed_fig4_1_2 = create_figure4_1_2()
	infected_node = ["a"]
	thresh = 0.35
	failed_fig4_1_2 = contagion_brd(failed_fig4_1_2, infected_node, thresh)
	print("With {} infected and threshold {}, the cascade was {}".format(infected_node,
		thresh, did_cascade(failed_fig4_1_2)))

# Approx 3080 (3082.06)
def q_9_b():
	tot_infected_across_trials = 0
	for i in range(100):
		fb = create_fb_graph()
		early = [randint(0, nx.number_of_nodes(fb)) for j in range(10)]
		tot_infected_across_trials += num_infected(contagion_brd(fb, early, 0.1))
	print(tot_infected_across_trials/float(100))

def q_9_c():
	for q in [0.0, 0.05, 0.1, 0.15, 0.2, 0.25, 0.3, 0.35, 0.4, 0.45, 0.5]:
		for k in range(0, 260, 10):
			tot_infected_across_trials = 0
			for i in range(10):
				fb = create_fb_graph()
				early = [randint(0, nx.number_of_nodes(fb)-1) for j in range(k)]
				tot_infected_across_trials += num_infected(contagion_brd(fb, early, q))
			print("{},{},{}".format(q, k, tot_infected_across_trials/float(10)))


q_9_a()
q_9_b()
# q_9_c()
