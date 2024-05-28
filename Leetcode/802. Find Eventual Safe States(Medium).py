# We start at some node in a directed graph, and every turn, we walk along a directed edge of the graph. If we reach a terminal node (that is, it has no outgoing directed edges), we stop.
#
# We define a starting node to be safe if we must eventually walk to a terminal node. More specifically, there is a natural number k, so that we must have stopped at a terminal node in less than k steps for any choice of where to walk.
#
# Return an array containing all the safe nodes of the graph. The answer should be sorted in ascending order.
#
# The directed graph has n nodes with labels from 0 to n - 1, where n is the length of graph. The graph is given in the following form: graph[i] is a list of labels j such that (i, j) is a directed edge of the graph, going from node i to node j.
#
# Input: graph = [[1,2],[2,3],[5],[0],[5],[],[]]
# Output: [2,4,5,6]
# Explanation: The given graph is shown above.
#
# Input: graph = [[1,2,3,4],[1,2],[3,4],[0,4],[]]
# Output: [4]

class Solution:

    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        # 0: non-visited
        # 1: safe
        # 2: unsafe
        n = len(graph)
        color = [0] * n
        res = []

        for i in range(len(graph)):
            if self.dfs(graph, i, color):
                res.append(i)

        return res

    def dfs(self, graph, start, color):
        if color[start] == 2:
            return False
        elif color[start] == 1:
            return True

        color[start] = 2
        for end in graph[start]:

            if not self.dfs(graph, end, color):
                return False

        color[start] = 1

        return True


    # def eventualSafeNodes(self, graph):
    #
    #     ## find cycle    graph outdgree = 0 mean safe no cycle
    #
    #     from collections import defaultdict, deque
    #     # graph = [[1, 2], [2, 3], [5], [0], [5], [], []]
    #     mp = defaultdict(set)
    #     dq = deque()
    #     outdegree = [0] * len(graph)
    #     for i, v in enumerate(graph):
    #         if v:
    #             for j in v:
    #                 mp[j].add(i)
    #             outdegree[i] = len(v)
    #         else:
    #             dq.append(i)
    #
    #     # dq = deque([i for i in range(len(graph)) if not outdegree[i]])
    #     # res = []
    #     while dq:
    #         size = len(dq)
    #         for _ in range(size):
    #             node = dq.popleft()
    #             if node in mp:
    #                 while mp[node]:
    #                     neighbor = mp[node].pop()
    #                     outdegree[neighbor] -= 1
    #                     if not outdegree[neighbor]:
    #                         dq.append(neighbor)
    #             # res.append(node)
    #
    #     return [i for i, v in enumerate(outdegree) if not v]
    #     # for neighbor in mp[node]:


if __name__ == "__main__":
    print(Solution().eventualSafeNodes([[1, 2], [2, 3], [5], [0], [5], [], []]))
