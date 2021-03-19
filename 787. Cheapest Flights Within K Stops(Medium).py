# There are n cities connected by m flights. Each flight starts from city u and arrives at v with a price w.
#
# Now given all the cities and flights, together with starting city src and the destination dst,
# your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.
#
# Example
# 1:
# Input:
# n = 3, edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
# src = 0, dst = 2, k = 1
# Output: 200
# Explanation:The graph looks like this:
# The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.
#
# Example
# 2:
# Input:
# n = 3, edges = [[0, 1, 100], [1, 2, 100], [0, 2, 500]]
# src = 0, dst = 2, k = 0
# Output: 500
# Explanation:
# The cheapest price from city 0 to city 2 with at most 0 stop costs 500, as marked blue in the picture.
#

from typing import List


class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:

        from collections import defaultdict
        import heapq
        graph = defaultdict(list)
        for u, v, w in flights:
            graph[u].append((v, w))
        Q = [(0, src, 0)]
        while Q:
            dist, i, k = heapq.heappop(Q)
            #print(i, graph[i])
            if i == dst:
                return dist
            if k <= K:
                for j, w in graph[i]:
                    #print(i, "->", j, "=", w)
                    heapq.heappush(Q, (dist + w, j, k + 1))
        return -1




if __name__ == "__main__":
    n = 10
    edges = [[3,4,4],[2,5,6],[4,7,10],[9,6,5],[7,4,4],[6,2,10],[6,8,6],[7,9,4],[1,5,4],[1,0,4],[9,7,3],[7,0,5],[6,5,8],[1,7,6],[4,0,9],[5,9,1],[8,7,3],[1,2,6],[4,1,5],[5,2,4],[1,9,1],[7,8,10],[0,4,2],[7,2,8]]
    src = 6
    dst = 0
    k = 7
    print(Solution().findCheapestPrice(n, edges, src, dst, k))
