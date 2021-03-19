from typing import List


class Solution:
    def findRightInterval(self, intervals: List[List[int]]) -> List[int]:
        from bisect import bisect_left
        ints = sorted([[j, k, i] for i, [j, k] in enumerate(intervals)])
        begs = [i for i, _, _ in ints]
        out = [-1] * len(begs)
        for i, j, k in ints:
            t = bisect_left(begs, j)
            if t < len(begs):
                out[k] = ints[t][2]
        return out


if __name__ == "__main__":
    print(Solution().findRightInterval(intervals = [[3,4],[2,3],[1,2]]))
