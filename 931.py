# 931. 下降路径最小和
from typing import List


class Solution:
    def minFallingPathSum(self, matrix: List[List[int]]) -> int:
        n = len(matrix)
        memo = {}
        # dp函数定义：从第一行落到i,j的路径最小和
        def dp(i, j):
            if (i,j) in memo:
                return memo[(i,j)]
            if i == 0:
                memo[(i, j)] = matrix[i][j]
                return matrix[i][j]
            else:
                m = float("inf")
                for col in (j-1, j, j+1):
                    if 0 <= col < n:
                        m = min(m, dp(i-1, col) + matrix[i][j])
                memo[(i, j)] = m
                return m

        res = float("inf")
        for c in range(n):
            res = min(res, dp(n-1, c))
        return res

if __name__ == '__main__':
    s = Solution()
    matrix = [[2, 1, 3], [6, 5, 4], [7, 8, 9]]
    # matrix = [[-19, 57], [-40, -5]]
    print(s.minFallingPathSum(matrix))