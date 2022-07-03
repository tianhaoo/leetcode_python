from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        path = []
        res = []
        def backtrack(start):
            s = sum(path)
            if s == target:
                res.append(path[:])
            if s > target:
                return
            for i in range(start, len(candidates)):
                path.append(candidates[i])
                backtrack(i)
                path.pop()

        backtrack(0)
        return res




if __name__ == '__main__':
    s = Solution()
    candidates = [2,3,6,7]
    target = 7
    print(s.combinationSum(candidates,target))