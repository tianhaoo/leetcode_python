# 62. 不同路径


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        memo = {}

        def dp(i, j):
            if (i,j) in memo:
                return memo[(i, j)]
            if i < 0 or j < 0:
                memo[(i, j)] = 0
                return 0
            elif i == 0 and j == 0:
                memo[(i, j)] = 1
                return 1
            else:
                t = dp(i-1, j) + dp(i, j-1)
                memo[(i, j)] = t
                return t

        res = dp(m-1, n-1)
        return res



    def uniquePaths2(self, m: int, n: int) -> int:
        def next_step(i, j):
            if i == m-1:
                return (i, j+1),
            elif j == n-1:
                return (i+1, j),
            elif i < m-1 and j < n-1:
                return (i+1, j), (i, j+1)
            else:
                return tuple()

        res = []
        def backtrack(path, i, j):
            if i == m-1 and j == n-1:
                res.append(path[:])
                # print(path)
            else:
                for next_i, next_j in next_step(i, j):
                    path.append((next_i, next_j))
                    backtrack(path, next_i, next_j)
                    path.pop()
        backtrack([], 0, 0)
        return len(res)


if __name__ == '__main__':
    s = Solution()
    m = 23
    n = 12
    print(s.uniquePaths(m, n))