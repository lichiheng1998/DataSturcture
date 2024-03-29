from Graph.DAG import DirectedAcyclicGraph, DFS

# Test DirectedAcyclicGraph and topological sort
g = DirectedAcyclicGraph()
g.add_edge(0, 1);
g.add_edge(0, 2);
g.add_edge(1, 2);
g.add_edge(2, 0);
g.add_edge(2, 3);
g.add_edge(3, 3);
print(g)
trace = DFS(g)
for v in trace:
    print(v)
print(g.isCyclic)
