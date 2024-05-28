from typing import List


class Solution:
    def subarraysWithKDistinct(self, A: List[int], K: int) -> int:
        def cal_atmostK(k):
            from collections import defaultdict
            cache = defaultdict(int)
            left = 0
            res = 0
            for right, val in enumerate(A):
                cache[val] += 1
                while len(cache) > k:
                    cache[A[left]] -= 1
                    if not cache[A[left]]:
                        del cache[A[left]]
                    left += 1
                res += (right - left + 1)
            return res

        return cal_atmostK(K) - cal_atmostK(K - 1)


if __name__ == '__main__':
    print(Solution().subarraysWithKDistinct([1, 2, 1, 2, 3], 2))
