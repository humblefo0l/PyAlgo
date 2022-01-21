from typing import List


class Solution:

    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        index = 0
        is_perm = False

        for i in range(len(nums) - 1, -1, -1):
            if nums[i] > nums[i - 1]:
                index = i - 1
                is_perm = True
                break

        if is_perm:
            i = self.nearest(nums, index, nums[index])
            nums[index], nums[i] = nums[i], nums[index]
            nums[index + 1:] = sorted(nums[index + 1:])
        else:
            sorted(nums)
        print(nums)

    def nearest(self, num, s, i):
        diff = 99999999
        l = {}
        for i in range(s, len(num)):
            if i < num[i]:
                d = num[i] - i
                if abs(diff) <= abs(d):
                    l[num[i]] = i
                    diff = i


        return l[0]

# a = [1,3,2]

a = [2,3,1]

s = Solution()
s.nextPermutation(a)