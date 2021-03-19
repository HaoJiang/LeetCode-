# Given a rows x cols binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.
#
# Input: matrix = [["1", "0", "1", "0", "0"],
#                  ["1", "0", "1", "1", "1"],
#                  ["1", "1", "1", "1", "1"],
#                  ["1", "0", "0", "1", "0"]]
# Output: 6
#
# Example 2:
#
# Input: matrix = []
# Output: 0
#
# Input: matrix = [["0"]]
# Output: 0
#
# Input: matrix = [["1"]]
# Output: 1
#
# Input: matrix = [["0","0"]]
# Output: 0

class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        if not matrix:
            return 0

        def largesttranglesArea(heights):
            heights = [0] + heights + [0]
            stack = [0]
            res = 0
            for i in range(1, len(heights)):
                while heights[i] < heights[stack[-1]]:
                    curheight = heights[stack.pop()]
                    curwidth = i - stack[-1] - 1
                    area = curheight * curwidth
                    res = max(res, area)
                stack.append(i)
            return res

        dp = [[0] * len(matrix[0]) for m in range(len(matrix))]
        # Input: matrix = [["1", "0", "1", "0", "0"],
        #                  ["1", "0", "1", "1", "1"],
        #                  ["1", "1", "1", "1", "1"],
        #                  ["1", "0", "0", "1", "0"]]
        # easy row we can use 84 largesttangle algo cul this questions
        #  [["1", "0", "1", "0", "0"],
        #   ["2", "0", "2", "1", "1"],
        #   ["3", "1", "3", "2", "2"],
        #   ["4", "0", "0", "3", "0"]]

        for i in range(len(dp)):  # row
            for j in range(len(dp[0])):  # col
                if matrix[i][j] == "1":
                    dp[i][j] = dp[i - 1][j] + 1
        return max([largesttranglesArea(dp[i]) for i in range(len(dp))])


if __name__ == "__main__":
    matrix = [["1", "0", "1", "0", "0"],
              ["1", "0", "1", "1", "1"],
              ["1", "1", "1", "1", "1"],
              ["1", "0", "0", "1", "0"]]
    print(Solution().maximalRectangle(matrix))
