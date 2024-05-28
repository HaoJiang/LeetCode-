class Solution:
    # check graph is tree
    # 1 check graph  is connected    means len(edges) != n-1
    # 2 check cycle
    def gvt(self, n, edges):
        from collections import defaultdict, deque

        if len(edges) != n - 1:
            return False

        mp = defaultdict(set)

        for i in edges:
            mp[i[0]].add(i[1])
            mp[i[1]].add(i[0])

        dq = deque()
        dq.append(0)
        visited = set()
        while dq:
            node = dq.popleft()
            visited.add(node)

            for i in mp[node]:
                if i not in visited:
                    dq.append(i)
                    visited.add(i)

        return len(visited) == n
