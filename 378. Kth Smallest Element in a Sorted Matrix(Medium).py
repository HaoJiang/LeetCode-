# Given a n x n matrix where each of the rows and columns are sorted in ascending order, find the kth smallest element in the matrix.
#
# Note that it is the kth smallest element in the sorted order, not the kth distinct element.
#
# Example:
#
# matrix = [
#    [ 1,  5,  9],
#    [10, 11, 13],
#    [12, 13, 15]
# ],
# k = 8,
#
# return 13.
#
# Note:
# You may assume k is always valid, 1 ≤ k ≤ n2.

class Solution(object):
    def kthSmallest(self, matrix, k):
        """
        :type matrix: List[List[int]]
        :type k: int
        :rtype: int
        """
        # import heapq
        # if not matrix:
        #     return
        #
        # m = len(matrix)
        # n = len(matrix[0])
        # hq = []
        # if k < m * n // 2:
        #     # using maxheap
        #     k = m * n - k + 1
        #     for i in range(m):
        #         for j in range(n):
        #             if k == 0:
        #                 heapq.heappushpop(hq, -matrix[i][j])
        #             else:
        #                 heapq.heappush(hq, -matrix[i][j])
        #                 k -= 1
        # else:
        #     # using minheap
        #     for i in range(m):
        #         for j in range(n):
        #             if k == 0:
        #                 heapq.heappushpop(hq, matrix[i][j])
        #             else:
        #                 heapq.heappush(hq, matrix[i][j])
        #                 k -= 1
        # return -heapq.heappop(hq)

        n = len(matrix)
        left = matrix[0][0]
        right = matrix[n - 1][n - 1]

        def calNums(midvalue):
            row, col = n - 1, 0
            nums = 0
            while row >= 0 and col < n:
                if midvalue >= matrix[row][col]:
                    nums += row + 1
                    col += 1
                else:
                    row -= 1
            return nums >= k

        while left < right:
            mid = left + (right - left) // 2
            if calNums(mid):
                right = mid
            else:
                left = mid + 1

        return left


if __name__ == "__main__":
    matrix = [
        [1, 5, 9],
        [10, 11, 13],
        [12, 13, 15]
    ]
    print(Solution().kthSmallest(matrix, 8))
