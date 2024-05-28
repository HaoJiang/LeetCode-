# There are N network nodes, labelled 1 to N.
#
# Given times, a list of travel times as directed edges times[i] = (u, v, w),
# where u is the source node, v is the target node, and w is the time it takes for a signal to travel from source to target.
#
# Now, we send a signal from a certain node K. How long will it take for all nodes to receive the signal? If it is impossible, return -1.
#
# Input: times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]], N = 4, K = 2
# Output: 2
#
#
# Note:
#
# N will be in the range [1, 100].
# K will be in the range [1, N].
# The length of times will be in the range [1, 6000].
# All edges times[i] = (u, v, w) will have 1 <= u, v <= N and 0 <= w <= 100.

from typing import List


class Solution:
    def networkDelayTime(self, times: List[List[int]], N: int, K: int) -> int:
        from collections import defaultdict
        import heapq
        mp = defaultdict(set)

        for u, v, w in times:
            mp[u].add((v, w))
        dist = {}
        if K not in mp:
            return -1
        dq = [(0, K)]
        while dq:
            time, currNode = heapq.heappop(dq)
            if currNode not in dist:
                dist[currNode] = time
                for bor, time2 in mp[currNode]:
                    if bor not in dist:
                        heapq.heappush(dq, (time + time2, bor))
        return max(dist.values()) if len(dist) == N else -1


if __name__ == "__main__":
    times = [[0, 2, 10],
             [0, 4, 30],
             [0, 5, 100],
             [1, 2, 5],
             [2, 3, 50],
             [3, 5, 10],
             [4, 3, 20],
             [4, 5, 60]]
    N = 6
    K = 0
    print(Solution().networkDelayTime(times, N, K))
