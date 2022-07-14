# 516. 最长回文子序列
from Utils import trace


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        if len(s) == 1:
            return 1

        memo = {}
        def dp(i, j):  # s[i, j] 中最长回文子序列的长度
            if (i, j) in memo:
                return memo[(i, j)]
            if i > j or i < 0 or j < 0 or i > len(s) - 1 or j > len(s) - 1:
                memo[(i, j)] = 0
                return 0
            elif s[i] == s[j]:
                t = dp(i + 1, j - 1) + 2
                memo[(i, j)] = t
                return t
            else:
                t = max(dp(i, j - 1), dp(i + 1, j))
                memo[(i, j)] = t
                return t
        res = dp(0, len(s) - 1)
        return res



if __name__ == '__main__':
    solution = Solution()
    s = "bbbab"
    print(solution.longestPalindromeSubseq(s))
