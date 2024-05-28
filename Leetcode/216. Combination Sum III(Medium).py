# Find all possible combinations of k numbers that add up to a number n, given that only numbers from 1 to 9 can be used and each combination should be a unique set of numbers.
#
# Note:
#
# All numbers will be positive integers.
# The solution set must not contain duplicate combinations.
# Example 1:
#
# Input: k = 3, n = 7
# Output: [[1,2,4]]
# Example 2:
#
# Input: k = 3, n = 9
# Output: [[1,2,6], [1,3,5], [2,3,4]]

class Solution(object):
    def combinationSum3(self, k, n):
        """
        :type k: int
        :type n: int
        :rtype: List[List[int]]
        """
        res = []

        def dfs(index=1, path=[], total=n, count=k):
            if not count and not total:
                res.append(path)
                return
            if k < 0:
                return
            if total < 0:
                return

            for i in range(index, 10):
                dfs(i + 1, path + [i], total - i, count - 1)

        dfs()
        return res


print(Solution().combinationSum3(3, 9))
