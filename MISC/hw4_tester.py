import hw4
import networkx as nx

# DO NOT SUBMIT THIS FILE
# It is just an example of a few tests that we will run on your code that you can use as a starting point
# to make sure the code is correct.
# You should put the two python files in the same folder and run this one

# Basic Testing
print("======================")
print("BASIC TESTING")
print("======================")
testGraph = hw4.DirectedGraph(5)
assert testGraph.number_of_nodes() == 5
assert testGraph.check_edge(0,1) == False
testGraph.add_edge(0,1)
assert testGraph.check_edge(0,1) == True
scores = hw4.scaled_page_rank(testGraph,0)
assert scores[2] == 1/5.0
print("done.")

# Graph 15.1 Left Testing
print("\n\n======================")
print("GRAPH 15.1 LEFT TESTING")
print("======================")
example_15_1_left = hw4.graph_15_1_left()
assert example_15_1_left.number_of_nodes() == 4
assert example_15_1_left.edges_from(0) == [1,3]
assert example_15_1_left.edges_from(1) == [2]
assert example_15_1_left.edges_from(2) == [0]
assert example_15_1_left.edges_from(3) == [3]
assert example_15_1_left.check_edge(0,1)
assert example_15_1_left.check_edge(1,2)
assert example_15_1_left.check_edge(2,0)
assert example_15_1_left.check_edge(0,3)
assert example_15_1_left.check_edge(3,3)

scores_0 = hw4.scaled_page_rank(example_15_1_left,0)
print("Example 15.1 Left - Scores - 0 Rounds: " + str(scores_0))
print("Sum of scores: " + str(sum(scores_0.values())))

scores_10 = hw4.scaled_page_rank(example_15_1_left,10)
print("Example 15.1 Left - Scores - 10 Rounds: " + str(scores_10))
print("Sum of scores: " + str(sum(scores_10.values())))

scores_20 = hw4.scaled_page_rank(example_15_1_left,20)
print("Example 15.1 Left - Scores - 20 Rounds: " + str(scores_20))
print("Sum of scores: " + str(sum(scores_20.values())))

nx_example_15_1_left = nx.DiGraph()
nx_example_15_1_left.add_edge(0,1)
nx_example_15_1_left.add_edge(1,2)
nx_example_15_1_left.add_edge(2,0)
nx_example_15_1_left.add_edge(0,3)
nx_example_15_1_left.add_edge(3,3)
correct_scores = nx.pagerank(nx_example_15_1_left)
print("Correct scores: " + str(correct_scores))


# Graph 15.1 Right Testing
print("\n\n======================")
print("GRAPH 15.1 RIGHT TESTING")
print("======================")
example_15_1_right = hw4.graph_15_1_right()
assert example_15_1_right.number_of_nodes() == 5
assert example_15_1_right.edges_from(0) == [1,3,4]
assert example_15_1_right.check_edge(0,1)
assert example_15_1_right.check_edge(1,2)
assert example_15_1_right.check_edge(2,0)
assert example_15_1_right.check_edge(0,3)
assert example_15_1_right.check_edge(0,4)
assert example_15_1_right.check_edge(3,4)
assert example_15_1_right.check_edge(4,3)

scores_0 = hw4.scaled_page_rank(example_15_1_right,0)
print("Example 15.1 Right - Scores - 0 Rounds: " + str(scores_0))
print("Sum of scores: " + str(sum(scores_0.values())))

scores_10 = hw4.scaled_page_rank(example_15_1_right,10)
print("Example 15.1 Right - Scores - 10 Rounds: " + str(scores_10))
print("Sum of scores: " + str(sum(scores_10.values())))

scores_20 = hw4.scaled_page_rank(example_15_1_right,20)
print("Example 15.1 Right - Scores - 20 Rounds: " + str(scores_20))
print("Sum of scores: " + str(sum(scores_20.values())))

nx_example_15_1_right = nx.DiGraph()
nx_example_15_1_right.add_edge(0,1)
nx_example_15_1_right.add_edge(1,2)
nx_example_15_1_right.add_edge(2,0)
nx_example_15_1_right.add_edge(0,3)
nx_example_15_1_right.add_edge(0,4)
nx_example_15_1_right.add_edge(3,4)
nx_example_15_1_right.add_edge(4,3)
correct_scores = nx.pagerank(nx_example_15_1_right)
print("Correct scores: " + str(correct_scores))


# Graph 15.2 Testing
print("\n\n======================")
print("GRAPH 15.2 TESTING")
print("======================")
example_15_2 = hw4.graph_15_2()
assert example_15_2.number_of_nodes() == 6
assert example_15_2.edges_from(0) == [1]
assert example_15_2.check_edge(0,1)
assert example_15_2.check_edge(1,2)
assert example_15_2.check_edge(2,0)
assert example_15_2.check_edge(3,4)
assert example_15_2.check_edge(4,5)
assert example_15_2.check_edge(5,3)

scores_0 = hw4.scaled_page_rank(example_15_2,0)
print("Example 15.2 - Scores - 0 Rounds: " + str(scores_0))
print("Sum of scores: " + str(sum(scores_0.values())))

scores_10 = hw4.scaled_page_rank(example_15_2,10)
print("Example 15.2 - Scores - 10 Rounds: " + str(scores_10))
print("Sum of scores: " + str(sum(scores_10.values())))

scores_20 = hw4.scaled_page_rank(example_15_2,20)
print("Example 15.2 - Scores - 20 Rounds: " + str(scores_20))
print("Sum of scores: " + str(sum(scores_20.values())))

nx_example_15_2 = nx.DiGraph()
nx_example_15_2.add_edge(0,1)
nx_example_15_2.add_edge(1,2)
nx_example_15_2.add_edge(2,0)
nx_example_15_2.add_edge(3,4)
nx_example_15_2.add_edge(4,5)
nx_example_15_2.add_edge(5,3)
correct_scores = nx.pagerank(nx_example_15_2)
print("Correct scores: " + str(correct_scores))


# Example 1 Testing
print("\n\n======================")
print("EXAMPLE 1 TESTING")
print("======================")
example1 = hw4.extra_graph_1()
assert example1.number_of_nodes() == 12
assert example1.edges_from(0) == [8]
assert example1.check_edge(1,10)
assert example1.check_edge(10,5)

example1_scores = hw4.scaled_page_rank(example1,20,0.07)
print("\nExample 1 Scores: " + str(example1_scores))
print("\nSum of scores: " + str(sum(example1_scores.values())))
assert(example1_scores == {0: 0.09249582061831191, 1: 0.10118309239680018, 2: 0.10267174257902882, 3: 0.09226040814604881, 4: 0.04024699952445642, 5: 0.059561037641300656, 6: 0.07454551265362994, 7: 0.030985065671708525, 8: 0.14622617209528213, 9: 0.07409577060943669, 10: 0.10817150751544692, 11: 0.07755687054854794})

nx_example1 = nx.DiGraph()
nx_example1.add_edges_from([
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
correct_scores = nx.pagerank(nx_example1)
# print("Correct scores: " + str(correct_scores))
# print("Sum of Correct scores: " + str(sum(correct_scores.values())))


# Example 2 Testing
print("\n\n======================")
print("EXAMPLE 2 TESTING")
print("======================")
example2 = hw4.extra_graph_2()
assert example2.number_of_nodes() == 12
assert example2.edges_from(0) == [1,3]
assert example2.check_edge(10,11)
assert example2.check_edge(3,6)

example2_scores = hw4.scaled_page_rank(example2,20,0.07)
print("\nExample 15.2 Scores: " + str(example2_scores))
print("\nSum of scores: " + str(sum(example2_scores.values())))
assert(example2_scores == {0: 0.05148081005487302, 1: 0.029788322158115242, 2: 0.10048316216002834, 3: 0.0836448799487884, 4: 0.11592508139567571, 5: 0.1738357286026897, 6: 0.05148081005487302, 7: 0.1564707819708666, 8: 0.005833333333333334, 9: 0.02180332588318794, 10: 0.028556739451938817, 11: 0.1806970249856291})

nx_example2 = nx.DiGraph()
nx_example2.add_edges_from([
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
correct_scores = nx.pagerank(nx_example2)
# print("Correct scores: " + str(correct_scores))
# print("Sum of Correct scores: " + str(sum(correct_scores.values())))
