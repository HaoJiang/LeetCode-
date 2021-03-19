class NumMatrix:
    from typing import List

    def __init__(self, matrix: List[List[int]]):
        m = len(matrix)
        n = len(matrix[0])
        self.prefixmatrix = [[0] * (n + 1) for _ in range(m + 1)]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                self.prefixmatrix[i][j] = matrix[i - 1][j - 1] + self.prefixmatrix[i - 1][j] + self.prefixmatrix[i][
                    j - 1] - self.prefixmatrix[i - 1][j - 1]
        print(self.prefixmatrix)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        return self.prefixmatrix[row2 + 1][col2 + 1] - self.prefixmatrix[row1][col2 + 1] - self.prefixmatrix[row2+1][
            col1] + \
               self.prefixmatrix[row1][col1]

    # Your NumMatrix object will be instantiated and called as such:


# [[0, 0, 0, 0, 0, 0],
#  [0, 3, 3, 4, 8, 10],
#  [0, 8, 14, 18, 24, 27],
#  [0, 9, 17, 21, 28, 36],
#  [0, 13, 22, 26, 34, 49],
#  [0, 14, 23, 30, 38, 58]]
matrix = [
    [3, 0, 1, 4, 2],
    [5, 6, 3, 2, 1],
    [1, 2, 0, 1, 5],
    [4, 1, 0, 1, 7],
    [1, 0, 3, 0, 5]
]
obj = NumMatrix(matrix)
row1 = 2
col1 = 1
row2 = 4
col2 = 3
param_1 = obj.sumRegion(row1, col1, row2, col2)
print(param_1)
