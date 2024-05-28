# Given a positive integer n, generate a square matrix filled with elements from 1 to n2 in spiral order.
#
# Example:
#
# Input: 3
# Output:
# [
#     [1, 2, 3],
#     [8, 9, 4],
#     [7, 6, 5]
# ]


class Solution(object):
    def genMatrix(self, n):
        if not n:
            return []
        matrix = [[1] * n for _ in range(n)]
        print(matrix)
        top = 0
        bottom = n - 1
        left = 0
        right = n - 1
        count = 1
        while left < right and top < bottom:
            for i in range(left, right):
                matrix[top][i] = count
                count += 1
            for i in range(top, bottom):
                matrix[i][right] = count
                count += 1
            for i in range(right, left, -1):
                matrix[bottom][i] = count
                count += 1
            for i in range(bottom, top, -1):
                matrix[i][left] = count
                count += 1
            left += 1
            right -= 1
            top += 1
            bottom -= 1

        if n % 2:
            matrix[top][left] = count

        return matrix


if __name__ == "__main__":
    print(Solution().genMatrix(4))
