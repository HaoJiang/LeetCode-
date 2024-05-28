# Definition for a Node.
class Node(object):
    def __init__(self, val=0, neighbors=None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution(object):
    def cloneGraph(self, node):
        """
        :type node: Node
        :rtype: Node
        """
        from collections import deque, defaultdict
        mp = defaultdict(set)



        dq = deque()
        visited = set()
        dq.append(node)
        clone_node = Node(node.val, [])
        dq_clone = deque()
        dq_clone.append(clone_node)
        while dq:
            node = dq.popleft()
            clone_node = dq_clone.popleft()
            for nei in node.neighbors:
                if (node.val, nei.val) not in visited:
                    nei_clone = Node(nei.val, [])
                    clone_node.neighbors.append(nei_clone)
                    visited.add((node.val, nei.val))
                    dq.append(nei)
                    dq_clone.append(nei_clone)
        return dq_clone


if __name__ == "__main__":
    adjList = [[2, 4], [1, 3], [2, 4], [1, 3]]
    print(Solution().cloneGraph(adjList))
