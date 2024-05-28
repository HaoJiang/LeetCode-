# Given an array of n positive integers and a positive integer s, find the minimal length of a contiguous subarray of which the sum ≥ s. If there isn't one, return 0 instead.
# #
# # Example:
# #
# # Input: s = 7, nums = [2,3,1,2,4,3]
# # Output: 2
# # Explanation: the subarray [4,3] has the minimal length under the problem constraint.

class Solution(object):
    def minSubArrayLen(self, s, nums):
        self.int_ = """
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        res = 0
        count = 0
        j = 0
        for i in range(len(nums)):
            res += nums[i]
            if res >= s:
                while j < i and res - nums[j] >= s:
                    res -= nums[j]
                    j += 1
                count = min(count, i - j + 1) if count else i - j + 1

        return count


nums = [2, 3, 1, 2, 4, 3]
s = 7
print(Solution().minSubArrayLen(s, nums))
