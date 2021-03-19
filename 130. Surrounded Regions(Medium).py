# Given a 2D board containing 'X' and 'O' (the letter O), capture all regions surrounded by 'X'.
#
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
# Example:
#
# X X X X
# X O O X
# X X O X
# X O X X
#
# After running your function, the board should be:
#
# X X X X
# X X X X
# X X X X
# X O X X

# Explanation:
#
# Surrounded regions shouldn’t be on the border,
# which means that any 'O' on the border of the board are not flipped to 'X'.
# Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'.
# Two cells are connected if they are adjacent cells connected horizontally or vertically.

from typing import List


class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        from collections import deque
        dq = deque()

        m = len(board)
        n = len(board[0])
        seen = set()
        visited = set()

        for i in range(m):
            for j in range(n):
                if (i == 0 or i == m - 1 or j == 0 or j == n - 1) and board[i][j] == "O":
                    dq.append((i, j))
                    visited.add((i, j))
                else:
                    if board[i][j] == 'O':
                        board[i][j] = "X"
                        seen.add((i, j))
        if not dq:
            return board
        move = ((0, 1), (1, 0), (-1, 0), (0, -1))
        while dq:
            row, col = dq.popleft()
            for p, q in move:
                new_p = row + p
                new_q = col + q
                if m > new_p >= 0 <= new_q < n and (new_p, new_q) not in visited and (new_p, new_q) in seen:
                    visited.add((new_p, new_q))
                    seen.discard((new_p, new_q))
                    board[new_p][new_q] = "O"
                    dq.append((new_p, new_q))

        return board


if __name__ == "__main__":
    board = [5 * ['X'] for i in range(5)]
    board[0][3] = "O"
    board[1][3] = "O"
    board[3][1] = "O"
    board[2][2] = "O"
    board[0][3] = "O"
    board[4][3] = "O"

    # [["X", "O", "X", "O", "X", "O"],
    #  ["O", "X", "X", "X", "X", "X"],
    #  ["X", "X", "X", "O", "X", "X"],
    #  ["O", "X", "O", "X", "O", "X"]]

    # [["X", "O", "X", "O", "X", "O"],
    #  ["O", "X", "X", "X", "X", "X"],
    #  ["X", "X", "X", "X", "X", "O"],
    #  ["O", "X", "O", "X", "O", "X"]]

    # [['X', 'O', 'X', 'O', 'X', 'O'],
    #  ['O', 'X', 'X', 'X', 'X', 'X'],
    #  ['X', 'X', 'X', 'X', 'X', 'O'],
    #  ['O', 'X', 'O', 'X', 'O', 'X']]
    print(Solution().solve([["X", "O", "X", "O", "X", "O"],
                            ["O", "X", "O", "X", "O", "X"],
                            ["X", "O", "X", "O", "X", "O"],
                            ["O", "X", "O", "X", "O", "X"]]))
