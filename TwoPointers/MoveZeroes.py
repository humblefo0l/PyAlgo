"""
283. Move Zeroes
Easy

Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the non-zero elements.

Note that you must do this in-place without making a copy of the array.



Example 1:

Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]
Example 2:

Input: nums = [0]
Output: [0]


Constraints:

1 <= nums.length <= 104
-231 <= nums[i] <= 231 - 1


Follow up: Could you minimize the total number of operations done?
"""
from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1 = p2 = 0
        move_zero = False
        while p2 < len(nums):
            # print(f'p1: {p1} p2: {p2}, len: {len(nums)}')
            if nums[p1]==0 and nums[p2] == 0:
                move_zero = True
                p2 += 1
                continue

            if move_zero:
                if nums[p2] == 0:
                    p2 += 1
                    continue

                nums[p1], nums[p2] = nums[p2], nums[p1]

            p1 += 1
            p2 += 1



# Input:
nums = [0,1,0,3,12]
Solution().moveZeroes(nums)
print(nums)

nums = [0]
Solution().moveZeroes(nums)
print(nums)

nums = [1]
Solution().moveZeroes(nums)
print(nums)