from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:

        while len(nums) > 1 and nums[0] == nums[-1]:
            nums.pop()

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            if nums[mid] <= nums[mid + 1]:
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
        # if not nums:
        #     return 0
        #
        # left = 0
        # right = len(nums) - 1
        # while left < right and nums[left] == nums[right]:
        #     left += 1
        #
        # if left > right:
        #     return nums[0]
        # if nums[left] < nums[right]:
        #     return nums[left]
        #
        # low = left
        # high = right
        #
        # while low < high:
        #     mid = (low + high) // 2
        #
        #     if nums[mid] > nums[high]:
        #         low = mid + 1
        #     else:
        #         high = mid
        #
        # return nums[low]

if __name__ == "__main__":
    print(Solution().findMin([1,3,3]))
