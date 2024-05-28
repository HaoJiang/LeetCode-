from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        nums.sort()

        k = len(nums) // 2

        perv = nums[:k][::-1]
        nxt = nums[k:][::-1]
        print(1)


if __name__ == '__main__':
    print(Solution().wiggleSort([1, 5, 1, 1, 6, 4]))
