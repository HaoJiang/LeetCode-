from typing import List


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        import heapq

        hq = []
        for i, j in classes:
            hq.append((-((i + 1) / (j + 1) - i / j), i, j))
        heapq.heapify(hq)

        while extraStudents:
            gain, i, j = heapq.heappop(hq)
            i += 1
            j += 1
            heapq.heappush(hq, (-((i + 1) / (j + 1) - i / j), i, j))
            extraStudents -= 1

        res = 0
        while hq:
            _, i, j = heapq.heappop(hq)
            res += (i / j)

        return res / len(classes)


if __name__ == '__main__':
    print(Solution().maxAverageRatio(classes=[[1, 2], [3, 5], [2, 2]], extraStudents=2))
