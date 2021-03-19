from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:

        if not nums:
            return 1
        n = len(nums)
        for i in range(n):
            if nums[i] <= 0 or nums[i] > n:
                nums[i] = n + 1

        for i in range(n):
            if abs(nums[i]) > n:
                continue
            k = abs(nums[i])
            nums[k - 1] = -nums[k - 1]

        for i in range(n):
            if nums[i] > 0:
                return i + 1


if __name__ == "__main__":
    print(Solution().firstMissingPositive(nums=[3, 4, -1, 1]))
