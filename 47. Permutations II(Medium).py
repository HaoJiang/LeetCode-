# Given a collection of numbers that might contain duplicates, return all possible unique permutations.
#
# Example:
#
# Input: [1,1,2]
# Output:
# [
#   [1,1,2],
#   [1,2,1],
#   [2,1,1]
# ]

class Solution(object):
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        if not nums:
            return []
        nums.sort()
        res = []

        def dfs(nums, path=[]):
            if not nums:
                res.append(path)
            for i in range(len(nums)):
                if i > 0 and nums[i] == nums[i - 1]:
                    continue
                else:
                    dfs(nums[:i] + nums[i + 1:], path + [nums[i]])

        # def dfs2(index=0):
        #     if index == len(nums):
        #         res.append(nums[:])
        #     for i in range(index, len(nums)):
        #         if i > 0 and nums[i] == nums[i - 1]:
        #             continue
        #         else:
        #             nums[index], nums[i] = nums[i], nums[index]
        #             dfs2(index + 1)
        #             nums[index], nums[i] = nums[i], nums[index]
        #
        dfs(nums)
        # dfs2()
        return res

    def permuteUnique2(self, nums):
        ans = [[]]
        for n in nums:
            new_ans = []
            for l in ans:
                for i in range(len(l) + 1):
                    new_ans.append(l[:i] + [n] + l[i:])
                    if i < len(l) and l[i] == n:
                        break  # handles duplication
            ans = new_ans
        return ans


nums = [1, 3, 1]
print(Solution().permuteUnique2(nums))
