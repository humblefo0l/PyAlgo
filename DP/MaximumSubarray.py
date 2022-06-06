"""
53. Maximum Subarray
Easy

21323

1050

Add to List

Share
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


Constraints:

1 <= nums.length <= 105
-104 <= nums[i] <= 104


Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        #         n = len(nums)
        #         dp = [None]* n
        #         dp[0] = nums[0]
        #         for i in range(1, n):
        #             if nums[i] > nums[i] + dp[i-1]:
        #                 dp[i] = nums[i]
        #             else:
        #                 dp[i] = nums[i]+ dp[i-1]

        #         return max(dp)

        #  ****************   METHOD 2 ******************
        #         csum = nums[0]
        #         osum = nums[0]

        #         for i in range(1, len(nums)):
        #             if csum > 0:
        #                 csum += nums[i]
        #             else:
        #                 csum = nums[i]

        #             if csum > osum:
        #                 osum = csum

        #         return osum

        #     ****************   METHOD 3 ******************
        cmax = nums[0]
        omax = nums[0]

        for i in range(1, len(nums)):
            cmax = max(cmax + nums[i], nums[i])
            omax = max(cmax, omax)

        return omax

s  = Solution()
nums = [-2,1,-3,4,-1,2,1,-5,4]
print(s.maxSubArray(nums))