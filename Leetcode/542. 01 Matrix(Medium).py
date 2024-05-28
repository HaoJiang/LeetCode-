# Given a matrix consists of 0 and 1, find the distance of the nearest 0 for each cell.
#
# The distance between two adjacent cells is 1.
#
# Example 1:
#
# Input:
# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]
#
# Output:
# [[0,0,0],
#  [0,1,0],
#  [0,0,0]]
#
# Example 2:
#
# Input:
# [[0,0,0],
#  [0,1,0],
#  [1,1,1]]
#
# Output:
# [[0,0,0],
#  [0,1,0],
#  [1,2,1]]

from typing import List


class Solution:
    def updateMatrix(self, matrix: List[List[int]]) -> List[List[int]]:

        from collections import deque
        dq = deque()
        n = len(matrix)
        m = len(matrix[0])
        visited = set()
        for i in range(n):
            for j in range(m):
                if matrix[i][j] == 0:
                    dq.append((i, j))
                    visited.add((i, j))

        move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        while dq:
            p, q = dq.popleft()
            for k in move:
                if 0 <= p + k[0] < n and 0 <= q + k[1] < m and matrix[p + k[0]][q + k[1]] != 0 and (
                        p + k[0], q + k[1]) not in visited:
                    matrix[p + k[0]][q + k[1]] = matrix[p][q] + 1
                    visited.add((p + k[0], q + k[1]))
                    dq.append((p + k[0], q + k[1]))
        return matrix

print(Solution().updateMatrix([[0,0,0],
 [0,1,0],
 [1,1,1]]))
