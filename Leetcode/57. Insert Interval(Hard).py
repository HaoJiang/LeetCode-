# Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).
#
# You may assume that the intervals were initially sorted according to their start times.
#
# Example 1:
#
# Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
# Output: [[1,5],[6,9]]
# Example 2:
#
# Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
# Output: [[1,2],[3,10],[12,16]]
# Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].


class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """

        newnums = []
        for i in range(len(intervals)):
            if newInterval[0] < intervals[i][0]:
                intervals.insert(i, newInterval)
                break
        else:
            intervals.append(newInterval)
        for i in intervals:
            if not newnums or i[0] > newnums[-1][1]:
                newnums.append(i)
            else:
                newnums[-1][1] = max(newnums[-1][1], i[1])

        return newnums



