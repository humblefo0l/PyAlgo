"""
Find minimum number of coins that make a given value
Given a value V, if we want to make change for V cents, and we have infinite supply of
each of C = { C1, C2, .. , Cm} valued coins, what is the minimum number of coins to make the change?
Examples:

Input: coins[] = {25, 10, 5}, V = 30
Output: Minimum 2 coins required
We can use one coin of 25 cents and one of 5 cents

Input: coins[] = {9, 6, 5, 1}, V = 11
Output: Minimum 2 coins required
We can use one coin of 6 cents and 1 coin of 5 cents

This problem is a variation of the problem discussed Coin Change Problem. Here instead of finding
total number of possible solutions, we need to find the solution with minimum number of coins.

The minimum number of coins for a value V can be computed using below recursive formula.

If V == 0, then 0 coins required.
If V > 0
   minCoin(coins[0..m-1], V) = min {1 + minCoins(V-coin[i])}
                               where i varies from 0 to m-1
                               and coin[i] <= V

"""


def count(values, index, key):
    """
    Dynamic approach to solve this problem in different way
    :param values:
    :param n:
    :return:
    """
    import sys

    if key == 0:
        return 0

    res = sys.maxsize

    for i in range(index):
        if values[i] <= key:
            sub_res = count(values, index, key - values[i])

            if sub_res != sys.maxsize and sub_res+1 < res:
                res = sub_res+1

    return res


if __name__ == '__main__':
    values = [1, 2, 3,7,9,10]
    key = 15
    index = len(values)

    print("Min number is %s"%count(values, index, key))
    dp={}
    print("Min number is %s"%countdp(values ,index, key, dp))
