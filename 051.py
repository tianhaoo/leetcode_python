# 51. N 皇后
import copy
from typing import List


class Solution:

    def gen_empty_board(self, n):
        return [["." for i in range(n)] for j in range(n)]

    def check(self, board, r, c):
        # 检查行
        row = board[r]
        for x in row:
            if x == "Q":
                return False
        # 检查列
        col = [row[c] for row in board]
        for x in col:
            if x == "Q":
                return False
        # 检查左上
        i, j = r, c
        while i >= 0 and j >=0:
            if board[i][j] == "Q":
                return False
            i -= 1
            j -= 1
        # 检查右下
        i, j = r, c
        while i < len(board) and j < len(board[0]):
            if board[i][j] == "Q":
                return False
            i += 1
            j += 1

        # 检查右上
        i, j = r, c
        while i < len(board) and j >= 0:
            if board[i][j] == "Q":
                return False
            i += 1
            j -= 1
        # 检查左下
        i, j = r, c
        while i >= 0 and j < len(board[0]):
            if board[i][j] == "Q":
                return False
            i -= 1
            j += 1

        return True



    def solveNQueens(self, n: int) -> List[List[str]]:
        def backtrack(res, board, current_r):
            if current_r == n:
                res.append(copy.deepcopy(board))
                return
            for c in range(n):
                if self.check(board, current_r, c):
                    board[current_r][c] = "Q"
                    backtrack(res, board, current_r+1)
                    board[current_r][c] = "."


        board = self.gen_empty_board(n)
        res = []
        backtrack(res, board, 0)
        ans = []
        for lst in res:
            temp = []
            for line in lst:
                temp.append("".join(line))
            ans.append(temp)
        return ans


if __name__ == '__main__':
    s = Solution()
    print(s.solveNQueens(4))
