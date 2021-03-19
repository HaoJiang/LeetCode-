# In a given 2D binary array A, there are two islands.  (An island is a 4-directionally connected group of 1s not connected to any other 1s.)
#
# Now, we may change 0s to 1s so as to connect the two islands together to form 1 island.
#
# Return the smallest number of 0s that must be flipped.  (It is guaranteed that the answer is at least 1.)
#
# Example 1:
#
# Input: A = [[0,1],[1,0]]
# Output: 1
# Example 2:
#
# Input: A = [[0,1,0],[0,0,0],[0,0,1]]
# Output: 2
# Example 3:
#
# Input: A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
# Output: 1
#
#
# Constraints:
#
# 2 <= A.length == A[0].length <= 100
# A[i][j] == 0 or A[i][j] == 1
from typing import List


class Solution:
    def shortestBridge(self, A: List[List[int]]) -> int:
        move = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        n = len(A)
        m = len(A[0])
        from collections import deque
        dq = deque()
        t = 2
        distance = 0
        seen1 = set()
        for i in range(n):
            for j in range(m):
                if A[i][j] == 1:
                    dq.append((i, j))
                    t -= 1
                    while dq:
                        if not t:
                            size = len(dq)
                            for _ in range(size):
                                p, q = dq.popleft()
                                seen1.add((p, q))
                                A[p][q] = 3
                                for k in move:
                                    if n > p + k[0] >= 0 and m > q + k[1] >= 0 and A[p + k[0]][q + k[1]] == 1:
                                        A[p + k[0]][q + k[1]] = 3
                                        dq.append((p + k[0], q + [1]))
                                        seen1.add((p + k[0], q + [1]))
                        else:
                            p, q = dq.popleft()
                            A[p][q] = 2
                            for k in move:
                                if n > p + k[0] >= 0 and m > q + k[1] >= 0 and A[p + k[0]][q + k[1]] == 1:
                                    A[p + k[0]][q + k[1]] = 2
                                    dq.append((p + k[0], q + k[1]))

        new_dq = deque(seen1)
        visited = set()
        while new_dq:
            size = len(new_dq)
            distance += 1
            for _ in range(size):
                p, q = new_dq.popleft()
                visited.add((p, q))
                for k in move:
                    if n > p + k[0] >= 0 and m > q + k[1] >= 0 and (p + k[0], q + k[1]) not in visited:
                        if A[p + k[0]][q + k[1]] == 2:
                            return distance - 1
                        elif A[p + k[0]][q + k[1]] == 0:
                            new_dq.append((p + k[0], q + k[1]))
                            visited.add((p + k[0], q + k[1]))


if __name__ == "__main__":
    print(Solution().shortestBridge(
        [[0, 1, 0], [0, 0, 0], [0, 0, 1]]))
