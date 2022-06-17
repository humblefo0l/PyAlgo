"""
46. Permutations
Medium

10993

195

Add to List

Share
Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.



Example 1:

Input: nums = [1,2,3]
Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
Example 2:

Input: nums = [0,1]
Output: [[0,1],[1,0]]
Example 3:

Input: nums = [1]
Output: [[1]]
"""


class Solution:
    result = []

    def permute(self, nums):
        self.result=[]
        self._permute(nums, [])
        return self.result

    def _permute(self, nums, path):
        if not nums:
            self.result.append(path)

        for i in range(len(nums)):
            self._permute(nums[:i] + nums[i+1:], path + [nums[i]])

s = Solution()

nums = [1,2,3]
# nums = "ABC"
print(s.permute(nums))
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
