from typing import List


class Solution:
    def countPairs(self, deliciousness: List[int]) -> int:
        odd = 0
        even = 0

        for i in deliciousness:
            if i % 2:
                odd += 1
            else:
                even += 1

        return odd // 2 + even 