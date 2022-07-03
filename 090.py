# 90. 子集 II
from typing import List


class Solution:


    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        res = []
        path = []

        def backtrack(start):
            res.append(path[:])

            for i in range(start, len(nums)):
                # 如果有相邻的树枝相同，则剪掉
                if i > start and nums[i] == nums[i-1]:
                    continue
                path.append(nums[i])
                backtrack(i+1)
                path.pop()

        # 先排序，让相同的元素靠在一起
        nums.sort()
        backtrack(0)
        return res


if __name__ == '__main__':
    s = Solution()
    nums = [2,1,2]
    print(s.subsetsWithDup(nums))

