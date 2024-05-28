# Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.
#
# Example:
#
# Input: n = 4, k = 2
# Output:
# [
#   [2,4],
#   [3,4],
#   [2,3],
#   [1,2],
#   [1,3],
#   [1,4],
# ]

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        self.res = []

        nums = range(1, n + 1)

        def dfs(idx, path):
            if len(path) == k:
                self.res.append(path)
                return
            for i in range(idx, len(nums)):
                if n - idx + len(path) < k:
                    break
                print(path)
                dfs(i + 1, path + [nums[i]])

        dfs(0, [])

        return self.res


print(Solution().combine(15, 4))
