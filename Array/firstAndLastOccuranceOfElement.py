"""
34. Find First and Last Position of Element in Sorted Array
Medium

8844

267

Add to List

Share
Given an array of integers nums sorted in non-decreasing order, find the starting and ending position of a given target value.

If target is not found in the array, return [-1, -1].

You must write an algorithm with O(log n) runtime complexity.



Example 1:

Input: nums = [5,7,7,8,8,10], target = 8
Output: [3,4]
Example 2:

Input: nums = [5,7,7,8,8,10], target = 6
Output: [-1,-1]
Example 3:

Input: nums = [], target = 0
Output: [-1,-1]


Constraints:

0 <= nums.length <= 105
-109 <= nums[i] <= 109
nums is a non-decreasing array.
-109 <= target <= 109
"""
from typing import List


def searchRange(nums: List[int], target: int) -> List[int]:
    result = []
    left = _search_range(nums, target, True)
    right = _search_range(nums, target, False)


    result.append(left)
    result.append(right)

    return result


def _search_range(nums, target, go_left):
    start = 0
    end = len(nums)-1
    result = -1
    while start <= end:
        mid = start + (end-start)//2

        if nums[mid] == target:
            result = mid
            if go_left:
                end = mid-1
            else:
                start = mid + 1

        elif target < nums[mid]:
            end = mid -1

        else:
            start = mid + 1

    return result



nums = [5, 7, 7, 8, 8, 10]
target = 8
print(searchRange(nums, target))

nums = [5,7,7,8,8,10]
target = 6
print(searchRange(nums, target))

nums = []
target = 0
print(searchRange(nums, target))
