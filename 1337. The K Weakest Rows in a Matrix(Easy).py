from typing import List


class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        import bisect
        ans = []
        for i, val in enumerate(mat):
            total = (sum(val), i)
            if len(ans) == k and total[0] > ans[-1][0]:
                continue
            bisect.insort_right(ans, total)
            if len(ans) > k:
                ans.pop()
        return [i[1] for i in ans]


if __name__ == '__main__':
    print(Solution().kWeakestRows([[1, 1, 0, 0, 0],
                                   [1, 1, 1, 1, 0],
                                   [1, 0, 0, 0, 0],
                                   [1, 1, 0, 0, 0],
                                   [1, 1, 1, 1, 1]], 3))
