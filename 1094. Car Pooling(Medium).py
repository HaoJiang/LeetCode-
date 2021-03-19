from typing import List


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:

        from collections import defaultdict
        cache = defaultdict(int)
        for i, j, k in trips:
            cache[j] += i
            cache[k] -= i

        presum = 0
        for i in sorted(cache):
            presum += cache[i]
            if presum > capacity:
                return False
        return not presum


if __name__ == '__main__':
    print(Solution().carPooling(trips=[[2, 1, 5], [3, 3, 7]], capacity=5))
