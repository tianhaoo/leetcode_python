# 40. 组合总和 II
from typing import List


class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        candidates.sort()

        def backtrack(start):
            if sum(path) == target:
                res.append(path[:])
            if sum(path) > target:
                return
            for i in range(start, len(candidates)):
                # 相邻不能相同
                if i > start and candidates[i] == candidates[i-1]:
                    continue

                path.append(candidates[i])
                backtrack(i + 1)
                path.pop()

        backtrack(0)
        return res

if __name__ == '__main__':
    s = Solution()
    candidates = [2,5,2,1,2]
    target = 5
    print(s.combinationSum2(candidates, target))