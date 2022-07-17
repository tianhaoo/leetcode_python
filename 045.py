# 45. 跳跃游戏 II
from typing import List


class Solution:
    def jump(self, nums: List[int]) -> int:
        memo = {}
        def dp(x):
            if x in memo:
                return memo[x]
            if x == 0:
                memo[x] = 1
                return 0
            else:
                res = float("inf")
                for i in range(0, x):
                    if nums[i] >= x-i:
                        res = min(res, dp(i) + 1)
                memo[x] = res
                return res

        t = dp(len(nums)-1)
        return t




if __name__ == '__main__':
    s = Solution()
    nums = [2, 3, 1, 1, 4]
    nums = [2, 3, 0, 1, 4]
    print(s.jump(nums))