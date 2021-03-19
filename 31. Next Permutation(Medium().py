from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]):
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)

        for i in range(n - 1, 0, -1):
            if nums[i - 1] < nums[i]:
                pivot = i - 1
                nxt = i
                while nxt < n and nums[nxt] > nums[pivot]:
                    nxt += 1
                nums[pivot], nums[nxt-1] = nums[nxt-1], nums[pivot]
                start = i
                end = n - 1
                while start < end:
                    nums[start], nums[end] = nums[end], nums[start]
                    start += 1
                    end -= 1
                return nums
        nums.reverse()
        return nums


if __name__ == "__main__":
    print(Solution().nextPermutation(nums=[1, 5, 1]))
