from typing import List


class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        map = {0: -1}
        count = 0
        maxlen = 0
        for idx, val in enumerate(nums):
            if val:
                count += 1
            else:
                count -= 1
            if count in map:
                maxlen = max(maxlen, idx - map[count])
            else:
                map[count] = idx
        return maxlen


if __name__ == '__main__':
    print(Solution().findMaxLength(([0, 1, 0, 1, 1, 1, 1, 0, 1, 1, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0])))
