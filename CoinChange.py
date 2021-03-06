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



def coinChange(coin, index, value):
    """
    Recursive approch to solve this problem

    :param coin:
    :param index:
    :param value:
    :return:
    """
    if value == 0 :
        return 1
    elif value >0 and index>=0 and index < len(coin):
        a = coinChange(coin, index, value - coin[index])
        b = coinChange(coin, index - 1, value)
        v = (a + b)
        return v
    else:
        return 0


def coinChangeDP(coin, index, value, memo):
    """
    Dynamic way of solving this problem in similar way as done in previous problem
    :param coin:
    :param index:
    :param value:
    :param memo:
    :return:
    """

    if (index, value) in memo:
        return memo[(index, value)]

    if value == 0:
        return 1

    elif value > 0 and index >= 0 and index < len(coin):
        memo[(index, value)] =  coinChangeDP(coin, index, value - coin[index], memo) + coinChangeDP(coin, index - 1, value, memo)

        return memo[(index, value)]
    else:
        return 0


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
    arr = [1, 2, 3,]
    key = 4
    m = len(arr) -1

    print("Recursive approach: %s"%coinChange(arr, m, key))
    r = coinChangeDP(arr, m, key, {})
    print("DP with similar approach: {}".format(r))
    r = countWithDPAnotherApproch(arr, key)
    print("DP with different approach: {}".format(r))
