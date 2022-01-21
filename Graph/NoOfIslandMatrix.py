"""
Find the number of islands | Set 1 (Using DFS)
Given a boolean 2D matrix, find the number of islands. A group of connected 1s forms an island.
For example, the below matrix contains 5 islands

Example:

Input : mat[][] = {{1, 1, 0, 0, 0},
                   {0, 1, 0, 0, 1},
                   {1, 0, 0, 1, 1},
                   {0, 0, 0, 0, 0},
                   {1, 0, 1, 0, 1}
Output : 5
This is a variation of the standard problem: “Counting the number of connected components
in an undirected graph”.

Before we go to the problem, let us understand what is a connected component. A connected
component of an undirected graph is a subgraph in which every two vertices are connected to each
other by a path(s), and which is connected to no other vertices outside the subgraph.
For example, the graph shown below has three connected components.

A graph where all vertices are connected with each other has exactly one connected component,
consisting of the whole graph. Such a graph with only one connected component is called a Strongly Connected Graph.

The problem can be easily solved by applying DFS() on each component. In each DFS() call, a component or
a sub-graph is visited. We will call DFS on the next un-visited component. The number of calls to DFS()
gives the number of connected components. BFS can also be used.

What is an island?
A group of connected 1s forms an island. For example, the below matrix contains 4 islands

A cell in 2D matrix can be connected to 8 neighbours. So, unlike standard DFS(), where we recursively
call for all adjacent vertices, here we can recursively call for 8 neighbours only. We keep track of
the visited 1s so that they are not visited again.
"""
class Graph:
    def __init__(self, r, c, g):
        self.row = r
        self.col = c
        self.graph = g

    def countIslands(self):
        count = 0
        visited = [[False for i in range(self.col)] for i in range(self.row)]

        for row in range(self.row):
            for col in range(self.col):
                if not visited[row][col] and self.graph[row][col]:
                    count += 1
                    self.DFS(row, col, visited)
        return count

    def isSafe(self, row, col, visited):

        return (row >= 0 and row < self.row and
                col >= 0 and col < self.col and
                not visited[row][col]
                and self.graph[row][col])



    def DFS(self, row, col, visited):
        r = [-1, -1, -1, 0, 0, 1, 0, 1]
        c = [-1, 0, 1, -1, 1, -1, 0, 1]

        visited[row][col] = True

        for i in range(8):
            if self.isSafe(row+r[i], col+c[i], visited):
                self.DFS(row + r[i], col + c[i], visited)


graph = [[1, 1, 0, 0, 0],
         [0, 1, 0, 0, 1],
         [1, 0, 0, 1, 1],
         [0, 0, 0, 0, 0],
         [1, 0, 1, 0, 1]]

# graph = [
#     [1,1,0,0],
#     [0,0,1,0],
#     [0,0,0,0],
#     [1,0,1,1],
#     [1,1,1,1]
# ]
row = len(graph)
col = len(graph[0])

g = Graph(row, col, graph)

print("Number of islands is:")
print(g.countIslands())
