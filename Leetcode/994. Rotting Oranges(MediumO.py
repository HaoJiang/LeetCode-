# In a given grid, each cell can have one of three values:
#
# the value 0 representing an empty cell;
# the value 1 representing a fresh orange;
# the value 2 representing a rotten orange.
# Every minute, any fresh orange that is adjacent (4-directionally) to a rotten orange becomes rotten.
#
# Return the minimum number of minutes that must elapse until no cell has a fresh orange.  If this is impossible, return -1 instead.
#
# Input: [[2,1,1],[1,1,0],[0,1,1]]
# Output: 4
# Example 2:
#
# Input: [[2,1,1],[0,1,1],[1,0,1]]
# Output: -1
# Explanation:  The orange in the bottom left corner (row 2, column 0) is never rotten, because rotting only happens 4-directionally.
#
# Input: [[0,2]]
# Output: 0
# Explanation:  Since there are already no fresh oranges at minute 0, the answer is just 0.
#
from typing import List


class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        from collections import deque
        # visited = set()
        m = len(grid)
        n = len(grid[0])
        good = 0
        dq = deque()
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    dq.append((i, j))
                    # visited.add((i, j))
                elif grid[i][j] == 1:
                    good += 1
        if not good:
            return 0

        # if not len(dq) and good:

        minutes = 0
        move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while dq:
            size = len(dq)
            minutes += 1
            for _ in range(size):
                gt = dq.popleft()
                for p, q in move:
                    x = p + gt[0]
                    y = q + gt[1]
                    if 0 <= x < m and 0 <= y < n  and grid[x][y] == 1:
                        dq.append((x, y))
                        grid[x][y] = 2
                        good -= 1

            if not good:
                return minutes

        return -1


if __name__ == "__main__":
    print(Solution().orangesRotting([[1,2]]))
