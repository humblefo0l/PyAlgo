"""
Maximum Sum Increasing Subsequence | DP-14
Given an array of n positive integers. Write a program to find the sum of maximum sum subsequence of
the given array such that the integers in the subsequence are sorted in increasing order. For example,
if input is {1, 101, 2, 3, 100, 4, 5}, then output should be 106 (1 + 2 + 3 + 100), if the input array
is {3, 4, 5, 10}, then output should be 22 (3 + 4 + 5 + 10) and if the input array is {10, 5, 4, 3},
then output should be 10
"""



def maxSumIS(a,n):

    dp = [i for i in a]

    for i in range(1, n):
        m = a[i]
        for j in range(i):

            if a[i] > a[j]:

                m = max(m, dp[i] + dp[j])
        dp[i] = m
    print(dp)
    return max(dp)



arr = [1, 101, 2, 3, 100, 4, 5]
n = len(arr)
print("Sum of maximum sum increasing subsequence is "  + str(maxSumIS(arr, n)))
