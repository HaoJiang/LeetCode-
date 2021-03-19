from typing import List
class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:

        left = 0
        right = len(arr)

        while left < right:
            mid = (left + right) // 2
            if arr[mid] > arr[mid + 1]:
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == "__main__":
    print(Solution().peakIndexInMountainArray([24, 69, 100, 99, 79, 78, 67, 36, 26, 19]))
