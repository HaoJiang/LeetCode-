from typing import List


class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])

        def reversegd(start, end):
            while start < end:
                s_i = start // n
                s_j = start % n
                e_i = end // n
                e_j = end % n
                grid[s_i][s_j], grid[e_i][e_j] = grid[e_i][e_j], grid[s_i][s_j]
                start += 1
                end -= 1

        k %= (m * n)
        reversegd(0, m * n - 1)
        reversegd(0, k - 1)
        reversegd(k, m * n - 1)

        return grid


if __name__ == '__main__':
    print(Solution().shiftGrid(grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4))
