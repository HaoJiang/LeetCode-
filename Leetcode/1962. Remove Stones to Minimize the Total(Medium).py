from typing import List


class Solution:
    def minStoneSum(self, piles: List[int], k: int) -> int:
        import heapq

        for i in range(len(piles)):
            piles[i] = -piles[i]

        heapq.heapify(piles)
        for i in range(k):
            tp = heapq.heappop(piles)
            heapq.heappush(piles, -((-tp + 1) // 2))
        return -sum(piles)


if __name__ == '__main__':
    print(Solution().minStoneSum(piles=[4, 3, 6, 7], k=3))
