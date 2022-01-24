from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if not n:
            return

        for i in range(n):
            nums1[i + m] = nums2[i]
            for j in range(m + i, 0, -1):
                if nums1[j] < nums1[j - 1]:
                    nums1[j], nums1[j - 1] = nums1[j - 1], nums1[j]
                else:
                    break

    def merge1(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """

        # we use 3 point control the line
        if not n:
            return

        while n and m:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[m + n - 1] = nums1[m - 1]
                m -= 1
            else:
                nums1[m + n - 1] = nums2[n - 1]
                n -= 1
        if n:
            nums1[:n] = nums2[:n]


if __name__ == "__main__":
    print(Solution().merge1(nums1=[1, 2, 3, 0, 0, 0], m=3, nums2=[2, 5, 6], n=3))
