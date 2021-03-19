#
# Given an n x n grid containing only values 0 and 1, where 0 represents water and 1 represents land,
# find a water cell such that its distance to the nearest land cell is maximized, and return the distance.
# If no land or water exists in the grid, return -1.
#
# The distance used in this problem is the Manhattan distance: the distance between two cells (x0, y0) and (x1, y1) is |x0 - x1| + |y0 - y1|.
#
# Input: grid = [[1,0,1],[0,0,0],[1,0,1]]
# Output: 2
# Explanation: The cell (1, 1) is as far as possible from all the land with distance 2.
#
# Input: grid = [[1, 0, 0], [0, 0, 0], [0, 0, 0]]
# Output: 4
# Explanation: The cell (2, 2) is as far as possible from all the land with distance 4.
#
# Constraints:
#
# n == grid.length
# n == grid[i].length
# 1 <= n <= 100
# grid[i][j] is 0 or 1
from typing import List, Tuple, Dict


class Solution:
    def maxDistance(self, grid: List[List[int]]) -> int:

        from collections import deque
        dq = deque()
        n = len(grid)
        for i in range(n):
            for j in range(n):
                if grid[i][j] == 1:
                    dq.append((i, j))
        if len(dq) == n ** 2 or not dq:
            return 0
        # visisted = set()
        move = [(0, -1), (0, 1), (1, 0), (-1, 0)]
        # up down left right
        distance = -1
        while dq:
            size = len(dq)
            distance += 1
            for _ in range(size):
                i, j = dq.popleft()
                grid[i][j] = -1
                # visisted.add((i, j))
                for mv in move:
                    p, q = i + mv[0], j + mv[1]
                    while n > p >= 0 and n > q >= 0 and grid[p][q] == 0:
                        grid[p][q] = 1
                        dq.append((p, q))

        return distance


if __name__ == "__main__":
    grid = [[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1],[1,1,1,1,1]]
    print(Solution().maxDistance(grid))
