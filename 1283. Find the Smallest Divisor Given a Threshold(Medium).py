from typing import List


class Solution:
    def ftsdgat(self, nums: List[List[int]], threshold: int) -> int:

        def ispossible(k, arr):
            return sum([(i - 1) // k + 1 for i in arr]) <= threshold

        left = 1
        right = max(nums)

        while left < right:
            mid = (left + right) // 2
            if ispossible(mid, nums):
                right = mid
            else:
                left = mid + 1
        return left


if __name__ == "__main__":
    print(Solution().ftsdgat(nums=[1, 2, 5, 9], threshold=6))
