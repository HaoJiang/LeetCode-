from typing import List

# 2D grid row = total cnt m * n // n  col == m * n % n     we use pointer 0 -> end m * n - 1
# reverse total then reverse 0 -> k -1 then reverse k -> m*n - 1
class Solution:
    def shiftGrid(self, grid: List[List[int]], k: int) -> List[List[int]]:
        m = len(grid)
        n = len(grid[0])
        k %= m * n

        def _reverse2Dgrid(start, end):
            while start < end:
                grid[start // n][start % n], grid[end // n][end % n] = grid[end // n][end % n], grid[start // n][
                    start % n]
                start += 1
                end -= 1

        _reverse2Dgrid(0, m * n - 1)
        _reverse2Dgrid(0, k - 1)
        _reverse2Dgrid(k, m * n - 1)

        return grid


if __name__ == "__main__":
    print(Solution().shiftGrid(
        grid = [[3,8,1,9],[19,7,2,5],[4,6,11,10],[12,0,21,13]], k = 4))
