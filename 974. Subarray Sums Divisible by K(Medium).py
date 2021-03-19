from typing import List


class Solution:
    def subarraysDivByK(self, A: List[int], K: int) -> int:
        from collections import defaultdict
        map = defaultdict(int)
        map[0] = 1
        prefix = 0
        res = 0
        for i in A:
            prefix += i
            if prefix % K in map:
                res += map[prefix % K]
            map[prefix % K] += 1
        return res


if __name__ == '__main__':
    print(Solution().subarraysDivByK(
        [4, 5, 0, -2, -3, 1], 5))
