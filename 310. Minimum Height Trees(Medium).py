# A tree is an undirected graph in which any two vertices are connected by exactly one path. In other words,
# any connected graph without simple cycles is a tree.
#
# Given a tree of n nodes labelled from 0 to n - 1,
# and an array of n - 1 edges where edges[i] = [ai, bi] indicates that there is an undirected edge between the two nodes ai and bi in the tree,
# you can choose any node of the tree as the root. When you select a node x as the root, the result tree has height h. Among all possible rooted trees,
# those with minimum height (i.e. min(h))  are called minimum height trees (MHTs).
#
# Return a list of all MHTs' root labels. You can return the answer in any order.
#
# The height of a rooted tree is the number of edges on the longest downward path between the root and a leaf.
#
# Input: n = 4, edges = [[1,0],[1,2],[1,3]]
# Output: [1]
# Explanation: As shown, the height of the tree is 1 when the root is the node with label 1 which is the only MHT.
#
# Input: n = 6, edges = [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]
# Output: [3, 4]
#
#
# Input: n = 2, edges = [[0,1]]
# Output: [0,1]

class Solution:
    def findMinHeightTrees(self, n, edges):
        if n == 1:
            return []
        elif n == 2:
            return [0]

        from collections import defaultdict, deque

        mp = defaultdict(list)
        # undirected graph
        for i in edges:
            mp[i[0]].append(i[1])
            mp[i[1]].append(i[0])

        dq = deque()

        for i in range(n):
            if len(mp[i]) == 1:
                dq.append(i)
        while n > 2:
            size = len(dq)
            n -= size
            for _ in range(size):
                node = dq.popleft()
                neighbor = mp[node].pop()
                mp[neighbor].remove(node)
                if len(mp[neighbor]) == 1:
                    dq.append(neighbor)

        return dq









if __name__ == "__main__":
    print(Solution().findMinHeightTrees(6, [[3, 0], [3, 1], [3, 2], [3, 4], [5, 4]]))
