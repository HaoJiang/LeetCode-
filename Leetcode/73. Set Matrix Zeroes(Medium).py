from typing import List


class Solution:

    def setZeroes(self, matrix: List[List[int]]):
        """
        Do not return anything, modify matrix in-place instead.
        """

        iscol = 0
        isrow = 0
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            if not matrix[i][0]:
                iscol = True
                break
        for i in range(n):
            if not matrix[0][i]:
                isrow = True
                break

        for i in range(1, m):
            for j in range(1, n):
                if not matrix[i][j]:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        for i in range(1, m):
            for j in range(1, n):
                if not matrix[i][0] or not matrix[0][j]:
                    matrix[i][j] = 0

        if iscol:
            for i in range(m):
                matrix[i][0] = 0
        if isrow:
            for i in range(n):
                matrix[0][i] = 0

        return matrix

    def setZeroes1(self, matrix: List[List[int]]):
        """
        Do not return anything, modify matrix in-place instead.
        """

        col = set()
        row = set()
        m = len(matrix)
        n = len(matrix[0])
        for i in range(m):
            for j in range(n):
                if not matrix[i][j]:
                    col.add(j)
                    row.add(i)

        for i in range(m):
            for j in range(n):
                if i in row or j in col:
                    matrix[i][j] = 0

        return matrix


if __name__ == '__main__':
    print(Solution().setZeroes(matrix=[[0, 1, 2, 0],
                                       [3, 4, 5, 2],
                                       [1, 3, 1, 5]]))
