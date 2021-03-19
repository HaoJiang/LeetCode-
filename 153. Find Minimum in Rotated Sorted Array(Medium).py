from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left = 0
        right = len(nums) - 1
        if not right:
            return nums[right]

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < nums[mid + 1]:
                if nums[0] < nums[-1]:
                    right = mid
                else:
                    if nums[mid] >= nums[0]:
                        left = mid + 1
                    else:
                        right = mid
            else:
                return nums[mid + 1]
        return nums[left]


if __name__ == "__main__":
    print(Solution().findMin([11, 13, 15, 17]))
