"""
977. Squares of a Sorted Array
Easy

Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.


Example 1:

Input: nums = [-4,-1,0,3,10]
Output: [0,1,9,16,100]
Explanation: After squaring, the array becomes [16,1,0,9,100].
After sorting, it becomes [0,1,9,16,100].
Example 2:

Input: nums = [-7,-3,2,3,11]
Output: [4,9,9,49,121]


Constraints:

1 <= nums.length <= 104
-104 <= nums[i] <= 104
nums is sorted in non-decreasing order.


Follow up: Squaring each element and sorting the new array is very trivial, could you find an O(n) solution using a different approach?
"""
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left , right = 0, len(nums)-1
        output = []
        while left <= right:
            l = nums[left] ** 2
            r = nums[right] ** 2
            if l > r:
                output.insert(0, l)
                left += 1
            else:
                output.insert(0, r)
                right -= 1

        return output

n = [-4, -1, 0, 3, 10]
print(Solution().sortedSquares(n))
n = [-5, -3, -2, -1]
print(Solution().sortedSquares(n))
n = [-1, 2, 2]
print(Solution().sortedSquares(n))
n = [2, 2]
print(Solution().sortedSquares(n))
n = [-2,0]
print(Solution().sortedSquares(n))
