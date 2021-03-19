# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.
#
# Example 1:
#
# Input:nums = [1,1,1], k = 2
# Output: 2

class Solution(object):
    def subarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """

        from collections import defaultdict

        dt = defaultdict(int)
        dt[0] = 1
        res = loc = 0
        for i in nums:
            loc += i
            res += dt.get(loc - k, 0)
            dt[loc] += 1
        return res


print(Solution().subarraySum([1], 0))
