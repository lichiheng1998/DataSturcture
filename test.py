from Graph.DAG import DirectedAcyclicGraph, DFS

# Test DirectedAcyclicGraph and topological sort
g = DirectedAcyclicGraph()
g.add_edge(5, 2);
g.add_edge(5, 0);
g.add_edge(4, 0);
g.add_edge(4, 1);
g.add_edge(2, 3);
g.add_edge(3, 1);
print(g)
trace = DFS(g)
for v in trace:
    print(v)
