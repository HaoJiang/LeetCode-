# Given an undirected graph, return true if and only if it is bipartite.
#
# Recall that a graph is bipartite if we can split its set of nodes into two independent subsets A and B,
# such that every edge in the graph has one node in A and another node in B.
#
# The graph is given in the following form: graph[i] is a list of indexes j for which the edge between nodes i and j exists.
# Each node is an integer between 0 and graph.length - 1.  There are no self edges or parallel edges: graph[i] does not contain i,
# and it doesn't contain any element twice.
#
# Input: graph = [[1,3],[0,2],[1,3],[0,2]]
# Output: true
# Explanation: We can divide the vertices into two groups: {0, 2} and {1, 3}.
#
#
# Input: graph = [[1,2,3],[0,2],[0,1,3],[0,2]]
# Output: false
# Explanation: We cannot find a way to divide the set of nodes into two independent subsets.

from typing import List


class Solution:
    def isBipartite(self, graph: List[List[int]]) -> bool:
        visited = {}
        stack = []
        for node in range(len(graph)):
            if node not in visited:
                stack.append(node)
                visited[node] = 1
                while stack:
                    curr = stack.pop()
                    for nei in graph[curr]:
                        if nei not in visited:
                            visited[nei] = visited[curr] ^ 1
                            stack.append(nei)
                        else:
                            if visited[curr] == visited[nei]:
                                return False
        return True

    def isBipartite1(self, graph):
        n = len(graph)
        flag = {}
        for node in range(n):
            if node in flag:
                continue
            if not self.dfs(graph, node, flag, True):
                return False
        return True

    def dfs(self, graph, node, flag, painted):
        if node not in flag:
            flag[node] = painted
        else:
            return flag[node] == painted

        for nexts in graph[node]:
            if not self.dfs(graph, nexts, flag, not painted):
                return False
        return True

        #
        # from collections import deque
        # n = len(graph)
        #
        # visited = [0] * n
        # dq = deque()
        # for i in range(n):
        #     if not visited[i]:
        #         dq.append((i, 1))
        #         while dq:
        #             node, color = dq.popleft()
        #             visited[node] = color
        #             color = 2 if color == 1 else 1
        #             for j in graph[node]:
        #                 if not visited[j]:
        #                     dq.append((j, color))
        #                 elif visited[j] != color:
        #                     return False
        #
        # return True


if __name__ == "__main__":
    print(Solution().isBipartite([[1,3],[0,2],[1,3],[0,2]]))
