# 712. 两个字符串的最小ASCII删除和

class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        memo = {}
        def dp(i, j):  # s1[0,i] 和 s2[0,j] 的最长公共子序列的asii码和的最大值
            if (i, j) in memo:
                return memo[(i, j)]
            if i < 0 or j < 0:
                memo[(i, j)] = 0
                return 0
            elif s1[i] == s2[j]:
                t = dp(i-1, j-1) + ord(s1[i])
                memo[(i, j)] = t
                return t
            else:
                t = max(dp(i-1, j), dp(i, j-1))
                memo[(i, j)] = t
                return t

        res = dp(len(s1)-1, len(s2)-1)
        s1_sum = sum([ord(c) for c in s1])
        s2_sum = sum([ord(c) for c in s2])
        return s1_sum + s2_sum - 2 * res



if __name__ == '__main__':
    s = Solution()
    s1 = "sea"
    s2 = "eat"
    print(s.minimumDeleteSum(s1, s2))