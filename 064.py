# 64. 最小路径和
from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:
        memo = {}
        def dp(x, y):
            if (x, y) in memo:
                return memo[(x, y)]
            if x < 0 or y < 0:
                memo[(x, y)] = float("inf")
                return float("inf")
            elif x == 0 and y == 0:
                memo[(x, y)] = grid[0][0]
                return grid[0][0]
            else:
                t = min(dp(x-1, y)+grid[x][y], dp(x, y-1)+grid[x][y])
                memo[(x, y)] = t
                return t
        res = dp(len(grid)-1, len(grid[0])-1)
        return res


if __name__ == '__main__':
    s = Solution()
    grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
    grid = [[1, 2, 3], [4, 5, 6]]
    print(s.minPathSum(grid))