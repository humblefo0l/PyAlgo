"""
Coin Change | DP-7
Given a value N, if we want to make change for N cents, and we have infinite supply of
each of S = { S1, S2, .. , Sm} valued coins, how many ways can we make the change? The
order of coins doesn’t matter.
For example, for N = 4 and S = {1,2,3}, there are four solutions: {1,1,1,1},{1,1,2},
{2,2},{1,3}. So output should be 4. For N = 10 and S = {2, 5, 3, 6}, there are five
solutions: {2,2,2,2,2}, {2,2,3,3}, {2,2,6}, {2,3,5} and {5,5}. So the output should be 5.

1) Optimal Substructure
To count the total number of solutions, we can divide all set solutions into two sets.
1) Solutions that do not contain mth coin (or Sm).
2) Solutions that contain at least one Sm.
Let count(S[], m, n) be the function to count the number of solutions, then it can be
written as sum of count(S[], m-1, n) and count(S[], m, n-Sm).

Therefore, the problem has optimal substructure property as the problem can be solved
using solutions to subproblems.

2) Overlapping Subproblems
Following is a simple recursive implementation of the Coin Change problem. The
implementation simply follows the recursive structure mentioned above.
"""



def count(arr, m, n):
    """
    Recursive approch to solve this problem
    :param arr:
    :param m:
    :param n:
    :return:
    """

    if m <= 0:
        return 0

    if n == 0:
        return 1

    if n<0:
        return 0

    return count(arr, m, n-arr[m-1]) + count(arr, m-1, n)


dp = [[-1 for i in range(150)] for j in range(150)]
def countWithDP(coins, m, N):
    """
    Dynamic way of solving this problem in similar way as done in previous problem
    :param coins:
    :param m:
    :param N:
    :return:
    """

    if m <= 0:
        return 0

    if N == 0:
        return 1

    if N < 0:
        return 0

    if N==0 and m>0:
        return 1

    if dp[m][N] != -1:
        return dp[m][N]

    dp[m][N] = countWithDP(coins, m-1, N) + \
               countWithDP(coins, m, N-coins[m-1])

    return dp[m][N]



def countWithDPAnotherApproch(coins, n):
    """
    Dynamic approach to solve this problem in different way
    :param coins: list of coins
    :param n: key for which combination needs to be calculated
    :return:
    """
    dp_size = n+1
    dp = [0]*dp_size
    dp[0]=1

    for c in range(len(coins)):
        for i in range(len(dp)):
            if coins[c] <= i:
                dp[i] = dp[i - coins[c]] + dp[i]

    return dp[-1]


if __name__ == '__main__':
    arr = [1, 2, 3,7,9,10]
    key = 50
    m = len(arr)

    print("Recursive approach: %s"%count(arr, m, key))
    r = countWithDP(arr, m, key)
    print("DP with similar approach: {}".format(r))
    r = countWithDPAnotherApproch(arr, key)
    print("DP with different approach: {}".format(r))
