# Input: root = [3,5,1,6,2,0,8,null,null,7,4], target = 5, K = 2
#
# Output: [7,4,1]
#
# Explanation:
# The nodes that are a distance 2 from the target node (with value 5)
# have values 7, 4, and 1.
#


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from typing import List


class Solution:
    def distanceK(self, root, target, K: int) -> List[int]:
        from collections import deque
        def dfsaddpar(root, par):
            if root:
                root.par = par
                dfsaddpar(root.left, root)
                dfsaddpar(root.right, root)

        dfsaddpar(root, None)

        dq = deque([(target, K)])

        seen = set()
        seen.add(target)
        res = []
        while dq:
            node, dis = dq.popleft()
            if not dis:
                res.append(node)
                continue
            for nei in (node.par, node.left, node.right):
                if nei and nei not in seen:
                    dq.append((nei, dis - 1))

        return res
