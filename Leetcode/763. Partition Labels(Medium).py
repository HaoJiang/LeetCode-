from typing import List


class Solution:
    def partitionLabels(self, S: str) -> List[int]:
        map = {}

        for idx, val in enumerate(S):
            if val in map:
                map[val][-1] = idx
            else:
                map[val] = [idx, idx]

        intervals = list(map.values())
        start = intervals[0][0]
        end = intervals[0][1]
        res = []
        for i in range(1, len(intervals)):
            if intervals[i][0] > end:
                res.append(end - start + 1)
                start = intervals[i][0]
                end = intervals[i][1]
            else:
                end = max(end, intervals[i][1])
        res.append(end - start + 1)
        return res


if __name__ == '__main__':
    print(Solution().partitionLabels(S="ababcbacadefegdehijhklij"))
