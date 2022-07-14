# 1143. 最长公共子序列
from Utils import trace


class Solution:
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        memo = {}
        def dp(i, j):  # text1[0,i]和 text2[0,j]的最长公共字串的长度
            if (i, j) in memo:
                return memo[(i, j)]
            elif i < 0 or j < 0:
                memo[(i, j)] = 0
                return 0
            elif text1[i] == text2[j]:
                t = dp(i - 1, j - 1) + 1
                memo[(i, j)] = t
                return t
            else:
                t = max(dp(i-1, j), dp(i, j-1))
                memo[(i, j)] = t
                return t
        res = dp(len(text1)-1, len(text2)-1)
        print(memo)
        return res



if __name__ == '__main__':
    s = Solution()
    text1 = "abcde"
    text2 = "rt"
    print(s.longestCommonSubsequence(text1, text2))