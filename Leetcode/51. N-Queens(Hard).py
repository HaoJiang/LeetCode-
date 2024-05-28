# The n-queens puzzle is the problem of placing n queens on an n x n chessboard such that no two queens attack each other.
#
# Given an integer n, return all distinct solutions to the n-queens puzzle.
#
# Each solution contains a distinct board configuration of the n-queens' placement, where 'Q' and '.' both indicate a queen and an empty space, respectively.
# Input: n = 4
# Output: [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
# Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above
#
# Example 2:
#
# Input: n = 1
# Output: [["Q"]]

# Constraints:
#
# 1 <= n <= 9
from typing import List


class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        from collections import defaultdict

        ROW = defaultdict(int)
        COL = defaultdict(int)
        DIA_L = defaultdict(int)
        DIA_R = defaultdict(int)
        self.board = [["."] * n for _ in range(n)]
        self.res = []

        # for i in range(n):
        #     for j in range(n):
        #         stack.append((i, j))
        def dfs(i):
            if i == n:
                self.res.append([''.join(i) for i in self.board])
            for j in range(n):
                if not ROW[i] and not COL[j] and not DIA_L[i - j] and not DIA_R[i + j]:
                    self.board[i][j] = "Q"
                    ROW[i] += 1
                    COL[j] += 1
                    DIA_L[i - j] += 1
                    DIA_R[i + j] += 1
                    dfs(i + 1)
                    self.board[i][j] = "."
                    ROW[i] -= 1
                    COL[j] -= 1
                    DIA_L[i - j] -= 1
                    DIA_R[i + j] -= 1

        dfs(0)
        return self.res

if __name__ == "__main__":

    print(Solution().solveNQueens(4))