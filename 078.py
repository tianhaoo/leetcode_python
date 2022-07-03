# 78. 子集
from copy import deepcopy
from typing import List


class Solution:

    def subsets(self, nums: List[int]) -> List[List[int]]:
        path = []
        res = []
        def backtrack(start):
            res.append(path[:])

            for i in range(start, len(nums)):
                path.append(nums[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return res


    def subsets2(self, nums: List[int]) -> List[List[int]]:
        path = []
        paths = []

        def backtracking(startindex):
            paths.append(path[:])
            for i in range(startindex, len(nums)):
                path.append(nums[i])
                backtracking(i + 1)
                path.pop()

        backtracking(0)
        return paths

if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3]
    print(s.subsets(nums))




