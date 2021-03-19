from typing import List


class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        from collections import deque
        dq = deque()

        dq.append((0, 0))
        step = 0
        n = len(grid)
        if grid[0][0] or grid[n - 1][n - 1]:
            return -1
        grid[0][0] = 1
        # visited = set()
        # visited.add((0, 0))
        while dq:
            size = len(dq)
            step += 1
            for _ in range(size):
                i, j = dq.popleft()
                if (i, j) == (n - 1, n - 1):
                    return step
                for p, q in (i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1), (i + 1, j + 1), (i - 1, j - 1), (
                        i - 1, j + 1), (i + 1, j - 1):
                    if n > p >= 0 <= q < n and not grid[p][q]:
                        grid[p][q] = 1
                        dq.append((p, q))
        return -1

        # import heapq
        # hq = []
        # heapq.heappush(hq, (1, 0, 0))
        # m = len(grid)
        # n = len(grid[0])
        # if grid[0][0]:
        #     return -1
        # if (m - 1, n - 1) == (0, 0):
        #     return 1
        # visited = {(0, 0): 1}
        # while hq:
        #     step, i, j = heapq.heappop(hq)
        #     for p, q in (i + 1, j), (i, j + 1), (i - 1, j), (i, j - 1), (i + 1, j + 1), (i - 1, j - 1), (
        #             i - 1, j + 1), (i + 1, j - 1):
        #         if m > p >= 0 <= q < n and not grid[p][q]:
        #             if (p, q) == (m - 1, n - 1):
        #                 return step + 1
        #             if (p, q) not in visited or step + 1 < visited[(p, q)]:
        #                 visited[(p, q)] = step + 1
        #                 heapq.heappush(hq, (step + 1, p, q))
        # return -1


if __name__ == '__main__':
    print(Solution().shortestPathBinaryMatrix((
        [[0, 1, 0, 0, 0, 0],
         [0, 1, 1, 1, 1, 1],
         [0, 0, 0, 0, 1, 1],
         [0, 1, 0, 0, 0, 1],
         [1, 0, 0, 1, 0, 1],
         [0, 0, 1, 0, 1, 0]])))
