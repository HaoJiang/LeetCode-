# Given a directed acyclic graph (DAG) of n nodes labeled from 0 to n - 1,
# find all possible paths from node 0 to node n - 1, and return them in any order.
#
# The graph is given as follows: graph[i] is a list of all nodes you can visit from node i
# (i.e., there is a directed edge from node i to node graph[i][j]).
#
# Input: graph = [[1,2],[3],[3],[]]
# Output: [[0,1,3],[0,2,3]]
# Explanation: There are two paths: 0 -> 1 -> 3 and 0 -> 2 -> 3.
#
#
# Input: graph = [[4,3,1],[3,2,4],[3],[4],[]]
# Output: [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
#
#
# Input: graph = [[1,2,3],[2],[3],[]]
# Output: [[0,1,2,3],[0,2,3],[0,3]]
#
# Input: graph = [[1,3],[2],[3],[]]
# Output: [[0,1,2,3],[0,3]]
#
# Constraints:
#
# n == graph.length
# 2 <= n <= 15
# 0 <= graph[i][j] < n
# graph[i][j] != i (i.e., there will be no self-loops).
# The input graph is guaranteed to be a DAG.
from typing import List
class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        from collections import deque

        dq = deque()
        dq.append((0, [0]))
        res = []
        n = len(graph) - 1
        while dq:
            node, path = dq.popleft()
            if node == n:
                res.append(path)
            for i in graph[node]:
                dq.append((i, path + [i]))
        return res




        # def dfs(curr, path):
        #     if curr == n:
        #         self.res.append(path)
        #
        #     for nei in graph[curr]:
        #         dfs(nei, path + [nei])
        # n = len(graph) - 1
        # self.res = []
        # dfs(0, [0])
        # return self.res

if __name__ == "__main__":
    graph = [[1, 3], [2], [3], []]
    print(Solution().allPathsSourceTarget(graph))