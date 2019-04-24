import hw4

# DO NOT SUBMIT THIS FILE
# It is just an example of a few tests that we will run on your code that you can use as a starting point
# to make sure the code is correct.
# You should put the two python files in the same folder and run this one

testGraph = hw4.DirectedGraph(5)

assert testGraph.number_of_nodes() == 5

assert testGraph.check_edge(0,1) == False

testGraph.add_edge(0,1)

assert testGraph.check_edge(0,1) == True

weights = hw4.scaled_page_rank(testGraph,0)

assert weights[2] == 1/5.0

assert hw4.graph_15_1_left().number_of_nodes() == 4
