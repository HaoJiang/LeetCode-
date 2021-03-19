class Solution(object):
    def shortestPathAllKeys(self, grid):
        """
        :type grid: List[str]
        :rtype: int
        """
        from collections import deque
        n, m = len(grid), len(grid[0])
        numOfKeys = 0
        direc = [[0, 1], [0, -1], [1, 0], [-1, 0]]
        visited = set()

        for i in range(n):
            for j in range(m):
                if grid[i][j] == '@':
                    starti = i
                    startj = j
                elif grid[i][j] in "abcdef":
                    numOfKeys += 1

        deque = deque()
        deque.append([starti, startj, 0, ".@abcdef", 0])

        while deque:
            i, j, steps, keys, collectedKeys = deque.popleft()

            if grid[i][j] in "abcdef" and grid[i][j].upper() not in keys:
                keys += grid[i][j].upper()
                collectedKeys += 1

            if collectedKeys == numOfKeys:
                return steps

            for x, y in direc:
                ni = i + x
                nj = j + y
                if 0 <= ni < n and 0 <= nj < m and grid[ni][nj] in keys:
                    if (ni, nj, keys) not in visited:
                        visited.add((ni, nj, keys))
                        deque.append([ni, nj, steps + 1, keys, collectedKeys])

        return -1


if __name__ == "__main__":
    print(Solution().shortestPathAllKeys(
        [['@', '.', '.', '.', 'a'],
         ['.', '#', '#', '#', 'A'],
         ['b', '.', 'B', 'C', 'c']]))
