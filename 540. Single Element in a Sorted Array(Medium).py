from typing import List


class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            nxt = mid - 1 if mid % 2 else mid + 1
            if nums[mid] == nums[nxt]:
                left = mid + 1
            else:
                right = mid
        return left


if __name__ == "__main__":
    print(Solution().singleNonDuplicate(nums=[1, 1, 2, 3, 3, 4, 4, 8, 8]))
