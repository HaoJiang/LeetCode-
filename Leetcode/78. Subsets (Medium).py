# Given a set of distinct integers, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
# Input: nums = [1,2,3]
# Output:
# [
#   [3],
#   [1],
#   [2],
#   [1,2,3],
#   [1,3],
#   [2,3],
#   [1,2],
#   []
# ]


class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        # interation
        # first create a empty list when you merge must be same datatype  list
        # res = [[]]
        # for i in nums:
        #     res += [j + [i] for j in res]
        # return res

        # dfs (backtracking)
        # first i need create golbal list to save the res  then create recursive fun back track res
        def dfs(index=0, path=[]):
            res.append(path)
            for i in range(index, len(nums)):
                dfs(i + 1, path + [nums[i]])
        res = []
        # subset if empty list should return [[]] because subset included empty list
        if not nums:
            return [[]]

        dfs()
        return res

test = [1, 2, 3]
print(Solution().subsets(test))
