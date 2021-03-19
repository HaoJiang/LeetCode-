# Consider a directed graph, with nodes labelled 0, 1, ..., n-1.  In this graph, each edge is either red or blue,
# and there could be self-edges or parallel edges.
#
# Each [i, j] in red_edges denotes a red directed edge from node i to node j.
#
# Similarly, each [i, j] in blue_edges denotes a blue directed edge from node i to node j.
#
# Return an array answer of length n, where each answer[X] is the length of the shortest path
# from node 0 to node X such that the edge colors alternate along the path (or -1 if such a path doesn't exist).
#
# Example 1:
#
# Input: n = 3, red_edges = [[0,1],[1,2]], blue_edges = []
# Output: [0,1,-1]
# Example 2:
#
# Input: n = 3, red_edges = [[0,1]], blue_edges = [[2,1]]
# Output: [0,1,-1]
# Example 3:
#
# Input: n = 3, red_edges = [[1,0]], blue_edges = [[2,1]]
# Output: [0,-1,-1]
# Example 4:
#
# Input: n = 3, red_edges = [[0,1]], blue_edges = [[1,2]]
# Output: [0,1,2]
# Example 5:
#
# Input: n = 3, red_edges = [[0,1],[0,2]], blue_edges = [[1,0]]
# Output: [0,1,1]
from typing import List


class Solution:
    def shortestAlternatingPaths(self, n: int, red_edges: List[List[int]], blue_edges: List[List[int]]) -> List[int]:
        from collections import defaultdict, deque
        dq = deque()
        gp = defaultdict(set)

        for i in red_edges:
            gp[i[0]].add((i[1], 'R'))

        for i in blue_edges:
            gp[i[0]].add((i[1], 'B'))
        res = [-1 for i in range(n)]
        visited = set()

        dq.append((0, 'None', -1))
        while dq:
            curr, color, distance = dq.popleft()
            distance += 1
            if res[curr] == -1:
                res[curr] = distance

            for bor in gp[curr]:
                if color and color != bor[1]:
                    if (curr, bor[0], bor[1]) not in visited:
                        visited.add((curr, bor[0], bor[1]))
                        dq.append((bor[0], bor[1], distance))
        return res


if __name__ == "__main__":
    n = 3
    red_edges = [[0, 1]]
    blue_edges = [[1, 2]]
    print(Solution().shortestAlternatingPaths(n, red_edges, blue_edges))
