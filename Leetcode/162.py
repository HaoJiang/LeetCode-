from typing import List


class Solution:
    def findPeakElement(self, nums: List[int]) -> int:

        left = 0
        right = len(nums)
        if len(nums) <= 1:
            return 0

        while left < right:
            mid = (left + right) // 2

            if nums[mid] >= nums[mid + 1]:
                right = mid

            else:
                left = mid + 1

        return left


if __name__ == "__main__":
    print(Solution().findPeakElement(nums=[1, 2, 1, 3, 5, 6, 7]))
