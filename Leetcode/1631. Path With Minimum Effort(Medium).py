from typing import List


class Solution:
    def minimumEffortPath(self, heights: List[List[int]]) -> int:
        import heapq

        m = len(heights)
        n = len(heights[0])
        pq = []
        visited = {}

        move = ((0, 1), (1, 0), (-1, 0), (0, -1))

        heapq.heappush(pq, (0, 0, 0))
        visited[(0, 0)] = float('-inf')
        while pq:
            diff, i, j = heapq.heappop(pq)
            print(diff, i, j)
            if i == m - 1 and j == n - 1:
                return diff
            for p, q in move:
                new_p = p + i
                new_q = q + j
                if m > new_p >= 0 <= new_q < n:
                    new_diff = max(abs(heights[new_p][new_q] - heights[i][j]), diff)
                    if (new_p, new_q) in visited:
                        if visited[(new_p, new_q)] > new_diff:
                            heapq.heappush(pq, (new_diff, new_p, new_q))
                            visited[(new_p, new_q)] = new_diff
                    else:
                        visited[(new_p, new_q)] = new_diff
                        heapq.heappush(pq, (new_diff, new_p, new_q))

        return -1


if __name__ == "__main__":
    print(Solution().minimumEffortPath(heights=[[4, 3, 4, 10, 5, 5, 9, 2],
                                                [10, 8, 2, 10, 9, 7, 5, 6],
                                                [5, 8, 10, 10, 10, 7, 4, 2],
                                                [5, 1, 3, 1, 1, 3, 1, 9],
                                                [6, 4, 10, 6, 10, 9, 4, 6]]))
# [[1,10,6,7,9,10,4,9]]
