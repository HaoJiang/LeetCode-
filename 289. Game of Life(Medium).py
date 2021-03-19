# Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

from typing import List


class Solution:
    def gameOfLife(self, board: List[List[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        from collections import deque
        from copy import copy, deepcopy
        dq = deque()

        matrix = deepcopy(board)

        move = ((0, 1), (1, 0), (0, -1), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1))

        def cal(i, j):
            lives_cell = 0
            # dies_cell = 0
            for p, q in move:
                new_i = i + p
                new_j = j + q
                if m > new_i >= 0 <= new_j < n:
                    if matrix[new_i][new_j]:
                        lives_cell += 1
                    # else:
                    #     dies_cell += 1

            if matrix[i][j]:
                if lives_cell == 2 or lives_cell == 3:
                    return 1
                elif lives_cell > 3:
                    return 0
            else:
                if lives_cell == 3:
                    return 1
            return 0

        m = len(board)
        n = len(board[0])
        matrix = deepcopy(board)
        for i in range(m):
            for j in range(n):
                k = cal(i, j)
                board[i][j] = k

        return board


if __name__ == "__main__":
    print(Solution().gameOfLife([[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]))
    # [[0, 1, 0], [0, 0, 1], [1, 1, 1], [0, 0, 0]]
