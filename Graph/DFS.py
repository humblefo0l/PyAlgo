"""
Depth First Search or DFS for a Graph
Depth First Traversal (or Search) for a graph is similar to Depth First Traversal of a tree.
The only catch here is, unlike trees, graphs may contain cycles, a node may be visited twice.
To avoid processing a node more than once, use a boolean visited array.

Example:

Input: n = 4, e = 6
0 -> 1, 0 -> 2, 1 -> 2, 2 -> 0, 2 -> 3, 3 -> 3
Output: DFS from vertex 1 : 1 2 0 3
Explanation:
DFS Diagram:


Input: n = 4, e = 6
2 -> 0, 0 -> 2, 1 -> 2, 0 -> 1, 3 -> 3, 1 -> 3
Output: DFS from vertex 2 : 2 0 1 3
Explanation:
DFS Diagram:

Following are implementations of simple Depth First Traversal. The C++ implementation uses adjacency
list representation of graphs. STL‘s list container is used to store lists of adjacent nodes.

Solution:

Approach: Depth-first search is an algorithm for traversing or searching tree or graph data structures.
The algorithm starts at the root node (selecting some arbitrary node as the root node in the case of a graph)
and explores as far as possible along each branch before backtracking. So the basic idea is to start from
the root or any arbitrary node and mark the node and move to the adjacent unmarked node and continue this
loop until there is no unmarked adjacent node. Then backtrack and check for other unmarked nodes and
traverse them. Finally print the nodes in the path.

Algorithm:
Create a recursive function that takes the index of node and a visited array.
Mark the current node as visited and print the node.
Traverse all the adjacent and unmarked nodes and call the recursive function with index of adjacent node.
"""

from collections import  defaultdict
class Graph:
    def __init__(self):
        self.graph = defaultdict(list)

    def addEdge(self, u, v):
        self.graph[u].append(v)

    def DFSUtils(self, v, visited):

        visited[v] = 1
        print(v, end=" ")

        for i in self.graph[v]:
            if i not in visited:
                self.DFSUtils(i, visited)


    def DFS(self, v):
        # visited = [False] * (max(self.graph) + 1)
        visited = dict()
        return self.DFSUtils(v, visited)

if __name__ == '__main__':
    g = Graph()
    g.addEdge(0, 1)
    g.addEdge(0, 2)
    g.addEdge(1, 2)
    g.addEdge(2, 0)
    g.addEdge(2, 3)
    g.addEdge(3, 3)

    print("Following is DFS from (starting from vertex 2)")
    g.DFS(2)