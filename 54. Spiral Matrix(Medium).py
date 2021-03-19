# Given a matrix of m x n elements (m rows, n columns), return all elements of the matrix in spiral order.
#
# Example 1:
#
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
# Output: [1,2,3,6,9,8,7,4,5]
#
# Example 2:
#
# Input:
# [
#   [1, 2, 3, 4],
#   [5, 6, 7, 8],
#   [9,10,11,12]
# ]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]

class Solutions(object):
    def spiralMatrix(self, matrix):
        if not matrix or not matrix[0]:
            return []

        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1
        res = []
        while top < bottom and left < right:
            for i in range(left, right):
                res.append(matrix[top][i])
            for i in range(top, bottom):
                res.append(matrix[i][right])
            for i in range(right, left, - 1):
                res.append(matrix[bottom][i])
            for i in range(bottom, top, -1):
                res.append(matrix[left][i])

            left += 1
            right -= 1
            top += 1
            bottom -= 1

        if left == right:
            for i in range(top, bottom + 1):
                res.append(matrix[left][i])
        elif top == bottom:
            for i in range(left, right + 1):
                res.append(matrix[top][i])

        return res


if __name__ == "__main__":
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    print(Solutions().spiralMatrix(matrix))
