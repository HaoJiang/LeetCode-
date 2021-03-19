from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        from collections import defaultdict
        map = defaultdict(list)

        for i, v in enumerate(nums):
            if v in map:
                if i - map[v][-1] == k:
                    return True
            map[v].append(i)
        return False


if __name__ == '__main__':
    print(Solution().containsNearbyDuplicate(nums=[1, 2, 3, 1], k=3))
