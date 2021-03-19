# # Given an array of events where events[i] = [startDayi, endDayi]. Every event i starts at startDayi and ends at endDayi.
# #
# # You can attend an event i at any day d where startTimei <= d <= endTimei. Notice that you can only attend one event at any time d.
# #
# # Return the maximum number of events you can attend.
#
# Input: events = [[1,2],[2,3],[3,4]]
# Output: 3
# Explanation: You can attend all the three events.
# One way to attend them all is as shown.
# Attend the first event on day 1.
# Attend the second event on day 2.
# Attend the third event on day 3.
# Example 2:
#
# Input: events= [[1,2],[2,3],[3,4],[1,2]]
# Output: 4
# Example 3:
#
# Input: events = [[1,4],[4,4],[2,2],[3,4],[1,1]]
# Output: 4
# Example 4:
#
# Input: events = [[1,100000]]
# Output: 1
# Example 5:
#
# Input: events = [[1,1],[1,2],[1,3],[1,4],[1,5],[1,6],[1,7]]
# Output: 7


class Solution(object):
    def maxEvents(self, events):
        """
        :type events: List[List[int]]
        :rtype: int
        """

        events.sort(key=lambda x: x[1])
        res = set()
        for s, e in events:
            for i in range(s, e + 1):
                if i not in res:
                    res.add(i)
                    break
        return len(res)

    ## O(n2) TLE

    def maxEvents_heap(self, events):

        import heapq

        events = heapq.heapify(events)

        day = events[0][0]
        res = 0
        while events:
            s, e = heapq.heappop(events)
            if day > e:
                continue
            elif s < day:
                heapq.heappush(events, [day, e])
            else:
                day = max(s + 1, day + 1)
                res += 1

        return res

    def maxEvents_heap___1(self, events):
        import heapq
        events.sort(reverse=1)
        h = []
        res = d = 0
        while events or h:
            if not h:
                d = events[-1][0]
            while events and events[-1][0] == d:
                heapq.heappush(h, events.pop()[1])
            heapq.heappop(h)
            res += 1
            d += 1
            while h and h[0] < d:
                heapq.heappop(h)
        return res


print(Solution().maxEvents_heap___1([[1, 2], [1, 2], [1, 1], [1, 5], [2, 2], [4, 4]]))
