from typing import List


class Solution:
    def leastBricks(self, wall: List[List[int]]) -> int:
        from collections import defaultdict
        # count = len(wall)
        # map = defaultdict(int)
        # height = len(wall)
        # for i in range(len(wall)):
        #     for j in range(len(wall[i]) -1):
        #         if j > 0:
        #             wall[i][j] += wall[i][j - 1]
        #         if wall[i][j] in map:
        #             map[wall[i][j]] -= 1
        #         else:
        #             map[wall[i][j]] = height - 1
        #         count = min(count, map[wall[i][j]])
        # return count

        height = len(wall)
        counts = defaultdict(lambda: height)
        for row in wall:
            _sum = 0
            for r in row[:-1]:
                _sum += r
                counts[_sum] -= 1

        if len(counts.values()):
            return min(counts.values())
        else:
            return height


if __name__ == '__main__':
    print(Solution().leastBricks([[1, 2, 2, 1],
                                  [3, 1, 2],
                                  [1, 3, 2],
                                  [2, 4],
                                  [3, 1, 2],
                                  [1, 3, 1, 1]]))
