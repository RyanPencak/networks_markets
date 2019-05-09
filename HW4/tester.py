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
print("======================")
print("GRAPH 15.1 Left TESTING")
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
print("Sum of correct scores: " + str(sum(correct_scores.values())))


# Graph 15.1 Right Testing
print("======================")
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


# Graph 15.2 Testing
print("======================")
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
