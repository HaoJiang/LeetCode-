# Given an integer array with all positive numbers and no duplicates, find the number of possible combinations that add up to a positive integer target.
#
# Example:
#
# nums = [1, 2, 3,]
# target = 4
#
# The possible combination ways are:
# (1, 1, 1, 1)
# (1, 1, 2)
# (1, 2, 1)
# (1, 3)
# (2, 1, 1)
# (2, 2)
# (3, 1)
#
# Note that different sequences are counted as different combinations.
#
# Therefore the output is 7.
#
# Follow up:
# What if negative numbers are allowed in the given array?
# How does it change the problem?
# What limitation we need to add to the question to allow negative numbers?
#
# Credits:
# Special thanks to @pbrother for adding this problem and creating all test cases.

## backtracking TLE

# class Solution(object):
#     def combinationSum4(self, nums, target):
#         """
#         :type nums: List[int]
#         :type target: int
#         :rtype: int
#         """
#
#         if not nums:
#             return []
#         nums.sort()
#         res = []
#
#         def dfs(path=[], total=target):
#             if not total:
#                 res.append(path)
#                 return
#             if total < 0:
#                 return
#             for num in nums:
#                 if num > total:
#                     break
#                 dfs(path + [num], total - num)
#
#         dfs()
#         return res
#
#
# nums = [1, 2, 3]
# target = 4
# print(Solution().combinationSum4(nums, target))

## using memo


class Solution(object):

    def comb_dp(self, nums, target):
        if not nums:
            return
        nums.sort()

        dp = [1] + [0] * target

        for i in range(1, target + 1):
            for num in nums:
                if i >= num:

                    dp[i] += dp[i - num]
                    print(dp)
        print(dp)
        return dp[target]

    def combinationSum4(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        memo = {}
        nums.sort()

        def dfs(index=0, total=target):
            if not total:
                return 1
            if total in memo:
                return memo[total]

            res = 0
            for i in range(index, len(nums)):
                if nums[i] > total:
                    break
                res += dfs(index, total - nums[i])
            memo[total] = res

            return res

        return dfs()


nums = [1, 2, 3]
target = 4
print(Solution().comb_dp(nums, target))
