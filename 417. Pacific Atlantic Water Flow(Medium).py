# Given an m x n matrix of non-negative integers representing the height of each unit cell in a continent, the "Pacific ocean" touches the left and top edges of the matrix and the "Atlantic ocean" touches the right and bottom edges.
#
# Water can only flow in four directions (up, down, left, or right) from a cell to another one with height equal or lower.
#
# Find the list of grid coordinates where water can flow to both the Pacific and Atlantic ocean.
#
# Note:
#
# The order of returned grid coordinates does not matter.
# Both m and n are less than 150.
#
# Example:
#
# Given the following 5x5 matrix:
#
#   Pacific ~   ~   ~   ~   ~
#        ~  1   2   2   3  (5) *
#        ~  3   2   3  (4) (4) *
#        ~  2   4  (5)  3   1  *
#        ~ (6) (7)  1   4   5  *
#        ~ (5)  1   1   2   4  *
#           *   *   *   *   * Atlantic
#
# Return:
#
# [[0, 4], [1, 3], [1, 4], [2, 2], [3, 0], [3, 1], [4, 0]] (positions with parentheses in above matrix).
from typing import List


class Solution:
    def pacificAtlantic(self, matrix: List[List[int]]) -> List[List[int]]:
        if not matrix:
            return []
        p_land = set()
        a_land = set()
        R, C = len(matrix), len(matrix[0])

        def spread(i, j, land):
            land.add((i, j))
            for x, y in ((i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1)):
                if (0 <= x < R and 0 <= y < C and matrix[x][y] >= matrix[i][j]
                        and (x, y) not in land):
                    spread(x, y, land)

        for i in range(R):
            if (i, 0) not in p_land:
                spread(i, 0, p_land)
            if (i, C - 1) not in a_land:
                spread(i, C - 1, a_land)
        for j in range(C):
            if (0, j) not in p_land:
                spread(0, j, p_land)
            if (R - 1, j) not in a_land:
                spread(R - 1, j, a_land)
        return list(p_land & a_land)


if __name__ == "__main__":
    matrix = [[10, 8, 10, 7, 9],
              [5, 2, 10, 1, 5],
              [7, 4, 10, 6, 8],
              [8, 5, 10, 1, 1],
              [10, 1, 10, 4, 1]]
    print(Solution().pacificAtlantic(matrix))
