class Solution:
    def themaze(self, matrix, rowStart, colStart, rowDest, colDest):
        from collections import deque

        move = ((0, 1), (1, 0), (0, -1), (-1, 0))
        m = len(matrix)
        n = len(matrix[0])

        dq = deque()
        dq.append((rowStart, colStart, 0))

        while dq:
            i, j, step = dq.popleft()

            if (i, j) == (rowDest, colDest):
                return True

            for p, q in move:
                new_p = p + i
                new_q = q + j
                while m > new_p >= 0 <= new_q < n and matrix[new_p][new_q] != 1:
                    new_p += p
                    new_q += q
                new_p -= p
                new_q -= q
                if not matrix[new_p][new_q]:
                    matrix[new_p][new_q] = 2
                    dq.append((new_p, new_q, step + 1))

        return False

        # maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 1, 0], [1, 1, 0, 1, 1], [0, 0, 0, 0, 0]],
        # start = [0,
        #                                                                                                        4], destination = [
        #     3, 2]

        #
        # if start == end:
        #     return True
        # dq = deque()
        # dq.append((rowStart, colStart, None))
        # m = len(matrix)
        # n = len(matrix[0])
        # visited = set()
        # visited.add((rowStart, colStart))
        # while dq:
        #     i, j, prev = dq.popleft()
        #     for p, q in move:
        #         new_p = p + i
        #         new_q = q + j
        #         if m > new_p >= 0 <= new_q < n and (new_p, new_q) not in visited:
        #             visited.add((new_p, new_q))
        #             dq.append((new_p, new_p, ))

        # m = len(matrix)
        # n = len(matrix[0])
        # for p, q in move:
        #     new_p = end[0] + p
        #     new_q = end[1] + q
        #     if m < (end[0] + p) or  (end[1] + q) > n:
