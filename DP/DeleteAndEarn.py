"""
740. Delete and Earn
Medium

4857

272

Add to List

Share
You are given an integer array nums. You want to maximize the number of points you get by performing the following operation any number of times:

Pick any nums[i] and delete it to earn nums[i] points. Afterwards, you must delete every element equal to nums[i] - 1 and every element equal to nums[i] + 1.
Return the maximum number of points you can earn by applying the above operation some number of times.



Example 1:

Input: nums = [3,4,2]
Output: 6
Explanation: You can perform the following operations:
- Delete 4 to earn 4 points. Consequently, 3 is also deleted. nums = [2].
- Delete 2 to earn 2 points. nums = [].
You earn a total of 6 points.
Example 2:

Input: nums = [2,2,3,3,3,4]
Output: 9
Explanation: You can perform the following operations:
- Delete a 3 to earn 3 points. All 2's and 4's are also deleted. nums = [3,3].
- Delete a 3 again to earn 3 points. nums = [3].
- Delete a 3 once more to earn 3 points. nums = [].
You earn a total of 9 points.


Constraints:

1 <= nums.length <= 2 * 104
1 <= nums[i] <= 104
"""
from collections import Counter
from typing import List


class Solution:
    def deleteAndEarn(self, nums: List[int]) -> int:
        earn1 = earn2 = 0
        count = Counter(nums)
        nums = sorted(set(nums))
        for i in range(len(nums)):
            currentValue = nums[i] * count[nums[i]]
            if i > 0 and nums[i] == nums[i-1] + 1:
                temp = max(currentValue + earn1, earn2)
                earn1 = earn2
                earn2 = temp
            else:
                temp = currentValue + earn2
                earn1 = earn2
                earn2 = temp
        return earn2





s = Solution()
nums = [3,4,2]
print(s.deleteAndEarn(nums))
nums = [2,2,3,3,3,4]
print(s.deleteAndEarn(nums))