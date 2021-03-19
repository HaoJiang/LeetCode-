# # Write a program to solve a Sudoku puzzle by filling the empty cells.
# #
# # A sudoku solution must satisfy all of the following rules:
# #
# # Each of the digits 1-9 must occur exactly once in each row.
# # Each of the digits 1-9 must occur exactly once in each column.
# # Each of the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.
# # The '.' character indicates empty cells.
#
# Input: board = [["5","3",".",".","7",".",".",".","."],
#                 ["6",".",".","1","9","5",".",".","."],
#                 [".","9","8",".",".",".",".","6","."],
#                 ["8",".",".",".","6",".",".",".","3"],
#                 ["4",".",".","8",".","3",".",".","1"],
#                 ["7",".",".",".","2",".",".",".","6"],
#                 [".","6",".",".",".",".","2","8","."],
#                 [".",".",".","4","1","9",".",".","5"],
#                 [".",".",".",".","8",".",".","7","9"]]
# Output: [["5","3","4","6","7","8","9","1","2"],
#          ["6","7","2","1","9","5","3","4","8"],
#          ["1","9","8","3","4","2","5","6","7"],
#          ["8","5","9","7","6","1","4","2","3"],
#          ["4","2","6","8","5","3","7","9","1"],
#          ["7","1","3","9","2","4","8","5","6"],
#          ["9","6","1","5","3","7","2","8","4"],
#          ["2","8","7","4","1","9","6","3","5"],
#          ["3","4","5","2","8","6","1","7","9"]]
# Explanation: The input board is shown above and the only valid solution is shown below:
#
# Constraints:
#
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit or '.'.
# It is guaranteed that the input board has only one solution.


class Solution(object):
    def solveSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: None Do not return anything, modify board in-place instead.
        """
        # from collections import deque
        ROW = [set() for _ in range(9)]
        COL = [set() for _ in range(9)]
        CUBE = [[set() for _ in range(3)] for _ in range(3)]
        stack = []
        self.number = {"1", "2", "3", "4", "5", "6", "7", "8", "9"}

        for i in range(9):
            for j in range(9):
                ch = board[i][j]
                if ch == ".":
                    stack.append((i, j))
                else:
                    ROW[i].add(ch)
                    COL[j].add(ch)
                    CUBE[i // 3][j // 3].add(ch)

        def dfs():
            if not stack:
                return True
            row, col = stack.pop()
            rst = self.number - ROW[row] - COL[col] - CUBE[row // 3][col // 3]
            for num in rst:
                board[row][col] = num
                ROW[row].add(num)
                COL[col].add(num)
                CUBE[row // 3][col // 3].add(num)
                if dfs():
                    return True
                ROW[row].discard(num)
                COL[col].discard(num)
                CUBE[row // 3][col // 3].discard(num)
            # print(ROW, COL, CUBE)

            stack.append((row, col))
            return False

        dfs()



if __name__ == "__main__":
    board = [["5", "3", ".", ".", "7", ".", ".", ".", "."], ["6", ".", ".", "1", "9", "5", ".", ".", "."],
             [".", "9", "8", ".", ".", ".", ".", "6", "."], ["8", ".", ".", ".", "6", ".", ".", ".", "3"],
             ["4", ".", ".", "8", ".", "3", ".", ".", "1"], ["7", ".", ".", ".", "2", ".", ".", ".", "6"],
             [".", "6", ".", ".", ".", ".", "2", "8", "."], [".", ".", ".", "4", "1", "9", ".", ".", "5"],
             [".", ".", ".", ".", "8", ".", ".", "7", "9"]]

    print(Solution().solveSudoku(board))

