from typing import List


class Solution:
    def maxOperations(self, nums: List[int], k: int) -> int:
        from collections import Counter

        ct = Counter(nums)
        ans = 0

        for idx, val in ct.items():
            if k - idx in ct:
                if k - idx == idx:
                    if val > 1:
                        ans += val // 2
                else:
                    ans += min(val, ct[k - idx])
                ct[k - idx] = 0
                ct[idx] = 0
        return ans


if __name__ == '__main__':
    print(Solution().maxOperations([3, 5, 1, 5],
                                   2))
