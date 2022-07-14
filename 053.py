# 53. 最大子数组和
from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        memo = {}

        def dp(x):  # dp函数定义为：以nums[x]结尾的 最大子数组和
            if x in memo:
                return memo[x]
            if x == 0:
                memo[x] = nums[x]
                return nums[x]
            else:
                t = max(nums[x], dp(x-1) + nums[x])
                memo[x] = t
                return t

        res = float("-inf")
        for i in range(len(nums)):
            res = max(res, dp(i))
        return res


if __name__ == '__main__':
    s = Solution()
    # nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    nums = [5,4,-1,7,8]
    print(s.maxSubArray(nums))