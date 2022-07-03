# 47. 全排列 II
from typing import List


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        used = [False for _ in nums]
        nums.sort()

        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])
            for i in range(len(nums)):
                if used[i]:
                    continue
                if i > 0 and nums[i] == nums[i-1] and not used[i-1]:
                    continue
                path.append(nums[i])
                used[i] = True
                backtrack()
                path.pop()
                used[i] = False
        backtrack()

        return res

if __name__ == '__main__':
    s = Solution()
    nums = [1, 1, 2]
    print(s.permuteUnique(nums))

