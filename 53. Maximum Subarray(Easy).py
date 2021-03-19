# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
#
# Example:
#
# Input: [-2,1,-3,4,-1,2,1,-5,4],
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.


class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        res = mx = nums[0]

        for i in range(1, len(nums)):
            mx = max(mx + nums[i], nums[i])
            res = max(res, mx)

        return res


    def maxSubArray_1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        for i in range(1, len(nums)):
            if nums[i - 1] > 0:
                nums[i] += nums[i - 1]
        return max(nums)


print(Solution().maxSubArray_1([-2, 1, -3, 4, -1, 2, 1, -5, 4]))
