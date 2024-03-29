"""
287. Find the Duplicate Number
Medium

14351

1756

Add to List

Share
Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

There is only one repeated number in nums, return this repeated number.

You must solve the problem without modifying the array nums and uses only constant extra space.



Example 1:

Input: nums = [1,3,4,2,2]
Output: 2
Example 2:

Input: nums = [3,1,3,4,2]
Output: 3


Constraints:

1 <= n <= 105
nums.length == n + 1
1 <= nums[i] <= n
All the integers in nums appear only once except for precisely one integer which appears two or more times.

"""
from typing import List


def findDuplicate(nums: List[int]) -> int:
    p = s = f = 0

    while s == 0 or nums[s] != nums[f]:
        s = nums[s]
        f = nums[nums[f]]

    while nums[s] != nums[p]:
        s = nums[s]
        p = nums[p]

    return nums[s]



nums = [1,3,4,2,2]
nums = [3,1,3,4,2]
print(findDuplicate(nums))