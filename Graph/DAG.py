from Graph.vertex import Vertex
from Graph import _WHITE, _GREY, _BLACK
import copy

class DirectedAcyclicGraph:
    def __init__(self, edges) -> None:
        # eliminate duplicates vertices
        self._vertices = {}
        for E in edges:
            self._vertices[E[0]] = Vertex(E[0])
            self._vertices[E[1]] = Vertex(E[1])

        # eliminate duplicates edges
        self._edges = set(edges)

        # variables exist for algorithm
        self._clock = 0

        # initialize graph
        self._graph = {}
        for E in self._edges:
            vertex_a, vertex_b = self._vertices[E[0]], self._vertices[E[1]]
            if vertex_a not in self._graph:
                self._graph[vertex_a] = []
            self._graph[vertex_a].append(vertex_b)

    def __str__(self):
        graph = ""
        for v in self._graph:
            graph += str(v.label) + " -> ["
            for i in range(len(self._graph[v])):
                graph += str(self._graph[v][i].label)
                if i < len(self._graph[v]) - 1:
                    graph += ", "
            graph += "]\n"
        return graph

def DFS_Explore(graph: DirectedAcyclicGraph, u: Vertex) -> None:
    # color the edge to grey
    u.color = _GREY
    # increment the time
    graph._clock = graph._clock + 1
    u.d = graph._clock
    if u in graph._graph:
        for v in graph._graph[u]:
            if v.color == _WHITE:
                v.parent = u
                DFS_Explore(graph, v)
    # finish exploring the vertex
    u.color = _BLACK
    graph._clock = graph._clock + 1
    u.f = graph._clock

def DFS(graph: DirectedAcyclicGraph):
    vertices = graph._vertices.values()
    # color all vertices to white
    for v in vertices:
        v.color = _WHITE
        v.d = -1
        v.f = -1
        v.parent = None
    # initialize the clock
    graph._clock = 0
    # start exploring
    for v in vertices:
        if v.color == _WHITE:
            DFS_Explore(graph, v)
    return graph._vertices.values()
