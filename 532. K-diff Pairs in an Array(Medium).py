from typing import List


class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        from collections import Counter

        ct = Counter(nums)
        res = 0
        if k == 0:
            for val in ct.values():
                res += val > 1
        else:
            for val in ct:
                res += val + k in ct
        return res
