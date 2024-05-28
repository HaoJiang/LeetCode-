# Given a binary array nums, you should delete one element from it.
#
# Return the size of the longest non-empty subarray containing only 1's in the resulting array.
#
# Return 0 if there is no such subarray.
#
# Example 1:
#
# Input: nums = [1,1,0,1]
# Output: 3
# Explanation: After deleting the number in position 2, [1,1,1] contains 3 numbers with value of 1's.
#
# Input: nums = [0,1,1,1,0,1,1,0,1]
# Output: 5
# Explanation: After deleting the number in position 4, [0,1,1,1,1,1,0,1] longest subarray with value of 1's is [1,1,1,1,1].
#
# Input: nums = [1, 1, 1]
# Output: 2
#
# Input: nums = [1,1,0,0,1,1,1,0,1]
# Output: 4
#
# Input: nums = [0,0,0]
# Output: 0
#
# 1 <= nums.length <= 10^5
# nums[i] is either 0 or 1.


class Solution(object):
    def longestSubarray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        k = 1
        j = 0

        for i in range(len(nums)):
            k -= 1 - nums[i]
            if k < 0:
                k -= nums[j] - 1
                j += 1
        return i - j


nums = [1, 1, 0, 0, 1, 1, 1, 0, 1]
print(Solution().longestSubarray(nums))
