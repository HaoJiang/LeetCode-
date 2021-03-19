from typing import List


class Solution:
    def countRestrictedPaths(self, n: int, edges: List[List[int]]) -> int:
        import heapq
        from collections import defaultdict
        import functools
        if n == 1:
            return 0
        graph = defaultdict(list)
        for u, v, w in edges:
            graph[u].append((w, v))
            graph[v].append((w, u))

        # Dijikstra to find shortest distance of paths from node `n` to any other nodes
        minHeap = [(0, n)]  # dist, node
        dist = [float('inf')] * (n + 1)
        dist[n] = 0
        while minHeap:
            d, u = heapq.heappop(minHeap)
            if d != dist[u]:
                continue
            for w, nei in graph[u]:
                if dist[nei] > d + w:
                    dist[nei] = d + w
                    heapq.heappush(minHeap, (dist[nei], nei))

        @functools.lru_cache(None)
        def dfs(src):
            if src == n: return 1  # Find a path to reach to destination
            ans = 0
            for _, nei in graph[src]:
                if dist[src] > dist[nei]:
                    ans += dfs(nei)
            return ans

        return dfs(1) % (10 ** 9 + 7)

if __name__ == '__main__':
    print(Solution().countRestrictedPaths(n = 5, edges = [[1,2,3],[1,3,3],[2,3,1],[1,4,2],[5,2,2],[3,5,1],[5,4,10]]))
