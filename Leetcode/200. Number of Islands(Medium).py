# Given an m x n 2d grid map of '1's (land) and '0's (water), return the number of islands.
#
# An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically.
# You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
#
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
#
# Example 2:
#
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
#
# Constraints:
#
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        n = len(grid)
        m = len(grid[0])

        visited = [[False] * m for _ in range(n)]
        move = ((0, -1), (0, 1), (1, 0), (-1, 0))

        def dfs(i, j):
            visited[i][j] = True
            for p, q in move:
                left = i + p
                right = j + q
                if n > left > -1 and m > right > -1 and not visited[left][right] and grid[left][right] == "1":
                    dfs(left, right)

        total = 0
        for i in range(n):
            for j in range(m):
                if grid[i][j] == "1" and not visited[i][j]:
                    dfs(i, j)
                    total += 1
                    print(1111111111111)

        return total


if __name__ == "__main__":
    print(Solution().numIslands([["1", "1", "1"],
                                 ["0", "1", "0"],
                                 ["1", "1", "1"]]))
