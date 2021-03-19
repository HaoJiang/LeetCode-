# Given a collection of distinct integers, return all possible permutations.
#
# Example:
#
# Input: [1,2,3]
# Output:
# [
#   [1,2,3],
#   [1,3,2],
#   [2,1,3],
#   [2,3,1],
#   [3,1,2],
#   [3,2,1]
# ]


class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        res = []

        def dfs(nums=nums, path=[]):
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                dfs(nums[:i] + nums[i + 1:], path + [nums[i]])

        def dfs2(index=0):
            if index == len(nums):
                res.append(nums[:])
            for i in range(index, len(nums)):
                nums[index], nums[i] = nums[i], nums[index]
                dfs2(index + 1)
                # backtack
                nums[index], nums[i] = nums[i], nums[index]

        # dfs(nums, [])
        dfs()
        return res


nums = [1, 2, 3]
print(Solution().permute(nums))
