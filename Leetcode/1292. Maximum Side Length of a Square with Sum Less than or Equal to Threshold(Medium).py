from typing import List


class Solution:
    def maxSideLength(self, mat: List[List[int]], threshold: int) -> int:
        rows = len(mat)
        cols = len(mat[0])
        prefix = [(cols + 1) * [0] for i in range(rows + 1)]

        for i in range(1, rows + 1):
            for j in range(1, cols + 1):
                prefix[i][j] = mat[i - 1][j - 1] + prefix[i - 1][j] + prefix[i][j - 1] - prefix[i - 1][j - 1]

        def ispossible(k):
            for i in range(rows - k + 1):  # + 1 means prefix m + 1 n + 1
                for j in range(cols - k + 1):
                    if prefix[i + k][j + k] - prefix[i][j + k] - prefix[i + k][j] + prefix[i][j] <= threshold:
                        return True
            return False

        left = 0
        right = min(rows, cols)

        while left < right:
            #### [left , mid - 1]   [mid, right]
            mid = left + (right - left + 1) // 2
            if ispossible(mid):
                left = mid
            else:
                right = mid - 1
        return left


if __name__ == "__main__":
    print(Solution().maxSideLength([[1000, 0, 0, 1], [1, 0, 0, 0], [1, 0, 0, 0], [1, 0, 0, 0]], 6))

    # [[1, 1, 1, 1],
    #  [1, 0, 0, 0],
    #  [1, 0, 0, 0],
    #  [1, 0, 0, 0]]

    # [[0, 0, 0, 0, 0],
    #  [0, 1, 2, 3, 4],
    #  [0, 2, 3, 4, 5],
    #  [0, 3, 4, 5, 6],
    #  [0, 4, 5, 6, 7]]

    # [[1, 1, 3, 2, 4, 3, 2],
    #  [1, 1, 3, 2, 4, 3, 2],
    #  [1, 1, 3, 2, 4, 3, 2]]

    # [[0, 0, 0, 0, 0, 0, 0, 0],
    #  [0, 1, 2, 5, 7, 11, 14, 16],
    #  [0, 2, 4, 10, 14, 22, 28, 32],
    #  [0, 3, 6, 15, 21, 33, 42, 48]]

    # 查找的正方形的边长越长，其计算出来的元素总和越大。我们可以二分正方形的边长，在满足阈值条件下尽可能地扩大正方形的边长，其等价于在升序数组中查找一个小于等于 k 的最大元素。
    # m = len(mat)
    # n = len(mat[0])
    # dp = [[0 for i in range(n + 1)] for j in range(m + 1)]
    #
    # for i in range(1, m + 1):
    #     for j in range(1, n + 1):
    #         # 计算prefix sum用来后续快速计算区域内元素总和。注意prefix sum公式，多加的一部分需要去掉。
    #         dp[i][j] = mat[i - 1][j - 1] + dp[i - 1][j] + dp[i][j - 1] - dp[i - 1][j - 1]
    #
    # def is_square_threshold(k):
    #     # 这个helper method计算的是，以dp[i][j] 为右下角，k为边长的正方形的区域内元素总和是否小于等于threshold（即满足题目要求）
    #     for i in range(m - mid + 1):
    #         for j in range(n - mid + 1):
    #             if threshold >= dp[i + mid][j + mid] - dp[i + mid][j] - dp[i][j + mid] + dp[i][j]:
    #                 return True
    #     return False
    #
    # left = 0  # 最小边长
    # right = min(m, n) # 最大边长
    # while left < right:
    #     # 划分 [left, mid - 1] 与 [mid, right] ，mid 被分到右边，对应 mid = left + (right - left + 1) // 2
    #     mid = left + (right - left + 1) // 2
    #
    #     if is_square_threshold(mid):
    #         # 当前mid能满足threshold要求，说明left设置的太小了，下一轮搜索[mid, right]
    #         left = mid
    #     else:
    #         # 当前mid不能满足threshold要求，说明right设置的太大了，下一轮搜索[left, mid - 1]
    #         right = mid - 1
    # return left
    #
