from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        pos = 0

        for i in nums:
            if i:
                nums[pos] = i
                pos += 1

        for i in range(pos, len(nums)):
            nums[i] = 0
        return nums





        # k = 0
        # for i in range(len(nums) - 1, -1, -1):
        #     if not nums[i]:
        #         j = i
        #         while j < len(nums) - k - 1:
        #             nums[j], nums[j + 1] = nums[j + 1], nums[j]
        #             j += 1
        #         k += 1
        # return nums


if __name__ == '__main__':
    print(Solution().moveZeroes([0, 1, 1, 3, 234, 0, 234, 324, 23, 0, 0, 3, 12]))
