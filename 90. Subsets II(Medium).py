# Given a collection of integers that might contain duplicates, nums, return all possible subsets (the power set).
#
# Note: The solution set must not contain duplicate subsets.
#
# Example:
#
# Input: [1,2,2]
# Output:
# [
#   [2],
#   [1],
#   [1,2,2],
#   [2,2],
#   [1,2],
#   []
# ]

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        # same like subset
        # interation

        if not nums:
            return [[]]
        res = [[]]
        for i in nums:
            res += [j + [i] for j in res if j + [i] not in res]
        return res

    def subsetsWithDup2(self, nums):
        ### using backtracking

        if not nums:
            return [[]]
        res = []
        nums.sort()
        # self.dfs(nums, 0, [], res)
        self.dfs3(nums, 0, [], res)
        return res

    def subsetsWithDup3(self, nums):

        if not nums:
            return [[]]

        from collections import Counter
        res = [[]]
        nums = Counter(nums)

        for i, v in nums.items():
            for j in range(len(res)):
                res += [res[j] + [i] * (k + 1) for k in range(v)]
        return res

    def dfs(self, nums, index, path, res):
        if path not in res:
            res.append(path)
        for i in range(index, len(nums)):
            self.dfs(nums, i + 1, path + [nums[i]], res)

    def dfs2(self, nums, index, path, res):
        if path not in res:
            res.append(path[:])
        for i in range(index, len(nums)):
            path.append(nums[i])
            # print(path)
            self.dfs2(nums, i + 1, path, res)
            path.pop()

    def dfs3(self, nums, index, path, res):
        res.append(path)
        for i in range(index, len(nums)):
            if i > index and nums[i] == nums[i - 1]:
                continue
            self.dfs3(nums, i + 1, path + [nums[i]], res)


nums = [1, 2, 2, 2]
print(Solution().subsetsWithDup2(nums))
