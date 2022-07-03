# 77. 组合

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        path = []
        nums = [i for i in range(1, n + 1)]
        def backtrack(start):
            if len(path) == k:
                res.append(path[:])
            else:
                for i in range(start, len(nums)):
                    path.append(nums[i])
                    backtrack(i + 1)
                    path.pop()
        k = k

        backtrack(0)
        return res

if __name__ == '__main__':
    s = Solution()
    print(s.combine(4, 2))