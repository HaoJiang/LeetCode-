from typing import List


class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:

        map = {0: -1}
        prefix = 0
        for idx, val in enumerate(nums):
            if k:
                prefix = (prefix + val) % k
            else:
                prefix += val
            if prefix in map:
                if idx - map[prefix] >= 2:
                    return True
            else:
                map[prefix] = idx

        return False


if __name__ == '__main__':
    print(Solution().checkSubarraySum([0, 1, 0], 0))
