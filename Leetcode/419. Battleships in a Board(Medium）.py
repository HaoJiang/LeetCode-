class Solution:
    def countBattleships(self, board: List[List[str]]) -> int:
        # just check the graph how many node not connect

        m = len(board)
        n = len(board[0])

        count = 0
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'X':
                    if (not i or board[i - 1][j] == '.') and (not j or board[i][j - 1] == '.'):
                        count += 1

        return count

#
# [["X",".",".","X"],
#  [".",".",".","X"],
#  [".",".",".","X"]]
