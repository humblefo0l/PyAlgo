"""
Min Cost Path | DP-6
Given a cost matrix cost[][] and a position (m, n) in cost[][], write a function that returns cost of
minimum cost path to reach (m, n) from (0, 0). Each cell of the matrix represents a cost to traverse
through that cell. Total cost of a path to reach (m, n) is sum of all the costs on that path (including
both source and destination). You can only traverse down, right and diagonally lower cells from a given
cell, i.e., from a given cell (i, j), cells (i+1, j), (i, j+1) and (i+1, j+1) can be traversed. You may
assume that all costs are positive integers.

For example, in the following figure, what is the minimum cost path to (2, 2)?


                    1       2       3

                    4       8       2

                    1       5       3

The path with minimum cost is highlighted in the following figure. The path is (0, 0) –> (0, 1) –>
(1, 2) –> (2, 2). The cost of the path is 8 (1 + 2 + 2 + 3).

"""

import sys

def minCost(cost, i, j):

    if i < 0 or j < 0:
        return sys.maxsize

    if i == 0 and j == 0:
        return cost[i][j]

    return cost[i][j] + min(minCost(cost, i-1, j),
                           minCost(cost, i, j-1),
                           minCost(cost, i-1, j-1)
                           )



def MinCostDP(cost, r, c, memo):

    if r < 0 or c < 0:
        return sys.maxsize

    if r == 0 and c == 0:
        return cost[r][c]

    if (r,c) in memo:
        return memo[(r,c)]

    else:
        memo[(r, c)] =  cost[r][c] + min(MinCostDP(cost, r, c - 1, memo),
                                         MinCostDP(cost, r - 1, c - 1, memo),
                                         MinCostDP(cost, r - 1, c, memo)
                                         )
        return memo[(r,c)]




if __name__ == '__main__':
    cost = [[1, 2, 3],
            [4, 8, 2],
            [1, 5, 3]]
    import time

    start_time = time.time()
    print(minCost(cost, 2, 2))

    memo = {}
    print(MinCostDP(cost, 2, 2, memo))

    cost = [[1, 21, 113, 11],
            [54, 10, 12, 15],
            [10, 5, 31, 2]]
    import time

    start_time = time.time()
    print(minCost(cost, 2, 2))

    memo = {}
    print(MinCostDP(cost, 2, 2, memo))

