# Example 1:
#
# Input: piles = [3,6,7,11], H = 8
# Output: 4
#
# Example 2:
#
# Input: piles = [30,11,23,4,20], H = 5
# Output: 30
# Example 3:
#
# Input: piles = [30,11,23,4,20], H = 6
# Output: 23

from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], H: int) -> int:
        left = 0
        right = max(piles)

        def isPossible(k):
            return sum(((pile - 1) // k + 1 for pile in piles)) <= H
        while left < right:
            mid = (left + right) // 2

            if isPossible(mid):
                right = mid
            else:
                left = mid + 1

        return left


