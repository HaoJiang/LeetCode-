from typing import List


class Solution:
    def search(self, nums: List[int], target: int) -> int:

        left = 0
        right = len(nums) - 1

        while left < right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                if nums[mid] > nums[-1]:
                    left = mid + 1
                else:
                    if target <= nums[-1]:
                        left = mid + 1
                    else:
                        right = mid
            else:
                if nums[mid] <= nums[-1]:
                    right = mid
                else:
                    if target <= nums[-1]:
                        left = mid + 1
                    else:
                        right = mid

        if nums[left] != target:
            return -1
        return left


if __name__ == "__main__":
    print(Solution().search(nums=[1], target=0))
