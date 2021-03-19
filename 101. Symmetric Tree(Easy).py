# Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).
#
# For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
#
#     1
#    / \
#   2   2
#  / \ / \
# 3  4 4  3
#
#
# But the following [1,2,2,null,3,null,3] is not:
#
#     1
#    / \
#   2   2
#    \   \
#    3    3

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if not root:
            return True
        stack = []
        stack.append((root.left, root.right))
        while stack:
            left, right = stack.pop()
            if not left and not right:
                continue
            # in the first condition we pass the no left and no right
            # so if left no or right no or left !+ right false
            if not left or not right or (left.val != right.val):
                return False
            else:
                stack.append((left.left, right.right))
                stack.append((left.right, right.left))
        return True
