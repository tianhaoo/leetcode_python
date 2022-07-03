# 46. 全排列
import copy
from typing import List


class Solution:
    def __init__(self):
        self.path = []
        self.res = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(choices: List[int]) -> None:
            if not choices:
                self.res.append(self.path[:])

            for i, choice in enumerate(choices):
                self.path.append(choice)
                choices.pop(i)
                backtrack(choices)
                self.path.pop()
                choices.insert(i, choice)

        backtrack(nums)

        return self.res

    def permute2(self, nums):
        used = [False for _ in nums]
        path = []
        res = []
        def backtrack():
            if len(path) == len(nums):
                res.append(path[:])
            for i in range(len(nums)):
                if not used[i]:  # path里面的元素不能重复选择
                    path.append(nums[i])
                    used[i] = True
                    backtrack()
                    path.pop()
                    used[i] = False
        backtrack()
        return res



if __name__ == '__main__':
    s = Solution()
    print(s.permute2([1, 2, 3]))
