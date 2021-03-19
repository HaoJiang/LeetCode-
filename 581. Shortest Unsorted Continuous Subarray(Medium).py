from typing import List


class Solution:
    def findUnsortedSubarray(self, nums: List[int]) -> int:

        small = float('inf')
        large = float('-inf')

        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                small = min(nums[i], small)
        else:
            if small == float('inf'):
                return 0
        for i in range(len(nums) - 1, 0, -1):
            if nums[i - 1] > nums[i]:
                large = max(nums[i - 1], large)

        for i in range(len(nums)):
            if nums[i] > small:
                small = i
                break
        for i in range(len(nums) - 1, -1, -1):
            if nums[i] < large:
                large = i
                break

        return large - small + 1
    # stack = []
    # small = len(nums)
    # for i in range(len(nums)):
    #     while stack and nums[stack[-1]] > nums[i]:
    #         small = min(small, stack.pop())
    #     stack.append(i)
    # if small == len(nums):
    #     return 0
    # stack.clear()
    # large = -1
    # for i in range(len(nums)-1, - 1, -1):
    #     while stack and nums[stack[-1]] < nums[i]:
    #         large = max(large, stack.pop())
    #     stack.append(i)
    #
    # return large - small + 1


if __name__ == '__main__':
    print(Solution().findUnsortedSubarray([2, 6, 4, 8, 10, 9, 15]))
