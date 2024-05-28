from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> bool:

        while len(nums) > 1 and nums[0] == nums[-1]:
            nums.pop()
        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) // 2
            if nums[mid] == target:
                return True

            elif nums[mid] >= nums[0]:
                if nums[mid] > target >= nums[0]:
                    right = mid
                else:
                    left = mid + 1
            else:
                if nums[mid] < target <= nums[-1]:
                    left = mid + 1
                else:
                    right = mid

        return False

        # left = 0
        # right = len(nums) - 1
        #
        # while left <= right and nums[left] == nums[right]:
        #     if nums[left] == target:
        #         return True
        #     left += 1
        #     right -= 1
        #
        # if left > right:
        #     return False
        #
        # low = left
        # high = right
        #
        # while low < high:
        #     mid = (low + high) // 2
        #
        #     if nums[mid] == target:
        #         return True
        #     elif nums[mid] > target:
        #         if target > nums[right]:
        #             high = mid
        #         else:
        #             if nums[mid] > nums[right]:
        #                 low = mid + 1
        #             else:
        #                 high = mid
        #     else:
        #         if target <= nums[right]:
        #             low = mid + 1
        #         else:
        #             if nums[mid] > nums[right]:
        #                 low = mid + 1
        #             else:
        #                 high = mid
        #
        # if nums[low] != target:
        #     return False
        # return True


if __name__ == "__main__":
    print(Solution().search(
        [2, 2, 2, 0, 2, 2, 2],
        0))
