from Graph.vertex import Vertex
from Graph import _WHITE, _GREY, _BLACK
from typing import List, Set
import copy

class DirectedAcyclicGraph:
    def __init__(self, *edges) -> None:
        # eliminate duplicates vertices
        self._vertices = {}
        self._edges = set()
        self._graph = {}

        # add each edge to the graph
        for E in edges:
            self.add_edge(*E)

        # variables exist for algorithm
        self._clock = 0
        self.isCyclic = None

    def add_edge(self, u, v):
        # add edges
        self._edges.add((u, v))
        # initialize vertex
        for e in [u, v]:
            if e not in self._vertices:
                self._vertices[e] = Vertex(e)
        # add to graph
        if u not in self._graph:
            self._graph[u] = []
        self._graph[u].append(v)

    def __str__(self):
        graph = ""
        for u in self._graph:
            vertex_u = self._vertices[u]
            graph += str(vertex_u.label) + " -> ["
            for i in range(len(self._graph[u])):
                v = self._graph[u][i]
                vertex_v = self._vertices[v]
                graph += str(vertex_v.label)
                if i < len(self._graph[u]) - 1:
                    graph += ", "
            graph += "]\n"
        return graph

def DFS_Explore(
        ordered_vertices: List[Vertex],
        graph: DirectedAcyclicGraph,
        prev, u
    ) -> None:
    vertex_u = graph._vertices[u]
    # If the vertex explored is in the process of being explored, then there is
    # a cycle in the graph.
    if vertex_u.color == _GREY:
        graph.isCyclic = True
        return
    elif vertex_u.color == _BLACK:
        return
    # set the parent vertex
    vertex_u.parent = None if prev is None else graph._vertices[prev]
    # color the edge to grey
    vertex_u.color = _GREY
    # increment the time
    graph._clock = graph._clock + 1
    vertex_u.d = graph._clock
    if u in graph._graph:
        for v in graph._graph[u]:
            DFS_Explore(ordered_vertices, graph, u, v)
    # finish exploring the vertex
    vertex_u.color = _BLACK
    graph._clock = graph._clock + 1
    vertex_u.f = graph._clock
    # Inserted to the list of visited vertices ordered by finishing time
    ordered_vertices.insert(0, vertex_u)

def DFS(graph: DirectedAcyclicGraph) -> List[Vertex]:
    ordered_vertices = []
    exploring_vertices = {}
    vertices = graph._vertices.values()
    # color all vertices to white
    for u in vertices:
        u.color = _WHITE
        u.d = -1
        u.f = -1
        u.parent = None
    # initialize the clock
    graph._clock = 0
    graph.isCyclic = False
    # start exploring
    for u in graph._vertices:
        if graph._vertices[u].color == _WHITE:
            DFS_Explore(ordered_vertices, graph, None, u)
    return ordered_vertices
