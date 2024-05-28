# Given an integer array of size n, find all elements that appear more than ⌊ n/3 ⌋ times.
#
# Note: The algorithm should run in linear time and in O(1) space.
#
# Example 1:
#
# Input: [3,2,3]
# Output: [3]
# Example 2:
#
# Input: [1,1,1,3,3,2,2,2]
# Output: [1,2]
from typing import List


class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:

        n = len(nums)
        if n <= 1:
            return nums

        p1 = None
        p2 = None
        p1_c = 0
        p2_c = 0
        for i in nums:
            if i == p1:
                p1_c += 1
            elif i == p2:
                p2_c += 1
            elif not p1_c:
                p1 = i
                p1_c += 1
            elif not p2_c:
                p2 = i
                p2_c += 1
            else:
                p1_c -= 1
                p2_c -= 1

        return [i for i in (p1, p2) if nums.count(i) > n // 3]

if __name__ == '__main__':
    print(Solution().majorityElement(nums=[4, 2, 1, 1]))
