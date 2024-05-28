# Given an array of integers nums and an integer k. A subarray is called nice if there are k odd numbers on it.
#
# Return the number of nice sub-arrays.
# Example 1:
#
# Input: nums = [1,1,2,1,1], k = 3
# Output: 2
# Explanation: The only sub-arrays with 3 odd numbers are [1,1,2,1] and [1,2,1,1].
# Example
# 2:
#
# Input: nums = [2, 4, 6], k = 1
# Output: 0
# Explanation: There is no
# odd
# numbers in the
# array.
# Example 3:
#
# Input: nums = [2,2,2,1,2,2,1,2,2,2], k = 2
# Output: 16

class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        from collections import defaultdict

        mp = defaultdict(int)
        mp[0] = 1
        res = presum = 0
        for i in nums:
            if i % 2:
                presum += 1
            res += mp.get(presum - k, 0)
            mp[presum] += 1
        return res


nums = [2, 2, 2, 1, 2, 2, 1, 2, 2, 2]
k = 2
print(Solution().numberOfSubarrays(nums, k))
