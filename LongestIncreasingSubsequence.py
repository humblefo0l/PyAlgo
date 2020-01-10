"""
Longest Increasing Subsequence | DP-3
We have discussed Overlapping Subproblems and Optimal Substructure properties.

Let us discuss Longest Increasing Subsequence (LIS) problem as an example problem that can be solved using
Dynamic Programming.
The Longest Increasing Subsequence (LIS) problem is to find the length of the longest subsequence of a given
sequence such that all elements of the subsequence are sorted in increasing order. For example, the length
of LIS for {10, 22, 9, 33, 21, 50, 41, 60, 80} is 6 and LIS is {10, 22, 33, 50, 60, 80}.
longest-increasing-subsequence

More Examples:

Input  : arr[] = {3, 10, 2, 1, 20}
Output : Length of LIS = 3
The longest increasing subsequence is 3, 10, 20

Input  : arr[] = {3, 2}
Output : Length of LIS = 1
The longest increasing subsequences are {3} and {2}

Input : arr[] = {50, 3, 10, 7, 40, 80}
Output : Length of LIS = 4
The longest increasing subsequence is {3, 7, 40, 80}
"""

import sys

def longestIncSeq(array, size):
    mv = -(sys.maxsize)

    for i in range(size):
        count = 1
        a = array[i]
        for j in range(i, size):
            b = array[j]
            if a< b:
                count +=1
            a,b = b,None
            mv = max(mv, count)
    return mv

def longestIncSeqDP(array, size):
    """
    In this solution, we initialized 1 to every element in dp array of size "size". Then we checked started iterating
    over dp from 1 idex till end. Each time j starting from 0 and then we are comparing j's value with i's value in array.
    If it smaller then we are taking max of (dp[i]'s value , 1+dp[j]'s value). In th end , last idex has the max amount.

    Source: https://www.youtube.com/watch?v=CE2b_-XfVDk

    :param array:
    :param size:
    :return:
    """
    dp = [1 for i in range(size)]

    for i in range(1, size):
        for j in range(i):
            if array[j] < array[i]:
                dp[i] = max(dp[i], dp[j] + 1)

    return dp[-1]


if __name__ == '__main__':

    array = [3, 10, 2, 1, 20]
    size = len(array)
    print(longestIncSeq(array, size))
    print(longestIncSeqDP(array, size))
    print()

    # array = [50, 3, 10, 7, 40, 80]
    # size = len(array)
    # print(longestIncSeq(array, size))
    # print(longestIncSeqDP(array, size))
    # print()
    #
    #
    # array = [10, 22, 9, 33, 21, 50, 41, 60]
    # size = len(array)
    # print(longestIncSeq(array, size))
    # print(longestIncSeqDP(array, size))
    # print()
    #
    #
    # array = [3, 2]
    # size = len(array)
    # print(longestIncSeq(array, size))
    # print(longestIncSeqDP(array, size))
    # print()
    #
    #
    # array = [10,9,2,5,3,7,101,18]
    # size = len(array)
    # print(longestIncSeq(array, size))
    # print(longestIncSeqDP(array, size))
    # print()
    #
    #
