# 583. 两个字符串的删除操作

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        """还是求最长公共子序列"""
        memo = {}
        def dp(i, j):
            # 表示word1[0,i] 和 word2[0,j]的最长公共子序列的长度
            if (i,j) in memo:
                return memo[(i,j)]
            if i < 0 or j < 0:
                memo[(i, j)] = 0
                return 0
            elif word1[i] == word2[j]:
                t = dp(i-1, j-1) + 1
                memo[(i, j)] = t
                return t
            else:
                t = max(dp(i-1, j), dp(i, j-1))
                memo[(i, j)] = t
                return t

        n1, n2 = len(word1), len(word2)
        res = dp(n1 - 1, n2 - 1)
        return n1 + n2 - 2 * res




if __name__ == '__main__':
    s = Solution()
    # word1 = "sea"
    # word2 = "eat"
    word1 = "leetcode"
    word2 = "etco"
    print(s.minDistance(word1, word2))
