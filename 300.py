# 300. 最长递增子序列
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        # dp(x) 定义为以nums[x]结尾的最长递增子序列长度
        memo = {}

        def dp(x):
            if x in memo:
                return memo[x]
            if x == 0:
                memo[x] = 1
                return 1
            else:
                res = 1
                for i in range(x):
                    temp = dp(i)
                    if nums[x] > nums[i]:
                        res = max(res, temp + 1)
                memo[x] = res
                return res

        lst = [dp(i) for i in range(len(nums))]
        return max(lst)


if __name__ == '__main__':
    s = Solution()
    # nums = [0, 1, 0, 3, 2, 3]
    # nums = [7,7,7,7,7,7,7]
    # nums = [10, 9, 2, 5, 3, 7, 101, 18]
    nums = [1,3,6,7,9,4,10,5,6]
    print(s.lengthOfLIS(nums))
