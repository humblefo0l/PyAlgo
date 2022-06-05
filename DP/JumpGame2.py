"""45. Jump Game II
Medium

8182

296

Add to List

Share
Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.



Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2"""
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:

        left = right = 0
        result = 0

        while right < len(nums)-1:
            farthest = 0
            for i in range(left, right+1):
                farthest = max(farthest, i+nums[i])

            left = right + 1
            right = farthest
            result += 1

        return result

s = Solution()
nums = [2,3,1,1,4]
print(s.jump(nums))