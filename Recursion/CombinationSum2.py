"""
40. Combination Sum II
Medium

4328

121

Add to List

Share
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

Each number in candidates may only be used once in the combination.

Note: The solution set must not contain duplicate combinations.



Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8
Output:
[
[1,1,6],
[1,2,5],
[1,7],
[2,6]
]
Example 2:

Input: candidates = [2,5,2,1,2], target = 5
Output:
[
[1,2,2],
[5]
]


Constraints:

1 <= candidates.length <= 100
1 <= candidates[i] <= 50
1 <= target <= 30
"""
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        candidates.sort()
        self._combinationSum2(candidates, target, 0, [], result)
        return result

    def _combinationSum2(self, candidates, target, index, temp_result,  result):
        if target == 0:
            if temp_result not in result:
                result.append(list(temp_result))

        if target < 0:
            return

        for i in range(index, len(candidates)):
            temp_result.append(candidates[i])
            self._combinationSum2(candidates, target-candidates[i], i+1, temp_result, result)
            temp_result.pop()


s = Solution()
candidates = [10,1,2,7,6,1,5]
target = 8
# print(s.combinationSum2(candidates, target))
candidates = [2,5,2,1,2]
target = 5
print(s.combinationSum2(candidates, target))