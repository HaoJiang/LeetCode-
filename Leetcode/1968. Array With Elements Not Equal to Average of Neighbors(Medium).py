from typing import List


class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        ### we need sort arr fist let,  because the arr is distinct
        ### so the arr is stiky asc  so we just swap the neihbor element then the neihbor will not get equal
        ###
        nums.sort()
        n = len(nums)
        i = 0
        while i + 1 < n:
            nums[i], nums[i + 1] = nums[i + 1], nums[i]
            i += 2
        return nums


if __name__ == '__main__':
    print(Solution().rearrangeArray([6,2,0,9,7]))
