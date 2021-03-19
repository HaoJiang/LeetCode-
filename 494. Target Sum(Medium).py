# You are given a list of non-negative integers, a1, a2, ..., an, and a target, S. Now you have 2 symbols + and -. For each integer, you should choose one from + and - as its new symbol.
#
# Find out how many ways to assign symbols to make sum of integers equal to target S.
#
# Example 1:
# Input: nums is [1, 1, 1, 1, 1], S is 3.
# Output: 5
# Explanation:
#
# -1+1+1+1+1 = 3
# +1-1+1+1+1 = 3
# +1+1-1+1+1 = 3
# +1+1+1-1+1 = 3
# +1+1+1+1-1 = 3
#
# There are 5 ways to assign symbols to make the sum of nums be target 3.
# Note:
# The length of the given array is positive and will not exceed 20.
# The sum of elements in the given array will not exceed 1000.
# Your output answer is guaranteed to be fitted in a 32-bit integer.

class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        :type nums: List[int]
        :type S: int
        :rtype: int
        """
        res = []
        k = len(nums)

        def dfs(index=0, path=[], count=k):
            if not count and sum(path) == S:
                res.append(path)
                return
            elif not count:
                return

            for i in range(index, k):
                dfs(i + 1, path + [nums[i]], count - 1) or dfs(i + 1, path + [-nums[i]], count - 1)

        dfs()
        return res


print(Solution().findTargetSumWays([1, 1, 1, 1, 1], 3))
