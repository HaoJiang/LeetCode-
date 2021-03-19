from typing import List


class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        nums.sort()

        left = 0
        right = len(nums)

        while left < right:
            mid = (left + right) >> 1
            if nums[mid - 1] != mid:
                right = mid
            else:
                left = mid + 1

        return nums[left - 1]

        # for i in nums:
        #     if nums[abs(i) - 1] < 0:
        #         return abs(i)
        #     nums[abs(i)-1] = -nums[abs(i)-1]


if __name__ == "__main__":
    print(Solution().findDuplicate([7,9,7,4,2,8,7,7,1,5]))
