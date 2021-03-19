from typing import List


class Solution:
    def shortestToChar(self, s: str, c: str) -> List[int]:
        intervals = [float('-inf')]

        for i, v in enumerate(s):
            if v == c:
                intervals.append(i)
        intervals.append(float('inf'))
        res = []
        pos = 0
        for idx, val in enumerate(s):
            res.append(min(idx - intervals[pos], intervals[pos + 1] - idx))
            if idx == intervals[pos + 1]:
                pos += 1
        return res

        # n = len(intervals)
        # if n > 1:
        #     intervals = [intervals[0]] + intervals + [intervals[-1]]
        #     pos = 1
        # else:
        #     intervals += [intervals[0]]
        #     pos = 0
        # res = []
        # for idx, val in enumerate(s):
        #     if idx == intervals[pos]:
        #         res.append(0)
        #         pos += 1
        #     else:
        #         res.append(min(abs(intervals[pos] - idx), abs(intervals[pos - 1] - idx)))
        # return res


if __name__ == '__main__':
    print(Solution().shortestToChar(s="loveleetcode", c="e"))
