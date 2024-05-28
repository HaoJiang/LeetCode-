class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        :type tiles: str
        :rtype: int
        """
        if not tiles:
            return []

        res = []

        def dfs(nums=sorted(tiles), path=''):
            if path:
                res.append(path)
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                else:
                    dfs(nums[:i] + nums[i + 1:], path + nums[i])
            return res

        return dfs()

        # res = set()

        # def dfs(path, t):
        #     if path not in res:
        #         if path:
        #             res.add(path)
        #         for i in range(len(t)):
        #             dfs(path + t[i], t[:i] + t[i + 1:])
        #
        # dfs('', tiles)
        # return len(res)

    from collections import defaultdict

    # class Solution:
    #     def numTilePossibilities(self, tiles: str) -> int:
    #         counts = defaultdict(int)
    #         for t in tiles:
    #             counts[t] += 1
    #         return self.dfs(counts)
    #
    #     def dfs(self, counts: dict) -> int:
    #         sum = 0
    #         for c in counts:
    #             if counts[c] > 0:
    #                 counts[c] -= 1
    #                 sum += 1
    #                 sum += self.dfs(counts)
    #                 counts[c] += 1  # backtrack :)
    #         return sum


print(Solution().numTilePossibilities('AAB'))
