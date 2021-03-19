# Given a binary tree, find its minimum depth.
#
# The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.
#
# Note: A leaf is a node with no children.

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        ### we are using top - down
        if not root:
            # no root return 0
            return 0

        elif not root.left or not root.right:
            # left and right both no child just return 1
            return 1

        else:
            if not root.left:
                # if no left just dfs right and plus self root + 1
                return self.minDepth(root.right) + 1
            elif not root.right:
                return self.minDepth(root.left) + 1
            else:
                return min(self.minDepth(root.left) + 1, self.minDepth(root.right) + 1)

    def minDepth1(self, root):
        # bottom - up
        if not root:
            return 0
        if not root.left and root.right:
            return 1

        depth = 10 ** 9

        if root.left:
            depth = min(self.minDepth(root.left), depth)

        if root.right:
            depth = min(self.minDepth(root.right), depth)

        return depth + 1

    def minDepth2(self, root):
        if not root:
            return 0

        from collections import deque

        dq = deque()

        dq.append((root, 1))
        while dq:
            size = len(dq)
            for _ in range(size):
                node, depth = dq.popleft()
                if not node.left and not node.right:
                    return depth
                if node.left:
                    dq.append((root.left, depth + 1))
                if node.right:
                    dq.append((root.right, depth + 1))

        return 0
