from Graph.DAG import DirectedAcyclicGraph, DFS

test_graph = DirectedAcyclicGraph([(1, 6), (1, 2), (2, 5), (2, 3), (5, 4), (1, 5)])
print(test_graph)
trace = DFS(test_graph)
for v in trace:
    print(v)
