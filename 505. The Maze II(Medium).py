class Solution:
    def themaze(self, matrix, rowStart, colStart, rowDest, colDest):
        # from collections import deque
        import heapq

        move = ((0, 1), (1, 0), (0, -1), (-1, 0))
        m = len(matrix)
        n = len(matrix[0])
        #
        # dq = deque()
        # dq.append((rowStart, colStart, 0))
        hq = []
        heapq.heappush(hq, (0, rowStart, colStart))
        visited = {}
        while hq:
            step, i, j = heapq.heappop(hq)
            for p, q in move:
                new_p = p + i
                new_q = q + j
                count = 0
                while m > new_p >= 0 <= new_q < n and matrix[new_p][new_q] != 1:
                    new_p += p
                    new_q += q
                    count += 1
                new_p -= p
                new_q -= q

                if (i, j) == (rowDest, colDest):
                    return step + count
                if (new_p, new_q) not in visited or count + step < visited[(new_p, new_q)]:
                    visited[(new_p, new_q)] = step + count
                    heapq.heappush(hq, (step + count, new_p, new_q))
        return -1
