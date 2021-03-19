# Given a matrix of M x N elements (M rows, N columns), return all elements of the matrix in diagonal order as shown in the below image.
#
# Input:
# [
#  [ 1, 2, 3 ],
#  [ 4, 5, 6 ],
#  [ 7, 8, 9 ]
# ]
#
# Output:  [1,2,4,7,5,3,6,8,9]

class Solution(object):
    def findDiagonalOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        from collections import defaultdict

        dt = defaultdict(list)
        res = []
        for i in range(len(matrix)):
            for j in range(len(matrix[i])):
                dt[i + j].append(matrix[i][j])

        for p in dt.items():
            res.extend(p[1][::-1])
            # if p[0] % 2:
            #     res.extend(p[1])
            # else:
            #     res.extend(p[1][::-1])

        print(res, dt)
        return res

    def findDiagonalOrderBFS(self, nums):
        ans = []
        m = len(nums)
        from collections import deque
        queue = deque([(0, 0)])
        while queue:
            row, col = queue.popleft()
            ans.append(nums[row][col])
            # we only add the number at the bottom if we are at column 0
            if col == 0 and row + 1 < m:
                queue.append((row + 1, col))
            # add the number on the right
            if col + 1 < len(nums[row]):
                queue.append((row, col + 1))

        return ans

    # 由观察可以得知，一共有两种走法，向右上方走和向左下方走。
    #
    # 再由二维数组的特性可以得知，向右上方走实际上等于
    # x -= 1, y += 1, 向左下方走实际上等于
    # x += 1, y -= 1
    #
    # 当向右上方走的时候，有两种情况会造成碰壁，因而需要转弯，
    #    CASE
    # 1: 碰到上方的壁(x无法再 - 1), 但还没碰到右方的壁（y可以 + 1）
    #               在这种情况下，下一步的坐标为
    # y += 1, 比如图里的
    # 1 --> 2
    #    CASE
    # 2: 碰到右方的壁(y无法再 + 1)
    #               在这种情况下, 下一步的坐标为
    # x += 1, 比如图里的
    # 3 --> 6
    # 向左下方走同理：
    #    CASE
    # 1: 碰到左方的壁(y无法再 - 1), 但还没有碰到下方的壁(x可以 + 1)
    # 在这种情况下, 下一步的坐标为
    # x += 1, 比如图里的
    # 4 --> 7
    #    CSSE
    # 2: 碰到下方的壁(x无法再 + 1)
    # 在这种情况下, 下一步的坐标为
    # y += 1, 比如图里的
    # 8 --> 9



if __name__ == "__main__":
    matrix = [[1, 2, 3, 4, 5],
              [6, 7],
              [8],
              [9, 10, 11],
              [12, 13, 14, 15, 16]]
    matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
    print(Solution().findDiagonalOrderBFS(matrix))
