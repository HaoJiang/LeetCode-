from typing import List


class Solution:
    def canEat(self, candiesCount: List[int], queries: List[List[int]]) -> List[bool]:
        for i in range(1, len(candiesCount)):
            candiesCount[i] += candiesCount[i - 1]

        res = []

        for ftype, enddays, dailyeat in queries:
            left = (enddays + 1) * 1
            right = (enddays + 1) * dailyeat
            pretotalcandys = candiesCount[ftype - 1] if ftype else 0
            totalcandys = candiesCount[ftype]
            if right <= pretotalcandys or left > totalcandys:
                res.append(False)
            else:
                res.append(True)
        return res


if __name__ == '__main__':
    print(Solution().canEat(candiesCount=[5, 2, 6, 4, 1],
                            queries=[[3, 1, 2], [4, 10, 3], [3, 10, 100], [4, 100, 30], [1, 3, 1]]))
