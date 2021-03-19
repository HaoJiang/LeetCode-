# Given a collection of intervals, merge all overlapping intervals.
# #
# # Example 1:
# #
# # Input: [[1,3],[2,6],[8,10],[15,18]]
# # Output: [[1,6],[8,10],[15,18]]
# # Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].
# # Example 2:
# #
# # Input: [[1,4],[4,5]]
# # Output: [[1,5]]
# # Explanation: Intervals [1,4] and [4,5] are considered overlapping.


class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """

        # if len(intervals) < 2:
        #     return intervals
        # intervals.sort()
        #
        # res = [intervals[0]]
        # for i in range(1, len(intervals)):
        #     if intervals[i][0] > res[-1][1]:
        #         res.append(intervals[i])
        #     else:
        #         res[-1][1] = max(intervals[i][1], res[-1][1])
        # return res

        intervals.sort()
        pos = 0
        for i in range(1, len(intervals)):
            if intervals[i][0] <= intervals[pos][1]:
                if intervals[i][1] > intervals[pos][1]:
                    intervals[pos][1] = intervals[i][1]
            else:
                pos += 1
                intervals[pos] = intervals[i]
        return intervals[:pos + 1]


print(Solution().merge([[1, 4], [2, 3]]))
