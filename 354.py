# 354. 俄罗斯套娃信封问题
from typing import List


class Solution:
    def maxEnvelopes(self, envelopes: List[List[int]]) -> int:
        memo = {0: 1}
        # 先按照宽度升序，高度降序排序
        envelopes.sort(key=lambda lst:(lst[0], -lst[1]))
        # 然后找出宽度的最长递增子序列的长度，即为答案

        def dp(x):  # dp定义为：以envelopes[x][0]结尾的最长递增序列
            if x in memo:
                return memo[x]
            if x == 0:
                return 1
            else:
                m = 1
                for i in range(x):
                    if envelopes[x][1] > envelopes[i][1]:
                        m = max(m, dp(i)+1)
                memo[x] = m
                return m

        res = 1
        for j in range(len(envelopes)):
            res = max(res, dp(j))
        return res







if __name__ == '__main__':
    s = Solution()
    envelopes = [[1,3],[3,5],[6,7],[6,8],[8,4],[9,5]]
    print(s.maxEnvelopes(envelopes))