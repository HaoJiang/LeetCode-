from typing import List


class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        res = []
        if not firstList or not secondList:
            return res

        i = 0
        j = 0
        n = len(firstList)
        m = len(secondList)
        while i < n and j < m:
            if firstList[i][1] < secondList[j][0]:
                i += 1
            elif firstList[i][0] > secondList[j][1]:
                j += 1
            else:
                start = max(firstList[i][0], secondList[j][0])
                end = min(firstList[i][1], secondList[j][1])
                res.append([start, end])
                if end == firstList[i][1] == secondList[j][1]:
                    i += 1
                    j += 1
                elif end == firstList[i][1]:
                    secondList[j][0] = end + 1
                    i += 1
                else:
                    firstList[i][0] = end + 1
                    j += 1
        return res


if __name__ == '__main__':
    print(Solution().intervalIntersection(firstList=[[0, 2], [5, 10], [13, 23], [24, 25]],
                                          secondList=[[1, 5], [8, 12], [15, 24], [25, 26]]))

# Input: firstList = [[0, 2], [5, 10], [13, 23], [24, 25]],
#       secondList = [[1, 5], [8, 12], [15, 24], [25, 26]]
# Output: [[1, 2], [5, 5], [8, 10], [15, 23], [24,``` 24], [25, 25]]
