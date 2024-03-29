"""
Breadth First Search or BFS for a Graph

Breadth First Traversal (or Search) for a graph is similar to Breadth First Traversal of a tree
(See method 2 of this post). The only catch here is, unlike trees, graphs may contain cycles, so we may come to
the same node again. To avoid processing a node more than once, we use a boolean visited array. For simplicity,
it is assumed that all vertices are reachable from the starting vertex.

For example, in the following graph, we start traversal from vertex 2. When we come to vertex 0, we look for all
adjacent vertices of it. 2 is also an adjacent vertex of 0. If we don’t mark visited vertices, then 2 will be
processed again and it will become a non-terminating process. A Breadth First Traversal of the following graph
is 2, 0, 3, 1.
"""

from collections import defaultdict

class Graph:
    def __init__(self):
        self.graph = defaultdict([])

    def addEdge(self, u, v):
        self.graph[u].append(v)



a = defaultdict(list)


# if __name__ == '__main__':
#     g = Graph()
#     g.addEdge(0, 1)
#     g.addEdge(0, 2)
#     g.addEdge(1, 2)
#     g.addEdge(2, 0)
#     g.addEdge(2, 3)
#     g.addEdge(3, 3)
#
#     print("Following is Breadth First Traversal"
#           " (starting from vertex 2)")
#     g.BFS(2)