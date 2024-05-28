from typing import List


class Solution:
    def check(self, nums: List[int]) -> bool:
        for a, b in zip(nums, nums[1:] + nums[:1]):
            print(a,b)

        # left = 1
        # right = len(nums)
        #
        # pos = nums[0]
        # while left < right:
        #     if nums[left] >= nums[left - 1]:
        #         left += 1
        #     else:
        #         left += 1
        #         while left < right:
        #             if pos >= nums[left] >= nums[left - 1]:
        #                 left += 1
        #             else:
        #                 return False
        # return True


if __name__ == '__main__':
    print(Solution().check(  [3,4,5,1,2]))
