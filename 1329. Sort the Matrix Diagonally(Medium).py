from typing import List


class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        from collections import defaultdict
        mp = defaultdict(list)
        m = len(mat)
        n = len(mat)
        for i in range(m):
            for j in range(n):
                mp[i - j].append(mat[i][j])

        for i in mp:
            mp[i].sort(reverse=True)

        for i in range(m):
            for j in range(n):
                mat[i][j] = mp[i - j].pop()

        return mat


if __name__ == "__main__":
    print(Solution().diagonalSort(mat=[[3, 3, 1, 1],
                                       [2, 2, 1, 2],
                                       [1, 1, 1, 2]]))
