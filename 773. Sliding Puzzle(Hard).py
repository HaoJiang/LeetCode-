# # On a 2x3 board, there are 5 tiles represented by the integers 1 through 5, and an empty square represented by 0.
# #
# # A move consists of choosing 0 and a 4-directionally adjacent number and swapping it.
# #
# # The state of the board is solved if and only if the board is [[1,2,3],[4,5,0]].
# #
# # Given a puzzle board, return the least number of moves required so that the state of the board is solved.
# # If it is impossible for the state of the board to be solved, return -1.
#
# Input: board = [[4,1,2],[5,0,3]]
# Output: 5
# Explanation: 5 is the smallest number of moves that solves the board.
# An example path:
# After move 0: [[4,1,2],[5,0,3]]
# After move 1: [[4,1,2],[0,5,3]]
# After move 2: [[0,1,2],[4,5,3]]
# After move 3: [[1,0,2],[4,5,3]]
# After move 4: [[1,2,0],[4,5,3]]
# After move 5: [[1,2,3],[4,5,0]]
#
# Note:
#
# board will be a 2 x 3 array as described above.
# board[i][j] will be a permutation of [0, 1, 2, 3, 4, 5].

from typing import List


class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        s = ''.join(str(col) for row in board for col in row)
        from collections import deque
        dq = deque()
        dq.append((s, s.index('0'), 0))
        visited = set()
        visited.add(s)
        m = len(board)
        n = len(board[0])
        while dq:
            lt, point, step = dq.popleft()
            x, y = point // n, point % n
            if lt == "123450":
                return step
            for p, q in ((x + 1, y), (x, y + 1), (x - 1, y), (x, y - 1)):
                if m > p >= 0 <= q < n:
                    new_point = p * n + q
                    new_lt = list(lt)
                    new_lt[point], new_lt[new_point] = new_lt[new_point], new_lt[point]
                    s = ''. join(new_lt)
                    if s not in visited:
                        visited.add(s)
                        dq.append((s, new_point, step + 1))
        return -1





if __name__ == "__main__":
    print(Solution().slidingPuzzle([[4, 1, 2], [5, 0, 3]]))
