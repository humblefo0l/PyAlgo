"""
53. Maximum Subarray
Easy

Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.



Example 1:

Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.
Example 2:

Input: nums = [1]
Output: 1
Example 3:

Input: nums = [5,4,-1,7,8]
Output: 23

"""


def maxSubArray( nums):
    csum = nums[0]
    osum = nums[0]

    for i in range(1, len(nums)):
        if csum > 0:
            csum += nums[i]
        else:
            csum = nums[i]

        if csum > osum:
            osum = csum

    return osum
    # n = len(nums)
    # # dp = [-1111] * n
    # dp = nums[0]
    # for i in range(1, n):
    #     # print(f"i: {i}, nums[i]: {nums[i]}, dp[i]: {dp[i]}, dp: {dp}")
    #
    #     s = nums[i] + dp[i-1]
    #
    #     if nums[i] > s:
    #         dp[i] = nums[i]
    #     else:
    #         dp[i] = nums[i] + dp[i - 1]
    #
    # return max(dp)

nums = [-2,1,-3,4,-1,2,1,-5,4]
print(maxSubArray(nums))

"""
n =  -2, 1, -3, 4, -1, 2, 1, -5, 4

-2, 1, -2, 4, 3, 5, 6, 1, 5 

"""