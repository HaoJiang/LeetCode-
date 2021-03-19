from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not n:
            return nums1
        for i in nums2:
            j = m
            nums1[j] = i
            while j > 0 and nums1[j] < nums1[j - 1]:
                nums1[j], nums1[j - 1] = nums1[j - 1], nums1[j]
                j -= 1
            m += 1
        return nums1

if __name__=='__main__':

    print(Solution().merge(nums1 = [1,2,3,0,0,0], m = 3, nums2 = [1,5,6], n = 3))




