from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        from collections import defaultdict
        import math
        mp = defaultdict(int)
        n = len(nums)
        for i in range(n):
            for j in range(i + 1, n):
                mp[nums[i] * nums[j]] += 1

        def comb(N, M):
            return math.factorial(N) // (math.factorial(N - M) * math.factorial(M))

        def perm(N):
            return math.factorial(N)

        count = 0
        for v in mp.values():
            if v > 1:
                count += comb(v, 2) * 8

        return count


if __name__ == "__main__":
    print(Solution().tupleSameProduct([2, 3, 4, 6]))
