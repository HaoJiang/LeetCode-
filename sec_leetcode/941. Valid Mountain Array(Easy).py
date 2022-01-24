from typing import List


class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:

        i = 0
        j = n = len(arr) - 1

        while i < n and arr[i] < arr[i + 1]:
            i += 1
        if not i:
            return False
        while j > 0 and arr[j] < arr[j - 1]:
            j -= 1
        if j == n or i != j:
            return False
        return True


if __name__ == '__main__':
    print(Solution().validMountainArray([9, 8, 7, 6, 5, 4, 3, 2, 1, 0]))
