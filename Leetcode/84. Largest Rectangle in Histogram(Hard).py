# Given n non-negative integers representing the histogram's bar height where the width of each bar is 1, find the area of largest rectangle in the histogram.
# Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
# The largest rectangle is shown in the shaded area, which has area = 10 unit.
#
# Input: [2,1,5,6,2,3]
# Output: 10
#
# https://leetcode.com/problems/largest-rectangle-in-histogram/

class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        if not heights:
            return 0
        if len(heights) == 1:
            return heights
        res = 0
        for i, v in enumerate(heights):
            left = i
            right = i
            while left > 0 and heights[left - 1] >= v:
                left -= 1
            while right < len(heights) - 1 and heights[right + 1] >= v:
                right += 1
            area = (right - left + 1) * v
            res = max(area, res)
        return res

    def largestRetangleArea2(self, height):
        if len(height) <= 1:
            return height
        # add sentinel less code logic better
        # the first 0 never pop  so the stack never empty
        # the sec 0 that will be let arr all elements pop
        height = [0] + height + [0]
        stack = [height[0]]
        res = 0
        for i in range(1, len(height)):
            while height[i] < height[stack[-1]]:
                curheight = height[stack.pop()]
                curwidth = i - stack[-1] - 1
                res = max(res, curheight * curwidth)
            stack.append(i)
        return res


if __name__ == "__main__":
    print(Solution().largestRetangleArea2([2, 2, 5, 6, 2, 2, 2, 2, 2]))
