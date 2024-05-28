from typing import List


class Solution:
    def highestPeak(self, isWater: List[List[int]]) -> List[List[int]]:
        from collections import deque
        m = len(isWater)
        n = len(isWater[0])
        dq = deque()
        water = []
        for i in range(m):
            for j in range(n):
                if isWater[i][j]:
                    dq.append((i, j, 0))
                    water.append((i, j))
        move = ((0, 1), (1, 0), (-1, 0), (0, -1))
        ans = 1
        while dq:
            i, j, height = dq.popleft()
            ans = max(height, ans)
            for p, q in move:
                new_p = p + i
                new_q = q + j
                if m > new_p >= 0 <= new_q < n and not isWater[new_p][new_q]:
                    isWater[new_p][new_q] = height + 1
                    dq.append((new_p, new_q, height + 1))
        for i, j in water:
            isWater[i][j] = 0
        return isWater


if __name__ == '__main__':
    print(Solution().highestPeak(isWater=[[0, 0, 1], [1, 0, 0], [0, 0, 0]]))
