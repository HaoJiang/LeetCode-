from typing import List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        def reversest(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        n = len(nums)
        k %= n
        reversest(0, n-1)
        reversest(0, k-1)
        reversest(k, n-1)

        return nums

if __name__ == "__main__":
    print(Solution().rotate(nums=[1, 2, 3, 4, 5, 6, 7], k=3))
