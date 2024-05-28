# Given an integer array nums, return true if there exists a triple of indices (i, j, k)
# such that i < j < k and nums[i] < nums[j] < nums[k].
# If no such indices exists, return false
#
#
# Example 1:
#
# Input: nums = [1,2,3,4,5]
# Output: true
# Explanation: Any triplet where i < j < k is valid.
#
# Example 2:
#
# Input: nums = [5,4,3,2,1]
# Output: false
# Explanation: No triplet exists.
# Example 3:
#
# Input: nums = [2,1,5,0,4,6]
# Output: true
# Explanation: The triplet (3, 4, 5) is valid because nums[3] == 0 < nums[4] == 4 < nums[5] == 6.

from typing import List


class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:

        ### solutions  is greedy    mean we maitain two  number
        # two max    and update two min numbver  n <= min 1   n <= min 2
        # this way can update two min  numnber
        #  the idea    1 6  9    mean   1- 6 any number   6    to 9  return True
        r1, r2 = float('inf'), float('inf')
        for n in nums:
            if n <= r1:
                r1 = n
            elif n <= r2:
                r2 = n
            else:
                return True
        return False


print(Solution().increasingTriplet([2, 1, 5, 0, 6]))
