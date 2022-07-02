# 46. 全排列
import copy
from typing import List


class Solution:
    def __init__(self):
        self.res = []

    def permute(self, nums: List[int]) -> List[List[int]]:
        def backtrack(path: List[int], choices: List[int]) -> None:
            if not choices:
                self.res.append(copy.deepcopy(path))

            for i, choice in enumerate(choices):
                path.append(choice)
                choices.remove(choice)
                backtrack(path, choices)
                path.remove(choice)
                choices.insert(i, choice)
        path = []
        backtrack(path, nums)

        return self.res


if __name__ == '__main__':
    s = Solution()
    print(s.permute([1, 2, 3]))
