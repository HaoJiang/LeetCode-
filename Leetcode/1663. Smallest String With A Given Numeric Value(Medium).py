from typing import List


class Solution:
    def getSmallestString(self, n: int, k: int) -> str:
        self.map = {i: chr(i + 96) for i in range(1, 27)}

        z, r = divmod(k - n, 25)

        return ('' if z == n else 'a' * (n - z - 1) + chr(ord('a') + r)) + 'z' * z
        # self.map = {i: chr(i + 96) for i in range(1, 27)}
        # from functools import lru_cache
        # @lru_cache(maxsize=None)
        # def dfs(n, k, path):
        #     if not n:
        #         return path
        #     if k - n + 1 >= 26:
        #         return dfs(n - 1, k - 26, 'z' + path)
        #     return dfs(0, k - n - 1, (n - 1) * 'a' + self.map[k - n + 1] + path)
        #
        # return dfs(n, k, '')


if __name__ == '__main__':
    print(Solution().getSmallestString(27, 27))
