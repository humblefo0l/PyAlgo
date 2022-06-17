"""
169. Majority Element
Easy

10099

351

Add to List

Share
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2

"""


def majorityElement(nums) -> int:

    major = nums[0]
    count = 1

    for i in nums[1:]:
        if count == 0:
            major = i
            count = 1
            continue

        if i == major:
            count +=1
        else:
            count -= 1

    return major



nums = [3,2,3]
nums = [2,2,1,1,1,2,2]
majorityElement(nums)