"""
0-1 Knapsack Problem | DP-10
Given weights and values of n items, put these items in a knapsack of capacity W to get the maximum
total value in the knapsack. In other words, given two integer arrays val[0..n-1] and wt[0..n-1]
which represent values and weights associated with n items respectively. Also given an integer W
which represents knapsack capacity, find out the maximum value subset of val[] such that sum of the
weights of this subset is smaller than or equal to W. You cannot break an item, either pick the complete
item, or don’t pick it (0-1 property).
"""

def knapSack(W, wt, val, n):

    if W == 0 or n == 0:
        return 0

    if wt[n-1] > W:
        return knapSack(W, wt, val, n-1)

    else:
        return max(val[n-1] + knapSack(W-wt[n-1], wt, val, n-1),
                   knapSack(W, wt, val, n-1))


def knapSackDP(W, wt, val, n, memo):
    if (W, n) in memo:
        return memo[(W, n)]

    if W == 0 or n == 0:
        return 0

    if wt[n-1] > W:
        memo[W, n] = knapSackDP(W, wt, val, n-1, memo)
        return memo[W,n]
    else:
        memo[(W, n)] = max(val[n-1] + knapSackDP(W-wt[n-1], wt, val, n-1, memo),
                           knapSackDP(W, wt, val, n-1, memo))
        return memo[(W,n)]


def knapSackAnother(W, wt, val, n):
    K = [[0 for x in range(W + 1)] for x in range(n + 1)]

    # Build table K[][] in bottom up manner
    for i in range(n + 1):
        for w in range(W + 1):
            if i == 0 or w == 0:
                K[i][w] = 0
            elif wt[i - 1] <= w:
                K[i][w] = max(val[i - 1] + K[i - 1][w - wt[i - 1]], K[i - 1][w])
            else:
                K[i][w] = K[i - 1][w]

    return K[n][W]


if __name__ == '__main__':
    import timeit, time

    val = [60, 100, 120, 200,1, 12, 234, 241,  12]
    wt =  [10, 20,  30,  42, 23,231,134, 234,  33]
    W = 5000
    n = len(val)
    start_time = time.time()
    print(knapSack(W , wt , val , n), end=", ")
    print("time elapsed: {:.2f}s".format(time.time() - start_time))
    memo = {}
    start_time = time.time()
    print(knapSackDP(W , wt , val , n, memo), end=", ")
    print("time elapsed: {:.2f}s".format(time.time() - start_time))

    start_time = time.time()
    print(knapSackAnother(W , wt , val , n), end=", ")
    print("time elapsed: {:.2f}s".format(time.time() - start_time))
