from typing import List

class Solution:
    def nearestValidPoint(self, x: int, y: int, points: List[List[int]]) -> int:

        min_dis = float('inf')
        ans = -1
        for idx, val in enumerate(points):
            if (val[0] == x or val[1] == y):
                t = abs(x - val[0]) + abs(y - val[1])
                if t < min_dis:
                    ans = idx
                    min_dis = t
        return ans



if __name__ == '__main__':
    print(Solution().nearestValidPoint(3,
4,
[[1,2],[3,1],[2,4],[2,3],[4,4]]))