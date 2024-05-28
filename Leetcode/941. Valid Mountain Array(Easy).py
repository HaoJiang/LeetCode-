from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        i = 1
        j = len(arr)

        while i < j and arr[i] > arr[i - 1]:
            i += 1

        if i == j or i == 1:
            return False
        while i < j and arr[i] < arr[i - 1]:
            i += 1

        return i == j


if __name__ == "__main__":
    print(Solution().validMountainArray(arr=[2, 1]))
