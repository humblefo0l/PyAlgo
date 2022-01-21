"""
39. Combination Sum
Medium

8691

203

Add to List

Share
Given an array of distinct integers candidates and a target integer target, return a list of all unique combinations of candidates where the chosen numbers sum to target. You may return the combinations in any order.

The same number may be chosen from candidates an unlimited number of times. Two combinations are unique if the frequency of at least one of the chosen numbers is different.

It is guaranteed that the number of unique combinations that sum up to target is less than 150 combinations for the given input.



Example 1:

Input: candidates = [2,3,6,7], target = 7
Output: [[2,2,3],[7]]
Explanation:
2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
7 is a candidate, and 7 = 7.
These are the only two combinations.
Example 2:

Input: candidates = [2,3,5], target = 8
Output: [[2,2,2,2],[2,3,3],[3,5]]
Example 3:

Input: candidates = [2], target = 1
Output: []

"""
from typing import List





class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        self._conbinationSum(candidates, target, [], 0, result)
        print(result)


    def _conbinationSum(self, candidates, target, temp_result, index, result):
        if target == 0:
            result.append(list(temp_result))
            return

        if target < 0:
            return

        for i in range(index, len(candidates)):
            if candidates[i] > target:
                continue
            temp_result.append(candidates[i])
            self._conbinationSum(candidates, target-candidates[i], temp_result, i, result)
            temp_result.pop(-1)




s = Solution()
# candidates = [2,3,6,7]
# target = 7
# s.combinationSum(candidates, target)

candidates = [2,7,6,3,5,1]
target = 9
s.combinationSum(candidates, target)