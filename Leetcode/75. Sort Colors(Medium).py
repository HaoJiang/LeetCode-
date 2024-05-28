from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        pos = 0
        i = 0
        j = n - 1
        while i <= j:
            if nums[i] == 0:
                nums[i], nums[pos] = nums[pos], nums[i]
                pos += 1
            elif nums[i] == 2:
                while j > i and nums[j] == 2:
                    j -= 1
                if j == i:
                    return nums
                nums[i], nums[j] = nums[j], nums[i]
                if not nums[i]:
                    nums[i], nums[pos] = nums[pos], nums[i]
                    pos += 1
                j -= 1
            i += 1
        return nums

if __name__ == '__main__':
    print(Solution().sortColors( [2,0,2,1,1,0]))



