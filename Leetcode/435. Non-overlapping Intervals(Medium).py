# Example 1:
#
# Input: [[1,2],[2,3],[3,4],[1,3]]
# Output: 1
# Explanation: [1,3] can be removed and the rest of intervals are non-overlapping.
# Example 2:
#
# Input: [[1,2],[1,2],[1,2]]
# Output: 2
# Explanation: You need to remove two [1,2] to make the rest of intervals non-overlapping.
# Example 3:
#
# Input: [[1,2],[2,3]]
# Output: 0
# Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

# You may assume the interval's end point is always bigger than its start point.
# Intervals like [1,2] and [2,3] have borders "touching" but they don't overlap each other.


class Solution(object):
    def eraseOverlapIntervals(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: int
        """
        # intervals.sort()
        #
        # j = 0
        # # left = intervals[0][0]
        # right = intervals[0][1]
        # for i in range(1, len(intervals)):
        #     if intervals[i][0] >= right:
        #         # left = intervals[i][0]
        #         right = intervals[i][1]
        #     else:
        #         if right > intervals[i][1]:
        #             # left = intervals[i][0]
        #             right = intervals[i][1]
        #         j += 1
        #
        # return j

        intervals.sort(key=lambda x: x[1])

        j = 1
        # left = intervals[0][0]
        right = intervals[0][1]
        for i in range(1, len(intervals)):
            if intervals[i][0] >= right:
                right = intervals[i][1]
                j += 1

        return len(intervals) - j


print(Solution().eraseOverlapIntervals([[1, 2], [2, 3]]))
