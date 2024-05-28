# Given an m x n board and a word, find if the word exists in the grid.
#
# The word can be constructed from letters of sequentially adjacent cells,
# where "adjacent" cells are horizontally or vertically neighboring.
# The same letter cell may not be used more than once.


# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true

from typing import List


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:

        m = len(board)
        n = len(board[0])
        k = len(word)
        move = ((0, 1), (1, 0), (0, -1), (-1, 0))

        def dfs(level, row, col, visited):
            if level == k:
                return True
            for p, q in move:
                new_p = p + row
                new_q = q + col
                if m > new_p >= 0 <= new_q < n and (new_p, new_q) not in visited and board[new_p][new_q] == word[level]:
                    visited.add((row, col))
                    if dfs(level + 1, new_p, new_q, visited):
                        return True
                    visited.discard((row, col))

            return False

        for i in range(m):
            for j in range(n):
                if board[i][j] == word[0]:
                    visited = set()
                    visited.add((i, j))
                    if dfs(1, i, j, visited):
                        return True

        return False


if __name__ == "__main__":
    print(Solution().exist(board=[["C", "A", "A"], ["A", "A", "A"], ["B", "C", "D"]], word="AAB"))
