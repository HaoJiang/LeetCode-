from typing import List


class Solution:
    def canChoose(self, groups: List[List[int]], nums: List[int]) -> bool:

        i = 0
        j = 0
        x = 0
        while x < len(nums):
            if groups[i][j] == nums[x]:
                j += 1
                if j == len(groups[i]):
                    i += 1
                    j = 0
            else:
                x -= j
                j = 0
            x += 1
            if i == len(groups):
                return True
        return False


if __name__ == '__main__':
    print(Solution().canChoose([[21, 22, 21, 22, 21, 30]],
                               [21, 22, 21, 22, 21, 22, 21, 30]))
