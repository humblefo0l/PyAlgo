"""
Cutting a Rod | DP-13
Given a rod of length n inches and an array of prices that contains prices of all pieces of size smaller
than n. Determine the maximum value obtainable by cutting up the rod and selling the pieces. For example,
if length of the rod is 8 and the values of different pieces are given as following, then the
maximum obtainable value is 22 (by cutting in two pieces of lengths 2 and 6)


length   | 1   2   3   4   5   6   7   8
--------------------------------------------
price    | 1   5   8   9  10  17  17  20

And if the prices are as following, then the maximum obtainable value is 24 (by cutting in eight pieces
of length 1)

length   | 1   2   3   4   5   6   7   8
--------------------------------------------
price    | 3   5   8   9  10  17  17  20

A naive solution for this problem is to generate all configurations of different pieces and find the highest priced configuration. This solution is exponential in term of time complexity. Let us see how this problem possesses both important properties of a Dynamic Programming (DP) Problem and can efficiently solved using Dynamic Programming.

1) Optimal Substructure:
We can get the best price by making a cut at different positions and comparing the values obtained after a cut. We can recursively call the same function for a piece obtained after a cut.

Let cutRod(n) be the required (best possible price) value for a rod of length n. cutRod(n) can be written as following.

cutRod(n) = max(price[i] + cutRod(n-i-1)) for all i in {0, 1 .. n-1}
"""
import sys

def cutRod(price, length):
    if length <=0:
        return 0
    max_value = -(sys.maxsize-1)

    for i in range(1, length):
        max_value = max(max_value, price[i] + cutRod(price, length-i-1))

    return max_value



def cutRodDP(array, size):
    dp = [0] * (size+1)
    for i in range(1, size+1):
        temp = -(sys.maxsize)
        for j in range(i):
            temp = max(temp, array[j] + dp[i-j-1])
        dp[i] = temp

    return dp[size]


# def cutRodS(arr, start, end):
#     if start == end:
#         return 1
#
#     if end < 0 and start >= len(arr):
#         return 0
#
#     return max(cutRodS(arr, start, end-1) + arr[end], cutRodS(arr, start, end-1))

def cr(a, s):
    if s <= 0:
        return 0

    m = -1

    for i in range(s):
        m = max(m, a[i] + cr(a, s - i - 1))

    return m



print(cr([1, 2, 3, 1], 4))

if __name__ == '__main__':

    arr = [1, 3,1, 4, 8,2, 5,7]
    size = len(arr)
    start = 0
    print("Maximum Obtainable Value is", cutRod(arr, size))
    print("Maximum Obtainable Value via DP is", cutRodDP(arr, size))
    # print("Maximum Obtainable Value via DP_S is", cutRodS(arr, start, size-1))
    print("Maximum Obtainable Value via DP_S is", cutRodS(arr, start))
