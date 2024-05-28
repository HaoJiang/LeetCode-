# On an N x N board, the numbers from 1 to N*N are written boustrophedonically starting
# from the bottom left of the board, and alternating direction each row.  For example,
# for a 6 x 6 board, the numbers are written as follows:

from typing import List
class Solution:
    def snakesAndLadders(self, board: List[List[int]]) -> int:

        ### N * N  from 1 to N * N
        # important is cal the row and col

        #    divmod(row, n ) n == total row
        from collections import deque
        dq = deque()

        n = len(board)
        def calRowandCol(point):

            row, col = divmod(point - 1, n)

            if row % 2:
                # mean odd ==  reverse line
                return n - row - 1, n - col - 1
            else:
                # mean ordered and the row form bottom to up
                return n - row - 1, col

        count = n * n
        step = 0
        dq.append((1, step))
        visited = set()
        visited.add(1)

        while dq:
            curr, step = dq.popleft()
            for i in range(curr + 1, curr + 7):
                row, col = calRowandCol(i)
                if board[row][col] > 0:
                    i = board[row][col]
                if i == count:
                    return step + 1
                if i not in visited:
                    dq.append((i, step + 1))
                    visited.add(i)
        return -1


if __name__ == "__main__":
    print(Solution().snakesAndLadders([[-1,-1,-1,46,47,-1,-1,-1],
                                       [51,-1,-1,63,-1,31,21,-1],
                                       [-1,-1,26,-1,-1,38,-1,-1],
                                       [-1,-1,11,-1,14,23,56,57]]))

